"""
Este script realiza operaciones básicas matemáticas y calcula el promedio de un conjunto de números.
"""

class OperacionesBasicas:
    """
    Clase para realizar operaciones básicas matemáticas.
    """
    def __init__(self):
        self.resultado = 0

    def sumar(self, a, b):
        """
        Suma dos números.
        """
        self.resultado = a + b

    def restar(self, a, b):
        """
        Resta dos números.
        """
        self.resultado = a - b

    def obtener_resultado(self):
        """
        Retorna el resultado de la operación.
        """
        return self.resultado


class CalculadoraPromedio:
    """
    Clase para calcular el promedio de un conjunto de números.
    """
    def __init__(self, valores):
        self.valores = valores

    def calcular_promedio(self):
        """
        Calcula y retorna el promedio de los valores proporcionados.
        """
        suma = sum(self.valores)
        promedio_local = suma / len(self.valores)
        return promedio_local

    def obtener_cantidad_valores(self):
        """
        Retorna la cantidad de valores utilizados para calcular el promedio.
        """
        return len(self.valores)

# Variables globales
NUMEROS = [1, 2, 3, 4, 5]
NUM1 = 10
NUM2 = 20

# Ejecución principal
if __name__ == "__main__":
    # Usar la clase OperacionesBasicas
    operaciones = OperacionesBasicas()
    operaciones.sumar(NUM1, NUM2)
    print(f"El resultado de la suma es: {operaciones.obtener_resultado()}")

    operaciones.restar(NUM1, NUM2)
    print(f"El resultado de la resta es: {operaciones.obtener_resultado()}")

    # Usar la clase CalculadoraPromedio
    calculadora_promedio = CalculadoraPromedio(NUMEROS)
    promedio = calculadora_promedio.calcular_promedio()
    print(f"El promedio de los números es: {promedio}")
