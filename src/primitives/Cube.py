from OpenGL.GL import *
from src.Texture import Texture


class Cube:
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
            [transform.scale.x / 2, -transform.scale.y / 2, -transform.scale.z / 2],
            [transform.scale.x / 2, -transform.scale.y / 2, transform.scale.z / 2],
            [-transform.scale.x / 2, -transform.scale.y / 2, transform.scale.z / 2],
            [-transform.scale.x / 2, -transform.scale.y / 2, -transform.scale.z / 2],
            [transform.scale.x / 2, transform.scale.y / 2, -transform.scale.z / 2],
            [transform.scale.x / 2, transform.scale.y / 2, transform.scale.z / 2],
            [-transform.scale.x / 2, transform.scale.y / 2, transform.scale.z / 2],
            [-transform.scale.x / 2, transform.scale.y / 2, -transform.scale.z / 2]
        ]

        faces = [
            [0, 1, 2, 3],
            [3, 2, 6, 7],
            [7, 6, 5, 4],
            [4, 5, 1, 0],
            [5, 6, 2, 1],
            [7, 4, 0, 3]
        ]

        normals = [
            [0.0, -1.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],
            [0.0, 0.0, -1.0],
            [1.0, 0.0, 0.0],
            [-1.0, 0.0, 0.0]
        ]

        tex_coords = [
            [0, 0],
            [1, 0],
            [1, 1],
            [0, 1]
        ]

        glBegin(GL_QUADS)
        for face in faces:
            normal = normals[faces.index(face)]
            glNormal3fv(normal)
            for vertex, tex_coord in zip(face, tex_coords):
                glTexCoord2fv(tex_coord)
                glVertex3fv([
                    vertices[vertex][0] + transform.position.x,
                    vertices[vertex][1] + transform.position.y,
                    vertices[vertex][2] + transform.position.z
                ])
        glEnd()
