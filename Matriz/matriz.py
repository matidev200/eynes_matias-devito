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

def buscar_indices(array):
    secuencia = 0

    # Definimos el diccionario de posiciones
    posicion = {
        "primera_posición": 0,
        "ultima_posición": 0
    }

    # Iteramos en el rango del array
    for i in range(len(array)):
        
        # Creamos una variable secuencia la cual la vamos a ir incrementando a medida que se hallen secuencias.
        if i == 0:
            secuencia += 1
            continue
        
        # Nuestra operación aritmetica es la siguiente n = n[n - 1] + 1 (nuestro elemento actual tiene que ser igual al anterior más uno.)
        if array[i] == array[i - 1] + 1:
            secuencia += 1

            # Si obtenemos una sumatoria de cuatro secuencias definimos la posición actual del iterador como posición final.
            if secuencia == 4:
                posicion["ultima_posición"] = i
                break
        else:
            # Caso contrario si tenemos secuencias diferentes de cuatro números resetearemos el contador a uno.
            if secuencia >= 2:
                break
            else:
                secuencia = 1
                posicion["primera_posición"] = i
    
    # Finalmente si la posición final es diferente de 0, significa que obtuvimos una secuencia.
    if posicion["ultima_posición"] != 0:
        return posicion