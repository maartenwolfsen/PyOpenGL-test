from OpenGL.GL import *


class Collider:
    def __init__(self, transform):
        self.transform = transform

    def is_colliding(self, collider):
        return (
            self.transform.position.x + self.transform.scale.x > collider.position.x
            and self.transform.position.x < collider.position.x + collider.scale.x
            and self.transform.position.y + self.transform.scale.y > collider.position.y
            and self.transform.position.y < collider.position.y + collider.scale.y
            and self.transform.position.z + self.transform.scale.z > collider.position.z
            and self.transform.position.z < collider.position.z + collider.scale.z
        )

    def draw(self):
        glDisable(GL_TEXTURE_2D)
        glDisable(GL_LIGHTING)
        glDisable(GL_LIGHT0)

        vertices = (
            (self.transform.scale.x / 2 + 0.01, -self.transform.scale.y / 2 - 0.01, -self.transform.scale.z / 2 - 0.01),
            (self.transform.scale.x / 2 + 0.01, self.transform.scale.y / 2 + 0.01, -self.transform.scale.z / 2 - 0.01),
            (-self.transform.scale.x / 2 - 0.01, self.transform.scale.y / 2 + 0.01, -self.transform.scale.z / 2 - 0.01),
            (-self.transform.scale.x / 2 - 0.01, -self.transform.scale.y / 2 - 0.01, -self.transform.scale.z / 2 - 0.01),
            (self.transform.scale.x / 2 + 0.01, -self.transform.scale.y / 2 - 0.01, self.transform.scale.z / 2 + 0.01),
            (self.transform.scale.x / 2 + 0.01, self.transform.scale.y / 2 + 0.01, self.transform.scale.z / 2 + 0.01),
            (-self.transform.scale.x / 2 - 0.01, -self.transform.scale.y / 2 - 0.01, self.transform.scale.z / 2 + 0.01),
            (-self.transform.scale.x / 2 - 0.01, self.transform.scale.y / 2 + 0.01, self.transform.scale.z / 2 + 0.01)
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
                    vertices[vertex][0] + self.transform.position.x,
                    vertices[vertex][1] + self.transform.position.y,
                    vertices[vertex][2] + self.transform.position.z
                ])
        glEnd()

        glEnable(GL_TEXTURE_2D)
        glEnable(GL_LIGHT0)
