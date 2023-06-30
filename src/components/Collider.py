from src.GameObject import GameObject
from OpenGL.GL import *
from src.math.Vector3 import Vector3


class Collider(GameObject):
    def __init__(self, label="origin"):
        self.label = label
        self.bounds = None

    def initialize(self):
        self.bounds = self.calculate_bounds()

    def calculate_bounds(self):
        position = self.components["Transform"].position
        scale = self.components["Transform"].scale

        min_bounds = position - scale / 2
        max_bounds = position + scale / 2

        return min_bounds, max_bounds

    def is_colliding(self, collider):
        self_half_size = self.components["Transform"].scale * 0.5
        collider_half_size = collider.scale * 0.5

        # Calculate the centers of the bounding boxes
        self_center = self.components["Transform"].position
        collider_center = collider.position

        # Calculate the differences between the centers
        center_diff = collider_center - self_center

        # Check for overlap along the x-axis
        if abs(center_diff.x) > (self_half_size.x + collider_half_size.x):
            return False

        # Check for overlap along the y-axis
        if abs(center_diff.y) > (self_half_size.y + collider_half_size.y):
            return False

        # Check for overlap along the z-axis
        if abs(center_diff.z) > (self_half_size.z + collider_half_size.z):
            return False

        # Check for overlap along the separating axes
        separating_axes = [
            Vector3(1, 0, 0),
            Vector3(0, 1, 0),
            Vector3(0, 0, 1)
        ]

        for axis in separating_axes:
            # Project the vertices of the objects onto the separating axis
            self_min = self_center.dot(axis) - self_half_size.dot(axis)
            self_max = self_center.dot(axis) + self_half_size.dot(axis)
            collider_min = collider_center.dot(axis) - collider_half_size.dot(axis)
            collider_max = collider_center.dot(axis) + collider_half_size.dot(axis)

            # Check for overlap on the separating axis
            if (self_max < collider_min) or (self_min > collider_max):
                return False

        # If no separating axis has overlap, collision occurs
        return True

    def draw(self):
        glDisable(GL_TEXTURE_2D)
        glDisable(GL_LIGHTING)
        glDisable(GL_LIGHT0)

        vertices = (
            (self.components["Transform"].scale.x / 2 + 0.01, -self.components["Transform"].scale.y / 2 - 0.01, -self.components["Transform"].scale.z / 2 - 0.01),
            (self.components["Transform"].scale.x / 2 + 0.01, self.components["Transform"].scale.y / 2 + 0.01, -self.components["Transform"].scale.z / 2 - 0.01),
            (-self.components["Transform"].scale.x / 2 - 0.01, self.components["Transform"].scale.y / 2 + 0.01, -self.components["Transform"].scale.z / 2 - 0.01),
            (-self.components["Transform"].scale.x / 2 - 0.01, -self.components["Transform"].scale.y / 2 - 0.01, -self.components["Transform"].scale.z / 2 - 0.01),
            (self.components["Transform"].scale.x / 2 + 0.01, -self.components["Transform"].scale.y / 2 - 0.01, self.components["Transform"].scale.z / 2 + 0.01),
            (self.components["Transform"].scale.x / 2 + 0.01, self.components["Transform"].scale.y / 2 + 0.01, self.components["Transform"].scale.z / 2 + 0.01),
            (-self.components["Transform"].scale.x / 2 - 0.01, -self.components["Transform"].scale.y / 2 - 0.01, self.components["Transform"].scale.z / 2 + 0.01),
            (-self.components["Transform"].scale.x / 2 - 0.01, self.components["Transform"].scale.y / 2 + 0.01, self.components["Transform"].scale.z / 2 + 0.01)
        )

        faces = (
            (0, 1, 2, 3),
            (3, 2, 7, 6),
            (6, 7, 5, 4),
            (4, 5, 1, 0),
            (1, 5, 7, 2),
            (4, 0, 3, 6)
        )

        colors = (
            (0, 1, 0.4),
        )

        glBegin(GL_QUADS)
        for face in faces:
            glColor3fv(colors[0])
            for vertex in face:
                glVertex3fv([
                    vertices[vertex][0] + self.components["Transform"].position.x,
                    vertices[vertex][1] + self.components["Transform"].position.y,
                    vertices[vertex][2] + self.components["Transform"].position.z
                ])
        glEnd()

        glEnable(GL_TEXTURE_2D)
        glEnable(GL_LIGHT0)
