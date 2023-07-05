from src.GameObject import GameObject
from OpenGL.GL import *
from src.math.Vector2 import Vector2


class Camera(GameObject):
    def __init__(self):
        self.rotation_speed = 0.5
        self.mouse_sensitivity = 0.1
        self.yaw = 0.0
        self.pitch = 0.0
        self.last_mouse_x = 0
        self.last_mouse_y = 0

    def move(self, mouse_movement):
        self.yaw -= mouse_movement[0] * self.mouse_sensitivity
        self.pitch -= mouse_movement[1] * self.mouse_sensitivity

    def update(self):
        position = self.components["Transform"].position

        glLoadIdentity()
        glRotatef(-self.pitch, 1, 0, 0)
        glRotatef(-self.yaw, 0, 1, 0)
        glTranslatef(-position.x, -position.y, -position.z)

    def get_direction(self):
        return Vector2(
            self.pitch,
            self.yaw
        )
