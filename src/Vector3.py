import math
from src.Quaternion import Quaternion


class Vector3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __add__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, Quaternion):
            return other + self
        else:
            raise TypeError(f"Unsupported operand type for +: Vector3 and {type(other)}")

    def __sub__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, Quaternion):
            return -other + self
        else:
            raise TypeError(f"Unsupported operand type for -: Vector3 and {type(other)}")

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector3(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, Vector3):
            return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)
        elif isinstance(other, Quaternion):
            return other * self
        else:
            raise TypeError(f"Unsupported operand type for *: Vector3 and {type(other)}")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            return Vector3(self.x / other, self.y / other, self.z / other)
        elif isinstance(other, Vector3):
            magnitude_squared = self.magnitude_squared()
            if magnitude_squared == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            return Vector3(self.x / magnitude_squared, self.y / magnitude_squared, self.z / magnitude_squared)
        else:
            raise TypeError("Unsupported operand type for division.")

    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)

    def __eq__(self, other):
        if isinstance(other, Vector3):
            return math.isclose(self.x, other.x) and math.isclose(self.y, other.y) and math.isclose(self.z, other.z)
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return f"Vector3({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return str(self)

    def __gt__(self, other):
        if isinstance(other, Vector3):
            return self.length_squared() > other.length_squared()
        elif isinstance(other, (int, float)):
            return self.length_squared() > other
        else:
            raise TypeError(f"Unsupported operand type for >: Vector3 and {type(other)}")

    def __ge__(self, other):
        if isinstance(other, Vector3):
            return self.length_squared() >= other.length_squared()
        elif isinstance(other, (int, float)):
            return self.length_squared() >= other
        else:
            raise TypeError(f"Unsupported operand type for >=: Vector3 and {type(other)}")

    def __lt__(self, other):
        if isinstance(other, Vector3):
            return self.length_squared() < other.length_squared()
        elif isinstance(other, (int, float)):
            return self.length_squared() < other
        else:
            raise TypeError(f"Unsupported operand type for <: Vector3 and {type(other)}")

    def __le__(self, other):
        if isinstance(other, Vector3):
            return self.length_squared() <= other.length_squared()
        elif isinstance(other, (int, float)):
            return self.length_squared() <= other
        else:
            raise TypeError(f"Unsupported operand type for <=: Vector3 and {type(other)}")

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
            self.x = float(value)
        elif index == 1:
            self.y = float(value)
        elif index == 2:
            self.z = float(value)
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
        elif isinstance(other, Quaternion):
            return other.dot(self)  # Delegate dot product to the Quaternion class
        else:
            raise TypeError(f"Unsupported operand type for dot product: Vector3 and {type(other)}")

    def cross(self, other):
        if isinstance(other, Vector3):
            x = self.y * other.z - self.z * other.y
            y = self.z * other.x - self.x * other.z
            z = self.x * other.y - self.y * other.x
            return Vector3(x, y, z)
        elif isinstance(other, Quaternion):
            raise TypeError(f"Unsupported operand type for cross product: Vector3 and {type(other)}")
        else:
            raise TypeError(f"Unsupported operand type for cross product: Vector3 and {type(other)}")

    def rotate(self, quaternion):
        # Perform quaternion rotation: v' = q * v * q_conjugate
        rotated_quat = quaternion * Quaternion(self.x, self.y, self.z, 0.0) * quaternion.conjugate()

        # Extract the vector part from the rotated quaternion
        rotated_vec = Vector3(rotated_quat.x, rotated_quat.y, rotated_quat.z)

        # Return the rotated vector
        return rotated_vec

    def conjugate(self):
        return Vector3(self.x, -self.y, -self.z)

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def magnitude_squared(self):
        return self.x ** 2 + self.y ** 2 + self.z ** 2
