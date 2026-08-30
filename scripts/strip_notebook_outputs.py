#!/usr/bin/env python3
"""Clear Jupyter outputs and execution counts from notebooks (source stays)."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def strip_notebook(path: Path) -> bool:
    nb = json.loads(path.read_text())
    changed = False
    for cell in nb.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        if cell.get("outputs"):
            cell["outputs"] = []
            changed = True
        if cell.get("execution_count") is not None:
            cell["execution_count"] = None
            changed = True
        metadata = cell.get("metadata") or {}
        for key in ("execution", "collapsed", "scrolled"):
            if key in metadata:
                del metadata[key]
                changed = True
        cell["metadata"] = metadata
    widgets = (nb.get("metadata") or {}).get("widgets")
    if widgets:
        del nb["metadata"]["widgets"]
        changed = True
    if changed:
        path.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + "\n")
    return changed


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    paths = [Path(p) for p in sys.argv[1:]]
    if not paths:
        paths = sorted(root.rglob("*.ipynb"))
        paths = [p for p in paths if ".ipynb_checkpoints" not in p.parts]
    stripped = 0
    for path in paths:
        if strip_notebook(path):
            print(f"stripped {path}")
            stripped += 1
        else:
            print(f"clean    {path}")
    print(f"{stripped} notebook(s) updated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
