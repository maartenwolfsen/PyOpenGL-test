from OpenGL.GL import *
from src.Texture import Texture


class Plane:
    def __init__(self):
        self.texture = Texture()
        self.texture_id = self.texture.load("assets/materials/brickwall.png")
        self.normal_map_texture_id = self.texture.load("assets/materials/brickwall_normal.png")

    def draw(self, transform):
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.texture_id)

        glActiveTexture(GL_TEXTURE1)
        glBindTexture(GL_TEXTURE_2D, self.normal_map_texture_id)

        vertices = [
            [transform.scale.x / 2, 0.0, -transform.scale.x / 2],
            [transform.scale.x / 2, 0.0, transform.scale.x / 2],
            [-transform.scale.x / 2, 0.0, transform.scale.x / 2],
            [-transform.scale.x / 2, 0.0, -transform.scale.x / 2]
        ]

        normal = [0.0, 1.0, 0.0]

        tex_coords = [
            [0, 0],
            [1, 0],
            [1, 1],
            [0, 1]
        ]

        glBegin(GL_QUADS)
        glNormal3fv(normal)

        for vertex, tex_coord in zip(vertices, tex_coords):
            glTexCoord2fv(tex_coord)
            glVertex3fv([
                vertex[0] + transform.position.x,
                vertex[1] + transform.position.y,
                vertex[2] + transform.position.z
            ])
        glEnd()
