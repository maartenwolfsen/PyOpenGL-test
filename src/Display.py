from OpenGL.GL import *


class Display:
    def __init__(self, display_width, display_height):
        self.display_width = display_width
        self.display_height = display_height
        self.screen = 0

    def draw_crosshair(self):
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        glOrtho(0, self.display_width, 0, self.display_height, -1, 1)
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()
        glDisable(GL_LIGHTING)

        glLineWidth(2.0)
        glColor3f(1.0, 1.0, 1.0)

        glBegin(GL_LINES)
        glVertex2f(self.display_width / 2 - 10, self.display_height / 2)
        glVertex2f(self.display_width / 2 + 10, self.display_height / 2)

        glVertex2f(self.display_width / 2, self.display_height / 2 - 10)
        glVertex2f(self.display_width / 2, self.display_height / 2 + 10)
        glEnd()

        glEnable(GL_LIGHTING)

        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)
        glPopMatrix()
