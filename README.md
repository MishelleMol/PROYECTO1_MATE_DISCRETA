# PROYECTO1_MATE_DISCRETA
Este es un repositorio para trabajar el primer proyecto de programación para matemática discreta. 


# File Finder Recursivo — Matemática Discreta - Dhidel Osorio & Mishelle Molina

## Descripción general

Este proyecto implementa una aplicación de que:  **explora, analiza y busca archivos dentro de un sistema de directorios**, aplicando principios de **recursión** y **estructuras de árboles**.  
(El código que hicimos solo es utilizable en Windows ;] )

Su objetivo es mostrar cómo la teoría de árboles y la recursión pueden aplicarse en la práctica para recorrer sistemas jerárquicos (como carpetas en un disco).

## Funcionamiento general

Al ejecutar `main.py`, se inicializa la clase `App`, que despliega un menú interactivo con cinco opciones principales:

1. **Mostrar estructura del árbol**  
   Genera una representación visual de los subdirectorios hasta una profundidad elegida (usando `DirTree`).

2. **Analizar propiedades matemáticas**  
   Usa `Analyzer` para calcular propiedades del árbol de directorios:
   - número total de nodos  
   - cantidad de directorios  
   - cantidad de archivos  
   - profundidad máxima  
   - factor de ramificación promedio

3. **Buscar archivos por criterio**  
   Permite aplicar filtros personalizados, como:
   - archivos con tamaño par  
   - archivos con todas las vocales en el nombre  
   - archivos menores a 1 KB  
   - archivos con una extensión específica  

4. **Cambiar directorio actual**  
   Permite navegar hacia un nuevo directorio raíz.

5. **Salir del programa**

La interfaz se mantiene limpia y clara gracias a las funciones auxiliares `clear()` y `pause()`.

## Estructura de archivos

| Orden | Archivo | Rol dentro del sistema |
|:--:|:--|:--|
| 1 | `utils.py` | Utilidades para consola: limpiar pantalla y pausar. |
| 2 | `menu.py` | Clase `Menu`, muestra las opciones del sistema. |
| 3 | `tree.py` | Clase `DirTree`, imprime el árbol de directorios. |
| 4 | `analyzer.py` | Clase `Analyzer`, calcula propiedades matemáticas del árbol. |
| 5 | `search.py` | Clase `FileSearcher` y predicados de búsqueda. |
| 6 | `app.py` | Controlador principal: integra todas las funcionalidades. |
| 7 | `main.py` | Punto de entrada: ejecuta la aplicación (`App().run()`). |


## Decisiones de diseño

- **Modularidad total:**  
  Cada archivo tiene una única responsabilidad. Esto facilita la mantenibilidad y la lectura del código.

- **Recursión controlada:**  
  Se utiliza en los recorridos de directorios (`DirTree`, `Analyzer`, `FileSearcher`), simulando recorridos de árboles en preorden.

- **Funciones de orden superior:**  
  En `search.py`, los criterios de búsqueda se implementan como **predicados** (funciones que retornan `True`/`False`), incluso con **cierres (closures)** para criterios personalizados.

- **Manejo seguro de errores:**  
  El código evita fallos por permisos restringidos mediante `try/except PermissionError`.

- **Interfaz sencilla y universal:**  
  Se elige una interfaz de consola multiplataforma (Windows/Linux) para centrarse en la lógica matemática y recursiva, no en la interfaz gráfica.

## Correctitud (inducción)

La correctitud de las funciones recursivas puede demostrarse mediante inducción estructural sobre el árbol de directorios:

1. **Caso base:**  
   Si el directorio no tiene subdirectorios, la función procesa solo sus archivos y termina correctamente.

2. **Hipótesis inductiva:**  
   Suponemos que la función funciona correctamente para todos los subdirectorios de profundidad `k`.

3. **Paso inductivo:**  
   Para un directorio de profundidad `k + 1`, se recorren sus subdirectorios aplicando la misma función recursiva (`walk()` o `render()`).  
   Dado que cada llamada recursiva procesa un subárbol finito, la función termina correctamente y cubre todo el árbol.

Por tanto, el recorrido recursivo es **totalmente correcto** y **termina para árboles finitos**, lo cual se garantiza en un sistema de archivos real.