from src.primitives.Cube import Cube
from src.primitives.Plane import Plane
from src.GameObject import GameObject
from src.math.Vector3 import Vector3
from src.components.Transform import Transform
from src.components.Collider import Collider
from OpenGL.GL import *
from OpenGL.GLU import *
import glfw


class Scene:
    def __init__(self, id):
        self.id = id
        t1 = Transform(
            Vector3(0, -1, 0),
            Vector3(1, 1, 1),
            Vector3(100, 1, 100)
        )
        t2 = Transform(
            Vector3(1, 0, 4),
            Vector3(2, 2, 2),
            Vector3(2, 2, 2)
        )
        t3 = Transform(
            Vector3(-5, 0, 4),
            Vector3(2, 2, 2),
            Vector3(2, 2, 2)
        )
        t4 = Transform(
            Vector3(-8, -0.5, 4),
            Vector3(2, 2, 2),
            Vector3(2, 1, 2)
        )
        t5 = Transform(
            Vector3(4, 0, 4),
            Vector3(0, 0, 0),
            Vector3(0.5, 2, 0.5)
        )
        self.game_objects = [
            GameObject(
                "ground",
                t1,
                Plane(),
                Collider(t1)
            ),
            GameObject(
                "cube1",
                t2,
                Cube(),
                Collider(t2)
            ),
            GameObject(
                "cube2",
                t3,
                Cube(),
                Collider(t3)
            ),
            GameObject(
                "cube3",
                t4,
                Cube(),
                Collider(t4)
            ),
            GameObject(
                "enemy1",
                t5,
                Cube(),
                Collider(t5)
            ),
        ]

        glLightfv(GL_LIGHT0, GL_POSITION, [1.5, 1.5, 1.5, 1.0])
        glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 1.0])
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [10.0, 10.0, 10.0, 1.0])
        glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])

    def add(self, game_object):
        self.game_objects.append(game_object)

    def render(self, display, camera, player, debug=False):
        glViewport(0, 0, display.width, display.height)
        gluPerspective(45, (display.width / display.height), 0.1, 50.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        camera.update(player.transform.position)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

        for o in self.game_objects:
            o.draw()

            if debug:
                o.collider.draw()

        display.draw_crosshair()

        glfw.swap_buffers(display.screen)
