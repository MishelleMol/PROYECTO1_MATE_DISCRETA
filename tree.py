from pathlib import Path

class DirTree:
    def __init__(self, root: Path):
        self.root = Path(root)

    def render(self, max_depth: int = 3) -> str:
        lines = ["."]
        def walk(path: Path, prefix: str, depth: int):
            if depth > max_depth:
                return
            try:
                entries = sorted(path.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))
            except PermissionError:
                entries = []
            total = len(entries)
            for i, entry in enumerate(entries):
                elbow = "└── " if i == total - 1 else "├── "
                lines.append(prefix + elbow + entry.name)
                if entry.is_dir():
                    extension = "    " if i == total - 1 else "│   "
                    walk(entry, prefix + extension, depth + 1)
        walk(self.root, "", 1)
        return "\n".join(lines)