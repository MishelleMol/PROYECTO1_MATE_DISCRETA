import os
from menu import Menu
from tree import DirTree
from analyzer import Analyzer
from search import FileSearcher, criteria_menu
from utils import clear, pause

class App:

    def __init__(self):
        self.cwd = os.getcwd() #estado: nuestro directorio actual
        self.menu = Menu()     #dependencia: menú interactivo

    def run(self): #bucle infinito que se detiene hasta que seleccionan la opción 5
        while True:
            clear()
            print(f"Directorio actual: {self.cwd}\n")
            choice = self._ask_menu_choice()

            if choice == 1:
                self.option_show_tree()
            elif choice == 2:
                self.option_analyze()
            elif choice == 3:
                self.option_search()
            elif choice == 4:
                self.option_change_dir()
            elif choice == 5:
                print("¡Hasta luego!")
                break

    
    def option_show_tree(self):
        print("\n ESTRUCTURA DEL ÁRBOL")
        depth = self._ask_int("Profundidad máxima a mostrar (default=3): ", default=3, min_value=1) #Pide profundidad y cómo sabemos el máximo es 3
        print()
        tree = DirTree(self.cwd) #DirTree  tiene raíz=cwd y lo renderiza. 
        print(tree.render(max_depth=depth))
        pause() #Esto causa una pausa para que el usuario lo lea 

    def option_analyze(self): 
        print("\n ANÁLISIS DE PROPIEDADES")
        props = Analyzer(self.cwd).properties()
        print(f"- Nodos totales: {props['nodes']}")
        print(f"- Directorios:   {props['dirs']}")
        print(f"- Archivos:      {props['files']}")
        print(f"- Profundidad máx.: {props['max_depth']}")
        print(f"- Factor de ramificación promedio: {props['avg_branching']:.2f}") #avg_branching se imprime con 2 decimales 
        pause()

    def option_search(self):
        predicate, description = criteria_menu() #devuelve un predicado (función filtro) y un texto descriptivo.
        if predicate is None:
            return
        print(f"\nBuscando archivos: {description} ...\n")
        searcher = FileSearcher(self.cwd)
        results = list(searcher.find(predicate)) 
        if not results:
            print("No se encontraron coincidencias.")
        else:
            for p in results:
                rel = os.path.relpath(p, self.cwd)
                try:
                    size = os.path.getsize(p)
                except OSError:
                    size = "?"
                print(f"• {rel}  ({size} bytes)")
            print(f"\nSe encontraron {len(results)} archivo(s).")
        pause()

    def option_change_dir(self):
        raw = input("\nIngrese ruta de directorio (relativa o absoluta): ").strip()
        if not raw:
            return
        target = raw
        if not os.path.isabs(target):
            target = os.path.abspath(os.path.join(self.cwd, target))#acepta rutas relativas (desde cwd) o absolutas
        if os.path.isdir(target):
            self.cwd = target
            print(f"Directorio cambiado a: {self.cwd}") #esto válida que exista y sea directorio antes de actualizar self.cwd
        else:
            print("Ruta inválida o no es un directorio.")
        pause()


    def _ask_menu_choice(self):
        while True:
            choice_str = self.menu.show()
            try:
                choice = int(choice_str)
                if 1 <= choice <= 5:
                    return choice
                print("Opción fuera de rango (1-5). Intenta de nuevo.")
            except ValueError:
                print("Entrada inválida. Escribe un número del 1 al 5.")

    def _ask_int(self, prompt, default=None, min_value=None, max_value=None):
        while True:
            raw = input(prompt).strip()
            if raw == "" and default is not None:
                return default
            try:
                val = int(raw)
                if min_value is not None and val < min_value:
                    print(f"Debe ser ≥ {min_value}.")
                    continue
                if max_value is not None and val > max_value:
                    print(f"Debe ser ≤ {max_value}.")
                    continue
                return val
            except ValueError:
                print("Ingresa un entero válido.")
