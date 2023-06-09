"""
Escribir una clase en python llamada círculo que contenga un radio, con un método que
devuelva el área y otro que devuelva el perímetro del círculo.
Si se instancia la clase con radio <= 0 mostrar una excepción indicando un error amigable al
usuario e impidiendo la instanciación.
Si printeamos el objeto creado debe mostrarse una representación amigable.
El objeto debe tener su atributo radio modificable, si se le intenta setear un valor <= 0
mostrar un error y no permitir modificación.
Permitir la multiplicación del circulo: Circulo * n debe devolver un nuevo objeto con el radio
multiplicado por n. No permitir la multiplicación por números <= 0
"""
import math

class Circulo:

    def __init__(self, radio):
        # Inicializamos la clase con una variable rádio protegida (la usaremos dentro de nuestro clase Círculo.)
        self._radio = radio

    # Definimos nuestros métodos getter and setter.
    @property
    def radio(self):
        return self._radio
    
    @radio.setter
    def radio(self, radio):
        if radio <= 0:
            raise ValueError("No puedes ingresar un radio menor o igual a cero.")
        
        self._radio = radio

    # Definimos nuestras funciones de la clase Círculo respetando las condiciones requeridas en la prueba.
    def area(self):
        return math.pi * self._radio ** 2

    def perimetro(self):
        return 2 * math.pi * self._radio
    
    def multiplicar_radio(self, factor):
        if factor <= 0:
            raise ValueError("No puedes multiplicar el radio por numeros menores o iguales a 0")      
        return Circulo(self._radio * factor)
    
    # Definimos nuestros métodos representativos.
    def __str__(self):
        return f"Este es tu objecto Circulo creado: Radio {self._radio}, Area: {self.area()}, Perimetro: {self.perimetro()} "

    def __repr__(self):
        return f"Circulo(radio={self._radio})"
        