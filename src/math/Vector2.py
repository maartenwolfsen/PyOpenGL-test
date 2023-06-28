import math
from src.math.Quaternion import Quaternion


class Vector2:
    def __init__(self, x=0.0, y=0.0):
        self.x = float(x)
        self.y = float(y)

    def __add__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        else:
            raise TypeError(f"Unsupported operand type for +: Vector2 and {type(other)}")

    def __sub__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        elif isinstance(other, Quaternion):
            return -other + self
        else:
            raise TypeError(f"Unsupported operand type for -: Vector2 and {type(other)}")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector2(self.x * other, self.y * other)
        elif isinstance(other, Vector2):
            return Vector2(self.x * other.x, self.y * other.y)
        elif isinstance(other, Quaternion):
            return other * self
        else:
            raise TypeError(f"Unsupported operand type for *: Vector2 and {type(other)}")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            return Vector2(self.x / other, self.y / other)
        elif isinstance(other, Vector2):
            magnitude_squared = self.magnitude_squared()
            if magnitude_squared == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            return Vector2(self.x / magnitude_squared, self.y / magnitude_squared)
        else:
            raise TypeError("Unsupported operand type for division.")

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def __eq__(self, other):
        if isinstance(other, Vector2):
            return math.isclose(self.x, other.x) and math.isclose(self.y, other.y)
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return f"Vector2({self.x}, {self.y})"

    def __repr__(self):
        return str(self)

    def __gt__(self, other):
        if isinstance(other, Vector2):
            return self.length_squared() > other.length_squared()
        elif isinstance(other, (int, float)):
            return self.length_squared() > other
        else:
            raise TypeError(f"Unsupported operand type for >: Vector2 and {type(other)}")

    def __ge__(self, other):
        if isinstance(other, Vector2):
            return self.length_squared() >= other.length_squared()
        elif isinstance(other, (int, float)):
            return self.length_squared() >= other
        else:
            raise TypeError(f"Unsupported operand type for >=: Vector2 and {type(other)}")

    def __lt__(self, other):
        if isinstance(other, Vector2):
            return self.length_squared() < other.length_squared()
        elif isinstance(other, (int, float)):
            return self.length_squared() < other
        else:
            raise TypeError(f"Unsupported operand type for <: Vector2 and {type(other)}")

    def __le__(self, other):
        if isinstance(other, Vector2):
            return self.length_squared() <= other.length_squared()
        elif isinstance(other, (int, float)):
            return self.length_squared() <= other
        else:
            raise TypeError(f"Unsupported operand type for <=: Vector2 and {type(other)}")

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Vector2 index out of range")

    def __setitem__(self, index, value):
        if index == 0:
            self.x = float(value)
        elif index == 1:
            self.y = float(value)
        else:
            raise IndexError("Vector2 index out of range")

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def length_squared(self):
        return self.x ** 2 + self.y ** 2

    def normalize(self):
        length = self.length()
        if length != 0:
            return Vector2(self.x / length, self.y / length)
        else:
            raise ValueError("Cannot normalize the zero vector.")

    def dot(self, other):
        if isinstance(other, Vector2):
            return self.x * other.x + self.y * other.y
        else:
            raise TypeError(f"Unsupported operand type for dot product: Vector2 and {type(other)}")

    def cross(self, other):
        raise NotImplementedError("Cross product is not supported in Vector2.")

    def rotate(self, angle):
        radians = math.radians(angle)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)
        x = self.x * cos_theta - self.y * sin_theta
        y = self.x * sin_theta + self.y * cos_theta
        return Vector2(x, y)

    def conjugate(self):
        return Vector2(self.x, -self.y)

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def magnitude_squared(self):
        return self.x ** 2 + self.y ** 2
