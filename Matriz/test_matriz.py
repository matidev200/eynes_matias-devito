"""
Crear una matriz de 5x5 randomizada con números enteros, encontrar secuencia de 4
números consecutivos horizontal o vertical y si se encuentra mostrar la posición inicial y
final.
"""
import unittest
import numpy as np
from matriz import generar_arrays, buscar_indices

class TestArray(unittest.TestCase):

    def setUp(self) :
        self.arrays = generar_arrays()

    def test_arrays(self):

        self.assertTrue(isinstance(self.arrays, dict), "La función debe retornar un diccionario")

        self.assertTrue(isinstance(self.arrays["array_horizontal"], np.ndarray), "Los diccionarios deben contener arrays")

        self.assertEqual(self.arrays["array_horizontal"].shape == (5,5),self.arrays["array_vertical"].shape == (5,5), "Las dimensiones de los array deben de ser de 5x5" )

        self.assertTrue((self.arrays["array_horizontal"] == self.arrays["array_horizontal"]).all(), "Los valores del array horizontal deben ser distintos")

        self.assertTrue((self.arrays["array_vertical"] == self.arrays["array_vertical"]).all(), "Los valores del array vertical deben ser distintos")

class TestSecuencia(unittest.TestCase):

    def setUp(self) :
        self.array_secuencia_0_3 = np.array([0,1,2,3,4])
        self.array_secuencia_1_4 = np.array([2,1,2,3,4])


    def test_buscar_indices(self):
        
        self.assertTrue(isinstance(buscar_indices(self.array_secuencia_0_3), dict), "La función buscar indices debe retornar un diccionario" )

        self.assertEqual(buscar_indices(self.array_secuencia_0_3), {'primera_posición':0, 'ultima_posición': 3}, "La primera posición debe ser el 0 y la ultima el 3 en este caso")

        self.assertEqual(buscar_indices(self.array_secuencia_1_4), {'primera_posición':1, 'ultima_posición': 4}, "La primera posición debe ser el 1 y la ultima el 4 en este caso")