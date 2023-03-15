"""
Crear una matriz de 5x5 randomizada con números enteros, encontrar secuencia de 4
números consecutivos horizontal o vertical y si se encuentra mostrar la posición inicial y
final.
"""

import numpy as np

def generar_arrays():
    
    # Definimos nuestro array de 5x5 con numeros random enteros del 1 al 10
    array_horizontal = np.random.randint(1, 5, size=(5,5))

    # Definimos el array vertical con la función transpose de numpy para que todos los arrays horizontales se coloquen verticalmente.
    array_vertical = np.transpose(array_horizontal)

    return {"array_horizontal": array_horizontal, "array_vertical" : array_vertical}