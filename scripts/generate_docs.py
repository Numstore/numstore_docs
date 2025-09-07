#!/usr/bin/env python3
import sys, os, re, html
from pathlib import Path
from typing import List, Tuple, Set

# --- Config ---
ROOT         = Path("src/views/resources")
OUTLINE_FILE = ROOT / "docs_outline.txt"
AUTOGEN_DIR  = ROOT / "autogen"
INDEX_NAME   = "Index.vue"
ROOT_FILE    = AUTOGEN_DIR / "ROOT.vue"

# --- Utilities for headings/IDs/component names ---
TAG_RE = re.compile(r"<[^>]+>")  # strip inline HTML tags (e.g., <em>...</em>) for IDs and names

def strip_tags(s: str) -> str:
    return TAG_RE.sub("", s)

def slugify(title: str) -> str:
    """Make a safe unique anchor ID with prefix, stripping HTML tags first."""
    clean = strip_tags(title)
    # keep letters, digits, spaces, dashes; remove others
    clean = re.sub(r"[^A-Za-z0-9\- ]+", "", clean)
    return "rawdocs-" + re.sub(r"\s+", "-", clean.strip().lower())

def pascalize(parts: List[str]) -> str:
    """
    Create a stable, unique-ish component name from the full path parts.
    Example: ['Numstore','Getting Started','Linux'] -> 'NumstoreGettingStartedLinuxSection'
    """
    toks: List[str] = []
    for p in parts:
        base = strip_tags(p)
        base = re.sub(r"[^A-Za-z0-9]+", " ", base)
        toks.extend([w for w in base.split() if w])
    if not toks:
        toks = ["Section"]
    name = "".join(w[0].upper() + w[1:] for w in toks)
    if name and name[0].isdigit():
        name = "C" + name  # must not start with digit
    return name + "Section"

# --- Outline parsing (preserve order) ---
def parse_outline(filename: Path) -> List[Tuple[str, ...]]:
    """
    Parse outline into a list of path tuples, preserving order.
    Indentation: 2 spaces per level.
    """
    raw = filename.read_text(encoding="utf-8").splitlines()
    lines = [ln.rstrip("\n") for ln in raw if ln.strip()]

    unit = 2
    stack: List[str] = []
    nodes: List[Tuple[str, ...]] = []

    for ln in lines:
        lead = len(ln) - len(ln.lstrip(" "))
        level = lead // unit
        name = ln.strip()
        # keep original text (including inline tags) for headings; sanitize only for filesystem later
        stack = stack[:level] + [name]
        nodes.append(tuple(stack))
    return nodes

def all_parents_in_order(nodes: List[Tuple[str, ...]]) -> List[Tuple[str, ...]]:
    """Include every ancestor once, in first-appearance order."""
    seen: Set[Tuple[str, ...]] = set()
    out: List[Tuple[str, ...]] = []
    for p in nodes:
        for i in range(1, len(p) + 1):
            sub = p[:i]
            if sub not in seen:
                seen.add(sub)
                out.append(sub)
    return out

# --- Filesystem helpers ---
def fs_safe(s: str) -> str:
    """Make a safe folder name (don’t break paths); preserve readability."""
    # Keep letters, digits, spaces, dashes, underscores, and basic punctuation like ()[].
    t = strip_tags(s)
    t = t.replace("/", "／")
    t = re.sub(r"[<>:\"\\|?*]", "_", t)  # Windows-illegal chars
    t = t.strip()
    return t if t else "Section"

def ensure_autogen_tree(ordered_nodes: List[Tuple[str, ...]]) -> None:
    """
    For each node path: create AUTOGEN_DIR/<path>/ and Index.vue if missing (never overwrite).
    """
    AUTOGEN_DIR.mkdir(parents=True, exist_ok=True)
    for node in ordered_nodes:
        parts = [fs_safe(p) for p in node]
        d = AUTOGEN_DIR.joinpath(*parts)
        d.mkdir(parents=True, exist_ok=True)
        index_path = d / INDEX_NAME
        if not index_path.exists():
            index_path.write_text(
                f"""<!-- Autocreated placeholder for {'/'.join(parts)} -->
<script setup>
// add content for this section
</script>
<template>
  <div></div>
</template>
""",
                encoding="utf-8",
            )

