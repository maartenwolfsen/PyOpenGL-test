from src.primitives.Cube import Cube
from src.primitives.Plane import Plane
from src.GameObject import GameObject
from src.math.Vector3 import Vector3
from src.components.Transform import Transform
from src.components.Collider import Collider
from src.components.PhysicsBody import PhysicsBody
from src.physics.PhysicsWorld import PhysicsWorld
from OpenGL.GL import *
from OpenGL.GLU import *
import glfw


class Scene:
    def __init__(self, label):
        self.label = label
        self.game_objects = [
            GameObject(
                "physObj1",
                Cube(),
                Transform(
                    Vector3(0, 2, -10),
                    Vector3(0, 0, 0),
                    Vector3(0.5, 0.5, 0.5)
                ),
                Collider(),
                PhysicsBody()
            )
        ]
        self.physics = PhysicsWorld(self)

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
