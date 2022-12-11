import math
class Fraction:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        y = abs(self.y * other.y) / math.gcd(self.y, other.y)
        x = self.x * (y / self.y) + other.x * (y / other.y)
        return Fraction(int(x), int(y))

    def __str__(self):
        return f'{self.x} / {self.y}'

if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    x + y == Fraction(3, 4)

    print(x+y)