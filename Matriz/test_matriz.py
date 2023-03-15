"""
Crear una matriz de 5x5 randomizada con números enteros, encontrar secuencia de 4
números consecutivos horizontal o vertical y si se encuentra mostrar la posición inicial y
final.
"""
import unittest
from matriz import generar_arrays


class TestArray(unittest.TestCase):

    def setUp(self) :
        self.arrays = generar_arrays()

    def test_arrays(self):

        self.assertTrue(isinstance(self.arrays, dict), "La función debe retornar un diccionario")