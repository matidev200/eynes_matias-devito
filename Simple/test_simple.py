import unittest
from simple import generador_diccionarios, ordenador_diccionarios


class TestDiccionarios(unittest.TestCase):

    def setUp(self) -> None:
        self.generador = generador_diccionarios()
        self.ordenador = ordenador_diccionarios(self.generador)

    
    def test_generador(self):
        self.assertTrue(isinstance(self.generador, list), "La función debe retornar una lista")

        self.assertEqual(len(self.generador), 10, "La longitud de la lista debe de ser de 10 elementos")

        for i in range(10):
            self.assertTrue(isinstance(self.generador[i], dict), "La lista debe contener diccionarios")

            self.assertTrue("id" in self.generador[i], "La lista debe contener diccionarios con id")

            self.assertTrue("edad" in self.generador[i], "La lista debe contener diccionarios con edad")

            self.assertTrue(self.generador[i]["edad"] in range(1,100), "Las edades deben estar entre 1 y 100")