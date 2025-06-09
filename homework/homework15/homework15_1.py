import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return math.isclose(self.get_square(), other.get_square(), rel_tol=1e-9)
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Rectangle):
            total_area = self.get_square() + other.get_square()
            side = math.sqrt(total_area)
            return Rectangle(round(side, 6), round(total_area / side, 6))
        return NotImplemented

    def __mul__(self, n):
        if isinstance(n, (int, float)):
            total_area = self.get_square() * n
            side = math.sqrt(total_area)
            return Rectangle(round(side, 6), round(total_area / side, 6))
        return NotImplemented

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height}, area={self.get_square()})"


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)

r3 = r1 + r2
assert round(r3.get_square(), 2) == 26, 'Test3'

r4 = r1 * 4
assert round(r4.get_square(), 2) == 32, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
print("Всі тести пройдені!")
pass