def warn_on_unknown_files(ordered_nodes: List[Tuple[str, ...]]) -> None:
    """
    Warn if there are unexpected files in section folders (anything other than Index.vue),
    or directories not present in the outline (under AUTOGEN_DIR).
    """
    wanted_dirs = {AUTOGEN_DIR.joinpath(*[fs_safe(p) for p in n]) for n in ordered_nodes}

    # Walk existing
    if AUTOGEN_DIR.exists():
        for root, _, files in os.walk(AUTOGEN_DIR):
            root_path = Path(root)
            if root_path == AUTOGEN_DIR:
                continue
            # warn on directories that aren't in outline
            if root_path not in wanted_dirs and (root_path / INDEX_NAME).exists():
                print(f"Warning: directory exists but not in outline: {root_path}")

            # warn on unexpected files
            for f in files:
                if f != INDEX_NAME and not f.startswith("ROOT"):  # allow ROOT.vue
                    print(f"Warning: unexpected file in {root_path}: {f}")

# --- Render the top-level ROOT.vue ---
def render_toc(ordered_nodes: List[Tuple[str, ...]]) -> str:
    out: List[str] = []
    stack_depth = 0

    def open_ul():
        out.append('<ul class="list-disc ml-6">')

    def close_ul():
        out.append("</ul>")

    for node in ordered_nodes:
        depth = len(node)
        title = node[-1]
        while stack_depth < depth:
            open_ul(); stack_depth += 1
        while stack_depth > depth:
            close_ul(); stack_depth -= 1
        out.append(
            f'<li class="mb-1"><a class="text-blue-600 hover:underline" href="#{slugify(title)}">'
            f'{html.escape(strip_tags(title))}</a></li>'
        )
    while stack_depth > 0:
        close_ul(); stack_depth -= 1
    return "\n".join(out)

def render_body(ordered_nodes: List[Tuple[str, ...]]) -> Tuple[str, List[Tuple[str, str]]]:
    """
    Return (template_html, imports) where imports is [(component_name, import_path)].
    For each node: header + component.
    """
    tpl: List[str] = []
    imports: List[Tuple[str, str]] = []

    for node in ordered_nodes:
        depth = len(node)
        tag = f"h{min(depth, 6)}"
        title = node[-1]                     # keep inline tags in visible text
        id_attr = slugify(title)             # clean IDs
        comp_name = pascalize(list(node))    # unique component name from path

        # Import path relative to ROOT.vue (AUTOGEN_DIR/ROOT.vue)
        rel_parts = [fs_safe(p) for p in node]
        import_path = "./" + "/".join(rel_parts) + f"/{INDEX_NAME}"

        imports.append((comp_name, import_path))

        # Section block
        tpl.append(f"<!-- From: {'/'.join([strip_tags(p) for p in node])} -->")
        tpl.append(f'<{tag} id="{id_attr}">{title}</{tag}>')
        tpl.append(f"<{comp_name} />")
        tbl.append("<br>")
        tpl.append("")  # spacer

    return "\n".join(tpl), imports

def build_root_vue(ordered_nodes: List[Tuple[str, ...]]) -> str:
    cmdline = " ".join(sys.argv)

    body_html, imports = render_body(ordered_nodes)
    import_lines = []
    # Deduplicate imports in case of weird duplicates (shouldn't happen with our naming, but safe)
    seen = set()
    for name, path in imports:
        key = (name, path)
        if key in seen: 
            continue
        seen.add(key)
        import_lines.append(f'import {name} from "{path}";')

    toc_html = render_toc(ordered_nodes)

    return f"""<!-- Autogenerated with command: {cmdline} -->
<script setup lang="ts">
{os.linesep.join(import_lines)}
</script>

<template>
  <div class="prose">
    <h1>Table of Contents</h1>
{toc_html}

{body_html}
  </div>
</template>

<style scoped>
@reference "tailwindcss";
h1 {{
  @apply text-4xl font-bold leading-tight;
}}

h2 {{
  @apply text-3xl font-bold leading-tight;
}}

h3 {{
  @apply text-2xl font-bold leading-tight;
}}

h4 {{
  @apply text-xl  font-bold leading-tight;
}}
</style>
"""

# --- Main ---
def main():
    if not OUTLINE_FILE.exists():
        print(f"outline not found: {OUTLINE_FILE}", file=sys.stderr)
        sys.exit(1)

    # Parse outline and derive ordered node list including all parents
    raw_nodes = parse_outline(OUTLINE_FILE)
    ordered_nodes = all_parents_in_order(raw_nodes)

    # Ensure AUTOGEN tree and placeholder Index.vue files
    ensure_autogen_tree(ordered_nodes)

    # Warn about extras
    warn_on_unknown_files(ordered_nodes)

    # Build ROOT.vue content and (re)write it (this one file is safe to overwrite)
    AUTOGEN_DIR.mkdir(parents=True, exist_ok=True)
    root_content = build_root_vue(ordered_nodes)
    ROOT_FILE.write_text(root_content, encoding="utf-8")
    print(f"[gendocs] wrote {ROOT_FILE}")

if __name__ == "__main__":
    main()

