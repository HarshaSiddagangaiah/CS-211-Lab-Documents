"""
Fractions
Harsha, 2023-01-17, CS 211
"""

class Fraction:
    def __init__(self, num : int, den: int):
        if num < 0 or den <= 0:
            raise ValueError("Denominator cannot be 0 and Numerator cannot be negative")

        self.num = num
        self.den = den
        self.simplify()

    def __str__ (self):
        return f"{self.num}/{self.den}"

    def __repr__ (self):
        return f'Fraction({self.num},{self.den})'

    def __mul__(self, other: "Fraction") -> "Fraction":
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __add__(self, other: "Fraction"):
        new_num = (self.num * other.den) + (other.num * self.den)
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def simplify(self):
        my_gcd = gcd(self.num, self.den)
        if my_gcd > 1:
            self.num //= my_gcd
            self.den //= my_gcd


def gcd(a: int, b: int) -> int:
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a
