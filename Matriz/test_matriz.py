"""
Crear una matriz de 5x5 randomizada con números enteros, encontrar secuencia de 4
números consecutivos horizontal o vertical y si se encuentra mostrar la posición inicial y
final.
"""
import unittest
import numpy as np
from matriz import generar_arrays


class TestArray(unittest.TestCase):

    def setUp(self) :
        self.arrays = generar_arrays()

    def test_arrays(self):

        self.assertTrue(isinstance(self.arrays, dict), "La función debe retornar un diccionario")

        self.assertTrue(isinstance(self.arrays["array_horizontal"], np.ndarray), "Los diccionarios deben contener arrays")

        self.assertEqual(self.arrays["array_horizontal"].shape == (5,5),self.arrays["array_vertical"].shape == (5,5), "Las dimensiones de los array deben de ser de 5x5" )

        self.assertTrue((self.arrays["array_horizontal"] == self.arrays["array_horizontal"]).all(), "Los valores del array horizontal deben ser distintos")

        self.assertTrue((self.arrays["array_vertical"] == self.arrays["array_vertical"]).all(), "Los valores del array vertical deben ser distintos")