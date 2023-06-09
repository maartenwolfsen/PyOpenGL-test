from src.Vector3 import Vector3
from src.components.Transform import Transform
from OpenGL.GL import *


class Enemy:
    def __init__(self):
        self.transform = Transform(
            Vector3(4, 0, 4),
            Vector3(0, 0, 0),
            Vector3(0.5, 2, 0.5)
        )
        self.health = 100

    def draw(self):
        vertices = [
            [self.transform.scale.x / 2, -self.transform.scale.y / 2, -self.transform.scale.z / 2],
            [self.transform.scale.x / 2, -self.transform.scale.y / 2, self.transform.scale.z / 2],
            [-self.transform.scale.x / 2, -self.transform.scale.y / 2, self.transform.scale.z / 2],
            [-self.transform.scale.x / 2, -self.transform.scale.y / 2, -self.transform.scale.z / 2],
            [self.transform.scale.x / 2, self.transform.scale.y / 2, -self.transform.scale.z / 2],
            [self.transform.scale.x / 2, self.transform.scale.y / 2, self.transform.scale.z / 2],
            [-self.transform.scale.x / 2, self.transform.scale.y / 2, self.transform.scale.z / 2],
            [-self.transform.scale.x / 2, self.transform.scale.y / 2, -self.transform.scale.z / 2]
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
                    vertices[vertex][0] + self.transform.position.x,
                    vertices[vertex][1] + self.transform.position.y,
                    vertices[vertex][2] + self.transform.position.z
                ])
        glEnd()
