
from math import gcd

class Rational:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        g = gcd(numerator, denominator)
        self.numerator = numerator // g
        self.denominator = denominator // g

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def getNumerator(self):
        return self.numerator

    def getDenominator(self):
        return self.denominator

    def __add__(self, other):
        return Rational(self.numerator * other.denominator + other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __sub__(self, other):
        return Rational(self.numerator * other.denominator - other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __mul__(self, other):
        return Rational(self.numerator * other.numerator, self.denominator * other.denominator)

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __gt__(self, other):
        return self.numerator * other.denominator > other.numerator * self.denominator
r1 = Rational(1, 2)
r2 = Rational(3, 4)
print("R1:", r1)
print("R2:", r2)
print("R1 + R2:", r1 + r2)
print("R1 - R2:", r1 - r2)
print("R1 * R2:", r1 * r2)
print("R1 == R2:", r1 == r2)
print("R1 < R2:", r1 < r2)
print("R1 > R2:", r1 > r2)
R1: 1/2
R2: 3/4
R1 + R2: 5/4
R1 - R2: -1/4
R1 * R2: 3/8
R1 == R2: False
R1 < R2: True
R1 > R2: False
r1 = Rational(1, 2)
r2 = Rational(3, 4)
print("R1:", r1)
print("R2:", r2)
print(r1.__add__(r2))
print(r1.__sub__(r2))
print(r1.__mul__(r2))
print(r1.__eq__(r2))
print(r1.__lt__(r2))
print(r1.__gt__(r2))
R1: 1/2
R2: 3/4
5/4
-1/4
3/8
False
True
False
