#!/usr/bin/env python3
"""Factory validation + index adapter (the optional Python adapter, per ARCHITECTURE §9).

Powers scripts/validate, scripts/check-links, and scripts/build-index. Shell
entrypoints call this when Python is available; structure/placeholder checks also
exist in pure shell so the basic path needs no runtime.

Subcommands:
  validate   structure + frontmatter agreement + schema + links (the full gate)
  links      reference resolution + cycle detection only
  index      emit the catalog index (index.json)

Exit codes: 0 = ok (pending links are warnings), 1 = failures, 2 = missing deps.
"""
import sys, os, glob, json, argparse

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required for the Python validation adapter "
          "(`pip install pyyaml`).", file=sys.stderr)
    sys.exit(2)

try:
    from jsonschema import Draft202012Validator
    from referencing import Registry, Resource
    HAVE_JSONSCHEMA = True
except ImportError:
    HAVE_JSONSCHEMA = False

# ── artifact model (mirrors /standards/architecture.md) ──────────────────────
SPEC_FILE = {"skill": "SKILL.md", "agent": "AGENT.md", "workflow": "WORKFLOW.md",
             "team": "TEAM.md", "playbook": "PLAYBOOK.md"}
CORE_FILES = ["README.md", "metadata.yaml", "CHANGELOG.md"]
# Recommended docs differ by artifact type (warn-if-missing, never fail). Skills carry the
# full doc set; roles/orchestrators (agent/team/workflow/playbook) need cross-links + review,
# but EXAMPLES/TROUBLESHOOTING are skill-oriented and not expected of them.
RECOMMENDED_BY_TYPE = {
    "skill":    ["EXAMPLES.md", "TROUBLESHOOTING.md", "RESOURCES.md", "REVIEW.md"],
    "agent":    ["RESOURCES.md", "REVIEW.md"],
    "team":     ["RESOURCES.md"],
    "workflow": ["RESOURCES.md", "REVIEW.md"],
    "playbook": ["RESOURCES.md", "REVIEW.md"],
}
AGREE_KEYS = ["name", "description", "version", "category", "runtime",
              "min_standard", "license"]

C = {"red": "\033[31m", "yellow": "\033[33m", "green": "\033[32m", "z": "\033[0m"}
def col(s, c):
    return f"{C[c]}{s}{C['z']}" if sys.stdout.isatty() else s

def load(p):
    with open(p, encoding="utf-8") as f:
        return yaml.safe_load(f)

def discover():
    """Return list of artifact dicts: {type, id, name, category, path, meta}."""
    arts = []
    # skills: skills/<category>/<name>/
    for m in glob.glob(os.path.join(ROOT, "skills", "*", "*", "metadata.yaml")):
        d = os.path.dirname(m); parts = d.replace("\\", "/").split("/")
        arts.append(_mk("skill", d, m, name=parts[-1], category=parts[-2],
                        id=f"{parts[-2]}/{parts[-1]}"))
    # agents/workflows/teams/playbooks: <type>s/<name>/
    for t in ("agent", "workflow", "team", "playbook"):
        for m in glob.glob(os.path.join(ROOT, t + "s", "*", "metadata.yaml")):
            d = os.path.dirname(m); name = d.replace("\\", "/").split("/")[-1]
            arts.append(_mk(t, d, m, name=name, category=None, id=name))
    return arts

def _mk(t, d, m, name, category, id):
    try:
        meta = load(m) or {}
    except Exception as e:
        meta = {"__error__": str(e)}
    return {"type": t, "path": d, "metafile": m, "name": name,
            "category": category, "id": id, "meta": meta}

def schema_validators():
    if not HAVE_JSONSCHEMA:
        return None
    names = ["metadata.schema.yaml", "skill.schema.yaml", "agent.schema.yaml",
             "team.schema.yaml", "workflow.schema.yaml", "playbook.schema.yaml"]
    reg = Registry().with_resources(
        [(n, Resource.from_contents(load(os.path.join(ROOT, "shared", "schemas", n))))
         for n in names])
    return {n.split(".")[0]: Draft202012Validator(
                load(os.path.join(ROOT, "shared", "schemas", n)), registry=reg)
            for n in names if n != "metadata.schema.yaml"}

def frontmatter(spec_path):
    with open(spec_path, encoding="utf-8") as f:
        txt = f.read()
    if not txt.startswith("---"):
        return None
    try:
        return yaml.safe_load(txt.split("---", 2)[1])
    except Exception:
        return None

# expected target type per composition field
def refs_of(a):
    """Yield (ref_id, expected_type) for an artifact's composition."""
    t, meta = a["type"], a["meta"]
    if t == "skill":
        for d in meta.get("dependencies") or []:
            yield d.get("name"), "skill"
    elif t == "agent":
        for d in meta.get("uses_skills") or []:
            yield d.get("name"), "skill"
    elif t == "team":
        for d in (meta.get("composes") or {}).get("agents") or []:
            yield d.get("name"), "agent"
    elif t == "workflow":
        c = meta.get("composes") or {}
        for d in c.get("skills") or []:    yield d.get("name"), "skill"
        for d in c.get("agents") or []:    yield d.get("name"), "agent"
        for d in c.get("workflows") or []: yield d.get("name"), "workflow"
    elif t == "playbook":
        c = meta.get("composes") or {}
        for d in c.get("teams") or []:     yield d.get("name"), "team"
        for d in c.get("workflows") or []: yield d.get("name"), "workflow"

