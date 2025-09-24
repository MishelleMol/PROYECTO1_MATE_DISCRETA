from pathlib import Path

class Analyzer:
    def __init__(self, root: Path):
        self.root = Path(root)

    def properties(self):
        dirs = 0
        files = 0
        max_depth = 0
        total_children = 0
        counted_dirs = 0

        def walk(path: Path, depth: int):
            nonlocal dirs, files, max_depth, total_children, counted_dirs
            max_depth = max(max_depth, depth)
            try:
                entries = list(path.iterdir())
            except PermissionError:
                entries = []
            dirs += 1
            child_count = 0
            for e in entries:
                if e.is_dir():
                    child_count += 1
                elif e.is_file():
                    child_count += 1
                    files += 1
            total_children += child_count
            counted_dirs += 1
            for e in entries:
                if e.is_dir():
                    walk(e, depth + 1)

        walk(self.root, 0)
        nodes = dirs + files
        avg_branching = (total_children / counted_dirs) if counted_dirs else 0.0
        return {
            "nodes": nodes,
            "dirs": dirs,
            "files": files,
            "max_depth": max_depth,
            "avg_branching": avg_branching,
        }