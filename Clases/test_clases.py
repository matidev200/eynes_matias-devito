import unittest
from clases import Circulo


class TestCirculo(unittest.TestCase):

    def setUp(self):
        self.circulo = Circulo(radio=23)
        self.circulo.radio = 1

    def test_class(self):

        self.assertTrue(isinstance(self.circulo, object), "The Circulo should be an object.")