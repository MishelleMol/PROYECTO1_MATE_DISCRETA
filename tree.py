import os #Para trabajar con archivos y rutas 

class DirTree: #Esta clase sirve para dibujar un árbol de carpetas y archivos.
    def __init__(self, root): #define el punto de inicio del árbol (raíz del directorio)
        self.root = os.path.abspath(root) #root (raíz) es la carpeta 
                                          #os.path.abspath(root) convierte la ruta a absoluta (segura y clara)

    def render(self, max_depth=3): #Genera el texto del árbol en forma de string
                                   #max_depth: limuta la profundidad de expliración (3 niveles)
        lines = ["."] #Es una lista que va a ir guardando línea por línea del árbol
        # DFS manual para poder controlar prefijos bonitos
        def walk(path, prefix, depth): #Función interna (recursiva) que explora carpetas y archivos
                                       #Esta función explora la carpeta llamada path.
                                       #prefix lo utilizamos para los símbolos, osea para dibujar un bonito árbol
                                       #depth es la profundidad actual. Si es mayor a 3 se detiene. 
            if depth > max_depth:
                return
            try:
                with os.scandir(path) as it: #os.scandir lista archivos y subcarpetas 
                    entries = [e for e in it]
            except PermissionError: #Si no hay permiso para entrar a una carpeta, se evita el error (esto se llama error handling)
                entries = []

            # Primero carpetas, luego archivos; orden alfabético
            entries.sort(key=lambda e: (not e.is_dir(), e.name.lower()))
            total = len(entries)

            for i, entry in enumerate(entries):
                elbow = "└── " if i == total - 1 else "├── "
                lines.append(prefix + elbow + entry.name) #Recorre cada archivo. Así es como creamos las ramas del árbol
                if entry.is_dir(): #Si es una carpeta va a entrar de forma recursiva 
                    extension = "    " if i == total - 1 else "│   "
                    walk(os.path.join(path, entry.name), prefix + extension, depth + 1) 

        walk(self.root, "", 1) #Esto llama a walk empezando desde la raíz 
        return "\n".join(lines) #Une todas las líneas del árbol en un solo string
