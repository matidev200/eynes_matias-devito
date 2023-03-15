"""
Hacer una función que genere una lista de diccionarios que contengan id y edad, donde
edad sea un número aleatorio entre 1 y 100 y la longitud de la lista sea de 10
elementos. retornar la lista.
Hacer otra función que reciba lo generado en la primer función y ordenarlo de mayor a
menor. Printear el id de la persona más joven y más vieja. Devolver la lista ordenada.
"""

import numpy as np

def generador_diccionarios():
    diccionarios = [{"id": i, "edad": np.random.randint(1, 100)} for i in range(10)]

    return diccionarios

def ordenador_diccionarios(diccionarios):
    # Ordenamos la lista con la función sorted aplicando lambda para tratar con cada key edad del diccionario.
    lista_ordenada = sorted(diccionarios, key=lambda item: item['edad'], reverse=True)

    # Hacemos uso del print para mostrar la edad más alta y la más baja.
    print(f'Persona más vieja: {lista_ordenada[0]["id"]}, Persona más joven: {lista_ordenada[-1]["id"]}')

    return lista_ordenada