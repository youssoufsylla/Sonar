"""
calculator.py - Un exemple simple pour le scan SonarQube
"""
import math
import sys

class Calculator:
    """Une classe calculatrice basique avec des opérations mathématiques"""

    def __init__(self):
        self.last_result = None

    def add(self, a, b):
        """Additionne deux nombres"""
        self.last_result = a + b
        return self.last_result

    def subtract(self, a, b):
        """Soustrait b de a"""
        self.last_result = a - b
        return self.last_result

    def divide(self, a, b):
        """Divise a par b"""
        if b == 0:  # Détection de division par zéro
            raise ValueError("Cannot divide by zero!")
        self.last_result = a / b
        return self.last_result

    def square_root(self, x):
        """Calcule la racine carrée"""
        if x < 0:
            print("Warning: Imaginary number!", file=sys.stderr)
        self.last_result = math.sqrt(x)
        return self.last_result

def main():
    """Fon