import math


class Quaternion:
    def __init__(self, w=1.0, x=0.0, y=0.0, z=0.0):
        self.w = w
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Quaternion({self.w}, {self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, Quaternion):
            return (
                math.isclose(self.w, other.w) and
                math.isclose(self.x, other.x) and
                math.isclose(self.y, other.y) and
                math.isclose(self.z, other.z)
            )
        return False

    def __mul__(self, other):
        from src.math.Vector3 import Vector3
        if isinstance(other, Quaternion):
            w = (self.w * other.w) - (self.x * other.x) - (self.y * other.y) - (self.z * other.z)
            x = (self.w * other.x) + (self.x * other.w) + (self.y * other.z) - (self.z * other.y)
            y = (self.w * other.y) - (self.x * other.z) + (self.y * other.w) + (self.z * other.x)
            z = (self.w * other.z) + (self.x * other.y) - (self.y * other.x) + (self.z * other.w)
            return Quaternion(w, x, y, z)
        elif isinstance(other, Vector3):
            vec_quat = Quaternion(0.0, other.x, other.y, other.z)
            rotated_quat = self * vec_quat * self.conjugate()
            rotated_vec = Vector3(rotated_quat.x, rotated_quat.y, rotated_quat.z)
            return rotated_vec
        elif isinstance(other, (int, float)):
            return Quaternion(self.w * other, self.x * other, self.y * other, self.z * other)
        return NotImplemented

    def conjugate(self):
        return Quaternion(-self.x, -self.y, -self.z, self.w)

    def inverse(self):
        conjugate = self.conjugate()
        magnitude_squared = self.magnitude_squared()
        return conjugate / magnitude_squared

    def magnitude(self):
        return src.math.sqrt(self.magnitude_squared())

    def magnitude_squared(self):
        return (self.w * self.w) + (self.x * self.x) + (self.y * self.y) + (self.z * self.z)

    def normalize(self):
        magnitude = self.magnitude()
        if magnitude != 0:
            self.w /= magnitude
            self.x /= magnitude
            self.y /= magnitude
            self.z /= magnitude

    @staticmethod
    def from_axis_angle(axis, angle):
        axis = axis.normalize()
        half_angle = angle / 2.0
        sin_half_angle = math.sin(half_angle)
        cos_half_angle = math.cos(half_angle)
        w = cos_half_angle
        x = axis.x * sin_half_angle
        y = axis.y * sin_half_angle
        z = axis.z * sin_half_angle
        return Quaternion(w, x, y, z)
