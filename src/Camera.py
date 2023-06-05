from OpenGL.GL import *


class Camera:
    def __init__(self):
        self.rotation_speed = 0.5
        self.mouse_sensitivity = 0.1
        self.yaw = 0.0
        self.pitch = 0.0

    def move(self, mouse_movement):
        self.yaw -= mouse_movement[0] * self.mouse_sensitivity
        self.pitch -= mouse_movement[1] * self.mouse_sensitivity

    def update(self, player_position):
        glLoadIdentity()
        glRotatef(-self.pitch, 1, 0, 0)
        glRotatef(-self.yaw, 0, 1, 0)
        glTranslatef(-player_position.x, -player_position.y, -player_position.z)
