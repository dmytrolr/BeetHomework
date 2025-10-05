from math import gcd


class Fraction:
    def __init__(self, numerator: int, denominator: int):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Чисельник і знаменник мають бути цілими числами")
        if denominator == 0:
            raise ValueError("Знаменник не може бути нульовим")
        sign = -1 if denominator < 0 else 1
        self.numerator = numerator * sign
        self.denominator = abs(denominator)
        self._reduce()

    def _reduce(self):
        common = gcd(self.numerator, self.denominator)
        self.numerator //= common
        self.denominator //= common

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented
        if other.numerator == 0:
            raise ZeroDivisionError("Ділення на дріб із нульовим чисельником")
        num = self.numerator * other.denominator
        den = self.denominator * other.numerator
        return Fraction(num, den)

    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)

# if __name__ == "__main__":
#     x = Fraction(1, 2)
#     y = Fraction(1, 4)
#
#     print(x + y)  # 3/4
#     print(x - y)  # 1/4
#     print(x * y)  # 1/8
#     print(x / y)  # 2/1
