class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        new_a = self.a * other.b + other.a * self.b
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __sub__(self, other):
        new_a = self.a * other.b - other.a * self.b
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __mul__(self, other):
        new_a = self.a * other.a
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __eq__(self, other):
        return self.a * other.b == self.b * other.a

    def __lt__(self, other):
        return self.a * other.b < self.b * other.a

    def __gt__(self, other):
        return self.a * other.b > self.b * other.a

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"
f_a = Fraction(2, 3)
f_b = Fraction(3, 6)

f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'

f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'

f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c
assert f_d > f_e
assert f_a != f_b

f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2

print('OK')

pass
