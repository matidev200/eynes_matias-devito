import unittest
from simple import generador_diccionarios, ordenador_diccionarios


class TestDiccionarios(unittest.TestCase):

    def setUp(self) -> None:
        self.generador = generador_diccionarios()
        self.ordenador = ordenador_diccionarios(self.generador)

    
    def test_generador(self):
        self.assertTrue(isinstance(self.generador, list), "La función debe retornar una lista")

        self.assertEqual(len(self.generador), 10, "La longitud de la lista debe de ser de 10 elementos")