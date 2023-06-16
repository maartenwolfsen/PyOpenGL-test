from OpenGL.GL import *
from OpenGL.GLU import *
from src.math.Vector2 import Vector2
import glfw


class Display:
    def __init__(self, width, height):
        if not glfw.init():
            print("Failed to initialize GLFW\n")
            quit()

        self.width = width
        self.height = height
        self.screen = glfw.create_window(width, height, "My Game", None, None)

        if not self.screen:
            print(
                "Failed to open GLFW window. If you have an Intel GPU, they are not 3.3 compatible. Try the 2.1 "
                "version of the tutorials.\n"
            )
            glfw.terminate()
            quit()

        self.mouse_position = Vector2(0, 0)

        glfw.window_hint(glfw.SAMPLES, 4)
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        glfw.make_context_current(self.screen)
        glMatrixMode(GL_PROJECTION)
        gluPerspective(45, (self.width / self.height), 0.1, 50.0)
        glLoadIdentity()
        glEnable(GL_DEPTH_TEST)
        glfw.set_cursor_pos(self.screen, self.width / 2, self.height / 2)
        glfw.set_input_mode(self.screen, glfw.CURSOR, glfw.CURSOR_DISABLED)

    def draw_crosshair(self):
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        glOrtho(0, self.width, 0, self.height, -1, 1)
        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()
        glDisable(GL_LIGHTING)

        glLineWidth(2.0)
        glColor3f(1.0, 1.0, 1.0)

        glBegin(GL_LINES)
        glVertex2f(self.width / 2 - 10, self.height / 2)
        glVertex2f(self.width / 2 + 10, self.height / 2)

        glVertex2f(self.width / 2, self.height / 2 - 10)
        glVertex2f(self.width / 2, self.height / 2 + 10)
        glEnd()

        glEnable(GL_LIGHTING)

        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)
        glPopMatrix()

    def get_relative_mouse_movement(self):
        current_x, current_y = glfw.get_cursor_pos(self.screen)
        delta_x = current_x - self.mouse_position.x
        delta_y = current_y - self.mouse_position.y
        self.mouse_position.x = current_x
        self.mouse_position.y = current_y

        return delta_x, delta_y
