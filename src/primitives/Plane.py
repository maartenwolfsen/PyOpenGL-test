from OpenGL.GL import *


class Plane:
    def draw(self, transform):
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)

        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

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

        glDisable(GL_TEXTURE_2D)
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

        glEnable(GL_TEXTURE_2D)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
