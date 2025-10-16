import os #esto nos permite interactuar con el sistema operativo (operative system)

def clear(): #limpia la pantalla de la consola 
    try: #intenta ejecutar un comando dependiendo del OS
        os.system("cls" if os.name == "nt" else "clear") #os.name: tipo del sistema operativo 
    except Exception:   #Si algo falla, ignora el error para que el programa siga                                  #nt: Windows #os.system(...): ejecuta el comando en la terminal 
        pass

def pause(): #Esto pausa el programa esperando a que el usuario presione Enter
    try:
        input("\nPresiona Enter para continuar...") #detiene la ejecucion hasta que el usuario presione enter 
    except EOFError: #Si el programa corre en un contexto donde no hay entrada disponible y da error, ignora el error 
        pass
