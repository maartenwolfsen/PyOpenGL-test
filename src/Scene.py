from src.components.Mesh import Mesh
from src.GameObject import GameObject
from src.math.Vector3 import Vector3
from src.components.Transform import Transform
from src.components.Collider import Collider
from src.components.PhysicsBody import PhysicsBody
from src.components.FirstPerson.Camera import Camera as FirstPersonCamera
from src.components.FirstPerson.Controller import Controller as FirstPersonController
from src.physics.PhysicsWorld import PhysicsWorld
from OpenGL.GL import *
from OpenGL.GLU import *
import glfw


class Scene:
    def __init__(self, label):
        self.label = label
        self.game_objects = [
            GameObject(
                "ground",
                Transform(
                    Vector3(0, -10, 0),
                    Vector3(0, 0, 0),
                    Vector3(50, 1, 50)
                ),
                Mesh("cube"),
                Collider()
            ),
            GameObject(
                "physObj1",
                Transform(
                    Vector3(0, 2, -10),
                    Vector3(0, 0, 0),
                    Vector3(0.5, 0.5, 0.5)
                ),
                Mesh("cube"),
                Collider(),
                PhysicsBody()
            ),
            GameObject(
                "player",
                Transform(
                    Vector3(0, 0, 0),
                    Vector3(0, 0, 0),
                    Vector3(1, 1, 1)
                ),
                Collider(),
                PhysicsBody(),
                FirstPersonCamera(),
                FirstPersonController()
            )
        ]
        self.physics = PhysicsWorld(self)

        glLightfv(GL_LIGHT0, GL_POSITION, [1.5, 1.5, 1.5, 1.0])
        glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 1.0])
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [10.0, 10.0, 10.0, 1.0])
        glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])

    def add(self, game_object):
        self.game_objects.append(game_object)

    def update(self):
        for go in self.game_objects:
            if go.has("Camera"):
                go.components["Camera"].update()
            if go.has("Controller"):
                go.components["Controller"].update(self.game_objects)

        self.physics.update()

    def render(self, display, debug=False):
        glViewport(0, 0, display.width, display.height)
        gluPerspective(45, (display.width / display.height), 0.1, 50.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        self.update()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

        for o in self.game_objects:
            o.draw()

            if debug:
                o.components["Collider"].draw()

        display.draw_crosshair()

        glfw.swap_buffers(display.screen)

    def get_game_object_by_component(self, component):
        for go in self.game_objects:
            if component in go.components:
                return go
