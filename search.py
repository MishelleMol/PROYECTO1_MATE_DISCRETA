import os



def size_even(file_path): #esta función de primer verifica  si file_path es un archivo. 
    return os.path.isfile(file_path) and (os.path.getsize(file_path) % 2 == 0)#Si es archivo revisa si su tamaño en bytes es par.

def has_all_vowels(file_path): 
    if not os.path.isfile(file_path):#revisa si es un archivo
        return False
    name, _ = os.path.splitext(os.path.basename(file_path)) #se queda solo con el nombre del archivo, sin extensión
    name = name.lower()
    for v in "aeiou": #Verifica si ese nombre tiene todas las vocales 
        if v not in name:
            return False #Si le falta alguna vocal devuelve False
    return True

def very_small(file_path): #Esta función devuelve True si el archivo pena menos de 1024 bytes (1KB)
    return os.path.isfile(file_path) and os.path.getsize(file_path) < 1024

def by_extension(ext): #Esta es una función que devuelve otra función.
    ext = ext.lower().lstrip(".")
    def _pred(file_path):
        return os.path.isfile(file_path) and os.path.splitext(file_path)[1].lower().lstrip(".") == ext
    return _pred

class FileSearcher:

    def __init__(self, root):
        self.root = os.path.abspath(root)

    def find(self, predicate): #predicate es una función que define el criterio de búsqueda
        for dirpath, dirnames, filenames in os.walk(self.root): #os.walk es para explorar todas las carpetas y subcarpetas desde la raíz (root)
            for fname in filenames:
                full = os.path.join(dirpath, fname)
                if predicate(full):
                    yield full #yield genera resultados uno por uno 

#Menú de criterios 

def criteria_menu(): #Esta función muestra opciones al usuario
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
