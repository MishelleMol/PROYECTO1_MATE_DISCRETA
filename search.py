from pathlib import Path


def size_even(file: Path) -> bool:
    return file.is_file() and file.stat().st_size % 2 == 0

def has_all_vowels(file: Path) -> bool:
    if not file.is_file():
        return False
    name = file.stem.lower()
    return all(v in name for v in "aeiou")

def very_small(file: Path) -> bool:
    return file.is_file() and file.stat().st_size < 1024 

def by_extension(ext: str):
    ext = ext.lower().lstrip(".")
    def _pred(file: Path) -> bool:
        return file.is_file() and file.suffix.lower().lstrip(".") == ext
    return _pred


class FileSearcher:
    def __init__(self, root: Path):
        self.root = Path(root)

    def find(self, predicate):
        def walk(path: Path):
            try:
                entries = list(path.iterdir())
            except PermissionError:
                entries = []
            for e in entries:
                if e.is_file() and predicate(e):
                    yield e
                if e.is_dir():
                    yield from walk(e)
        return walk(self.root)


def criteria_menu():
    print("\nCRITERIOS DE BÚSQUEDA")
    print(" 1. Archivos con tamaño par (bytes)")
    print(" 2. Archivos con todas las vocales (en el nombre)")
    print(" 3. Archivos muy pequeños (< 1 KB)")
    print(" 4. Archivos por extensión personalizada")
    print(" 5. Volver al menú principal")

    while True:
        raw = input("\nElige una opción (1-5): ").strip()
        try:
            opt = int(raw)
        except ValueError:
            print(" Ingresa un número del 1 al 5.")
            continue

        if opt == 1:
            return size_even, "tamaño par"
        if opt == 2:
            return has_all_vowels, "nombre con todas las vocales"
        if opt == 3:
            return very_small, "muy pequeños (<1 KB)"
        if opt == 4:
            ext = input("Ingrese la extensión (ej. py, txt, pdf): ").strip()
            if not ext:
                print(" Extensión vacía, intenta de nuevo.")
                continue
            return by_extension(ext), f"extensión .{ext.lstrip('.')}"
        if opt == 5:
            return None, None

        print(" Opción fuera de rango.")