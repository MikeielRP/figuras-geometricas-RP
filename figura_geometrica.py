"""Programa en python que calcula el área de las figuras geométricas"""

from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):
    """Clase abstracta que define la interfaz para calcular áreas."""
    def __init__(self, base=None, altura=None):
        self.base = base
        self.altura = altura

    @abstractmethod
    def calcular_area(self):
        """Método abstracto para calcular el área de una figura."""



class Rectangulo(FiguraGeometrica):
    """Clase para calcular el área de un rectángulo."""
    def __init__(self, base, altura):
        super().__init__(base, altura)

    def calcular_area(self):
        return self.base * self.altura



class Triangulo(FiguraGeometrica):
    """Clase para calcular el área de un triángulo."""
    def __init__(self, base, altura):
        super().__init__(base, altura)

    def calcular_area(self):
        return (self.base * self.altura) / 2



class Circulo(FiguraGeometrica):
    """Clase para calcular el área de un círculo."""
    def __init__(self, radio):
        super().__init__()  # Aunque no se usen base/altura, se llama igual
        self.radio = radio
        self.pi = 3.14159

    def calcular_area(self):
        return self.pi * (self.radio ** 2)



BASE_RECTANGULO = 10
ALTURA_RECTANGULO = 5
BASE_TRIANGULO = 7
ALTURA_TRIANGULO = 4
RADIO_CIRCULO = 3


if __name__ == "__main__":
    rectangulo = Rectangulo(BASE_RECTANGULO, ALTURA_RECTANGULO)
    triangulo = Triangulo(BASE_TRIANGULO, ALTURA_TRIANGULO)
    circulo = Circulo(RADIO_CIRCULO)

    print(f"El área del rectángulo es: {rectangulo.calcular_area()}")
    print(f"El área del triángulo es: {triangulo.calcular_area()}")
    print(f"El área del círculo es: {circulo.calcular_area()}")
