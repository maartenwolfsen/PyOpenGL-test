import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
from src.Player import Player
from src.Camera import Camera
from src.Texture import Texture

from src.Vector3 import Vector3
from src.GameObject import GameObject
from src.Collider import Collider
from src.components.Transform import Transform
from src.primitives.Cube import Cube
from src.primitives.Plane import Plane

pygame.init()

display_width = 800
display_height = 600
pygame.display.set_mode((display_width, display_height), DOUBLEBUF | OPENGL)
pygame.mouse.set_visible(False)

player = Player()
camera = Camera()
t1 = Transform(
            Vector3(0, -1, 0),
            Vector3(1, 1, 1),
            Vector3(100, 1, 100)
        )
t2 = Transform(
            Vector3(1, 0, 2),
            Vector3(2, 2, 2),
            Vector3(1, 1, 1)
        )
t3 = Transform(
            Vector3(-1, 0, 2),
            Vector3(2, 2, 2),
            Vector3(1, 1, 1)
        )
t4 = Transform(
            Vector3(-2, -0.25, 2),
            Vector3(2, 2, 2),
            Vector3(1, 0.5, 1)
        )
gameObjects = [
    #GameObject(
    #    t1,
    #    Plane(),
    #    Collider(t1)
    #),
    GameObject(
        t2,
        Cube(),
        Collider(t2)
    ),
    GameObject(
        t3,
        Cube(),
        Collider(t3)
    ),
    GameObject(
        t4,
        Cube(),
        Collider(t4)
    )
]

texture = Texture()

glViewport(0, 0, display_width, display_height)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(45, (display_width / display_height), 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)

glLightfv(GL_LIGHT0, GL_POSITION, [1.5, 1.5, 1.5, 1.0])
glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 1.0])
glLightfv(GL_LIGHT0, GL_DIFFUSE, [10.0, 10.0, 10.0, 1.0])
glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])


def handle_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

    keys = pygame.key.get_pressed()

    temp_player = Player()
    t = player.transform
    temp_player.transform = Transform(
        Vector3(t.position.x, t.position.y, t.position.z),
        Vector3(t.rotation.x, t.rotation.y, t.rotation.z),
        Vector3(t.scale.x, t.scale.y, t.scale.z)
    )

    if keys[pygame.K_a]:
        temp_player.transform.position.x += player.speed * math.sin(math.radians(camera.yaw - 90))
        temp_player.transform.position.z += player.speed * math.cos(math.radians(camera.yaw - 90))
    if keys[pygame.K_d]:
        temp_player.transform.position.x -= player.speed * math.sin(math.radians(camera.yaw - 90))
        temp_player.transform.position.z -= player.speed * math.cos(math.radians(camera.yaw - 90))
    if keys[pygame.K_w]:
        temp_player.transform.position.x -= player.speed * math.sin(math.radians(camera.yaw))
        temp_player.transform.position.z -= player.speed * math.cos(math.radians(camera.yaw))
    if keys[pygame.K_s]:
        temp_player.transform.position.x += player.speed * math.sin(math.radians(camera.yaw))
        temp_player.transform.position.z += player.speed * math.cos(math.radians(camera.yaw))

    colliding = False
    for go in gameObjects:
        if go.collider.is_colliding(temp_player):
            colliding = True
            break

    if not colliding:
        player.transform = temp_player.transform

    camera.move(pygame.mouse.get_rel())

    pygame.mouse.set_pos(display_width // 2, display_height // 2)


def render_scene():
    glViewport(0, 0, display_width, display_height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (display_width / display_height), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    camera.update(player.transform.position)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    glActiveTexture(GL_TEXTURE1)
    glBindTexture(GL_TEXTURE_2D, normal_map_texture_id)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    for o in gameObjects:
        o.draw()

    glDisable(GL_TEXTURE_2D)
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)

    pygame.display.flip()
    pygame.time.wait(10)


texture_id = texture.load("assets/materials/brickwall.png")
normal_map_texture_id = texture.load("assets/materials/brickwall_normal.png")

while True:
    handle_input()
    render_scene()
