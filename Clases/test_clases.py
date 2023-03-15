import unittest
from clases import Circulo


class TestCirculo(unittest.TestCase):

    def setUp(self):
        self.circulo = Circulo(radio=23)
        self.circulo.radio = 1

    def test_class(self):

        self.assertTrue(isinstance(self.circulo, object), "The Circulo should be an object.")
        
        self.assertTrue(hasattr(self.circulo, "radio"), "The object should contains the radio method")

        self.assertTrue(hasattr(self.circulo, "perimetro"), "La clase debe contener un método perímetro")

        self.assertTrue(hasattr(self.circulo, "area"), "La clase debe contener un  método área")

        self.assertTrue(hasattr(self.circulo, "multiplicar_radio"), "La clase debe tener un método de multiplicación para el radio")