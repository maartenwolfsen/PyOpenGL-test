import math


class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, (int, float)):
            return Vector3(self.x + other, self.y + other, self.z + other)
        else:
            raise TypeError("Unsupported operand type for +: Vector3 and {}".format(type(other)))

    def __sub__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, (int, float)):
            return Vector3(self.x - other, self.y - other, self.z - other)
        else:
            raise TypeError("Unsupported operand type for -: Vector3 and {}".format(type(other)))

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector3(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, Vector3):
            return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)
        else:
            raise TypeError("Unsupported operand type for *: Vector3 and {}".format(type(other)))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector3(self.x / other, self.y / other, self.z / other)
        elif isinstance(other, Vector3):
            return Vector3(self.x / other.x, self.y / other.y, self.z / other.z)
        else:
            raise TypeError("Unsupported operand type for /: Vector3 and {}".format(type(other)))

    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)

    def __eq__(self, other):
        if isinstance(other, Vector3):
            return self.x == other.x and self.y == other.y and self.z == other.z
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return "Vector3({}, {}, {})".format(self.x, self.y, self.z)

    def __repr__(self):
        return str(self)

    def __gt__(self, other):
        if isinstance(other, Vector3):
            return self.length_squared() > other.length_squared()
        elif isinstance(other, (int, float)):
            return self.length_squared() > other
        else:
            raise TypeError("Unsupported operand type for >: Vector3 and {}".format(type(other)))

    def __ge__(self, other):
        if isinstance(other, Vector3):
            return self.length_squared() >= other.length_squared()
        elif isinstance(other, (int, float)):
            return self.length_squared() >= other
        else:
            raise TypeError("Unsupported operand type for >=: Vector3 and {}".format(type(other)))

    def __lt__(self, other):
        if isinstance(other, Vector3):
            return self.length_squared() < other.length_squared()
        elif isinstance(other, (int, float)):
            return self.length_squared() < other
        else:
            raise TypeError("Unsupported operand type for <: Vector3 and {}".format(type(other)))

    def __le__(self, other):
        if isinstance(other, Vector3):
            return self.length_squared() <= other.length_squared()
        elif isinstance(other, (int, float)):
            return self.length_squared() <= other
        else:
            raise TypeError("Unsupported operand type for <=: Vector3 and {}".format(type(other)))

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        elif index == 2:
            return self.z
        else:
            raise IndexError("Vector3 index out of range")

    def __setitem__(self, index, value):
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        elif index == 2:
            self.z = value
        else:
            raise IndexError("Vector3 index out of range")

    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def length_squared(self):
        return self.x ** 2 + self.y ** 2 + self.z ** 2

    def normalize(self):
        length = self.length()
        if length != 0:
            return Vector3(self.x / length, self.y / length, self.z / length)
        else:
            raise ValueError("Cannot normalize the zero vector.")

    def dot(self, other):
        if isinstance(other, Vector3):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            raise TypeError("Unsupported operand type for dot product: Vector3 and {}".format(type(other)))

    def cross(self, other):
        if isinstance(other, Vector3):
            x = self.y * other.z - self.z * other.y
            y = self.z * other.x - self.x * other.z
            z = self.x * other.y - self.y * other.x
            return Vector3(x, y, z)
        else:
            raise TypeError("Unsupported operand type for cross product: Vector3 and {}".format(type(other)))
