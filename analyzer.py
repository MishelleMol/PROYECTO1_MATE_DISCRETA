import os #para recorrer carpetas y manejar rutas

class Analyzer:

    def __init__(self, root): #Guarda la carpeta raíz (root) desde donde se empieza el análisis
        self.root = os.path.abspath(root) #abspath normaliza rutas 

    def properties(self): #esta función realiza todo el análisis del árbol
        dirs = 0 #contador de carpetas
        files = 0 #contador de archivos 
        max_depth = 0 #máxima profundidad detectada 
        total_children = 0 #total de hijos por carpeta (archivos + carpetas)
        counted_dirs = 0 #total de carpetas inspeccionadas

        # Recorremos todo el árbol con os.walk
        for dirpath, dirnames, filenames in os.walk(self.root, topdown=True):
            # profundidad: cuántos separadores adicionales tiene respecto a la raíz
            rel = os.path.relpath(dirpath, self.root) #os.path.relpath elimina redundancias. 
            depth = 0 if rel == "." else rel.count(os.sep) + 0 #calcula cuántos niveles hemos bajado desdde la raíz
            if depth > max_depth:
                max_depth = depth

            dirs += 1  # contamos este directorio #suma 1 por cada directorio encontrado 
            files += len(filenames) #suma archivos dentro de él

            child_count = len(dirnames) + len(filenames) #cuenta cuántos hijos tiene cada carpeta
            total_children += child_count                #nos sirve para calcular el promedio
            counted_dirs += 1

        nodes = dirs + files #nodes es el total de nodos
        avg_branching = (total_children / counted_dirs) if counted_dirs else 0.0 #avg_branching = promedio de hijos por carpeta. 

        return {
            "nodes": nodes,
            "dirs": dirs,
            "files": files,
            "max_depth": max_depth,
            "avg_branching": avg_branching,
        }
