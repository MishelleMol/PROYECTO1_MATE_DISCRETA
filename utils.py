import os

def clear():
    # Limpia pantalla en Windows / Unix. Ignora errores (por compatibilidad).
    try:
        os.system("cls" if os.name == "nt" else "clear")
    except Exception:
        pass

def pause():
    try:
        input("\nPresiona Enter para continuar...")
    except EOFError:
        pass