def cmd_validate(arts, do_schema=True):
    errors, warns = [], []
    sv = schema_validators() if do_schema else None
    if do_schema and sv is None:
        warns.append("jsonschema/referencing not installed — schema validation SKIPPED "
                     "(`pip install jsonschema referencing`).")
    for a in arts:
        aid = f"{a['type']}:{a['id']}"
        meta = a["meta"]
        if "__error__" in meta:
            errors.append(f"{aid}: metadata.yaml parse error: {meta['__error__']}"); continue
        # structure
        spec = SPEC_FILE[a["type"]]
        for f in [spec] + CORE_FILES:
            if not os.path.isfile(os.path.join(a["path"], f)):
                errors.append(f"{aid}: missing required file {f}")
        if a["type"] == "skill" and not os.path.isdir(os.path.join(a["path"], "tests")):
            errors.append(f"{aid}: missing required tests/ directory")
        if a["type"] == "skill" and not os.path.isfile(os.path.join(a["path"], "IMPLEMENTATION.md")):
            errors.append(f"{aid}: missing required file IMPLEMENTATION.md")
        for f in RECOMMENDED_BY_TYPE.get(a["type"], []):
            if not os.path.isfile(os.path.join(a["path"], f)):
                warns.append(f"{aid}: missing recommended file {f}")
        # naming
        if meta.get("name") != a["name"]:
            errors.append(f"{aid}: metadata name '{meta.get('name')}' != folder '{a['name']}'")
        if a["type"] == "skill" and meta.get("category") != a["category"]:
            errors.append(f"{aid}: category '{meta.get('category')}' != folder '{a['category']}'")
        # frontmatter agreement
        sp = os.path.join(a["path"], spec)
        if os.path.isfile(sp):
            fm = frontmatter(sp) or {}
            for k in AGREE_KEYS:
                if k in fm and str(fm.get(k)) != str(meta.get(k)):
                    errors.append(f"{aid}: {spec} '{k}' != metadata.yaml '{k}'")
        # placeholders
        for r, _, files in os.walk(a["path"]):
            for f in files:
                with open(os.path.join(r, f), encoding="utf-8", errors="ignore") as fh:
                    if "{{" in fh.read():
                        errors.append(f"{aid}: leftover placeholder in {os.path.relpath(os.path.join(r,f), a['path'])}")
        # schema
        if sv:
            v = sv.get(a["type"])
            if v:
                for e in v.iter_errors(meta):
                    errors.append(f"{aid}: schema: {e.message}")
    # links (pending = warn, cycle = error)
    le, lw = check_links(arts)
    errors += le; warns += lw
    return errors, warns

def check_links(arts):
    errors, warns = [], []
    sets = {"skill": set(), "agent": set(), "workflow": set(), "team": set(), "playbook": set()}
    for a in arts:
        sets[a["type"]].add(a["id"])
    edges = {}
    for a in arts:
        aid = f"{a['type']}:{a['id']}"
        for ref, exp in refs_of(a):
            if not ref:
                errors.append(f"{aid}: malformed reference (missing name)"); continue
            if ref in sets[exp]:
                edges.setdefault(f"{a['type']}:{a['id']}", []).append(f"{exp}:{ref}")
            else:
                warns.append(f"{aid}: pending reference -> {exp}:{ref} (not yet built)")
    # cycle detection over resolved edges
    WHITE, GREY, BLACK = 0, 1, 2
    color = {}
    def dfs(n, stack):
        color[n] = GREY
        for m in edges.get(n, []):
            if color.get(m, WHITE) == GREY:
                errors.append(f"dependency cycle: {' -> '.join(stack + [m])}")
            elif color.get(m, WHITE) == WHITE:
                dfs(m, stack + [m])
        color[n] = BLACK
    for n in list(edges):
        if color.get(n, WHITE) == WHITE:
            dfs(n, [n])
    return errors, warns

def cmd_index(arts):
    items = []
    for a in sorted(arts, key=lambda x: (x["type"], x["id"])):
        m = a["meta"]
        items.append({"id": a["id"], "type": a["type"], "category": a.get("category"),
                      "title": m.get("title"), "description": m.get("description"),
                      "version": m.get("version"), "status": m.get("status", "active"),
                      "tags": m.get("tags", []), "runtime": m.get("runtime"),
                      "path": os.path.relpath(a["path"], ROOT).replace("\\", "/")})
    out = {"generated_from": "metadata.yaml", "count": len(items), "artifacts": items}
    dst = os.path.join(ROOT, "index.json")
    with open(dst, "w", encoding="utf-8", newline="\n") as f:
        json.dump(out, f, indent=2); f.write("\n")
    print(f"wrote {os.path.relpath(dst, ROOT)} ({len(items)} artifacts)")
    return [], []

def main():
    ap = argparse.ArgumentParser(prog="factory")
    ap.add_argument("cmd", choices=["validate", "links", "index"])
    ap.add_argument("--no-schema", action="store_true")
    args = ap.parse_args()
    arts = discover()
    if args.cmd == "validate":
        errors, warns = cmd_validate(arts, do_schema=not args.no_schema)
    elif args.cmd == "links":
        errors, warns = check_links(arts)
    else:
        errors, warns = cmd_index(arts)
    for w in warns:
        print(col("WARN ", "yellow") + w)
    for e in errors:
        print(col("FAIL ", "red") + e)
    n = len(arts)
    if errors:
        print(col(f"\n{args.cmd}: {len(errors)} error(s), {len(warns)} warning(s) over {n} artifacts", "red"))
        sys.exit(1)
    print(col(f"\n{args.cmd}: OK ({len(warns)} warning(s) over {n} artifacts)", "green"))
    sys.exit(0)

if __name__ == "__main__":
    main()
