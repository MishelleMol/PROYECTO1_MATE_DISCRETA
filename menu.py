
class Menu:
    def __init__(self):
        self.options = [
            "Mostrar estructura del árbol",
            "Analizar propiedades matemáticas",
            "Buscar archivos por criterio",
            "Cambiar directorio",
            "Salir",
        ]

    def show(self, title="FILE FINDER RECURSIVO - MATEMÁTICA DISCRETA"):
        print("=" * 50)
        print(title)
        print("=" * 50)
        for i, opt in enumerate(self.options, start=1):
            print(f"{i}. {opt}")
        return input("> Elige una opción (1-5): ").strip()
