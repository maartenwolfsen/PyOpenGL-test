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
gameObjects = [
    GameObject(
        Transform(
            Vector3(0, -0.5, 0),
            Vector3(1, 1, 1),
            Vector3(10, 10, 10)
        ),
        Plane(),
        "test"
    ),
    GameObject(
        Transform(
            Vector3(1, 0, 0),
            Vector3(1, 1, 1),
            Vector3(1, 1, 1)
        ),
        Cube(),
        "test"
    ),
    GameObject(
        Transform(
            Vector3(-1, 0, 0),
            Vector3(1, 1, 1),
            Vector3(1, 1, 1)
        ),
        Cube(),
        "test"
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
    if keys[pygame.K_a]:
        player.position[0] += player.speed * math.sin(math.radians(camera.yaw - 90))
        player.position[2] += player.speed * math.cos(math.radians(camera.yaw - 90))
    if keys[pygame.K_d]:
        player.position[0] -= player.speed * math.sin(math.radians(camera.yaw - 90))
        player.position[2] -= player.speed * math.cos(math.radians(camera.yaw - 90))
    if keys[pygame.K_w]:
        player.position[0] -= player.speed * math.sin(math.radians(camera.yaw))
        player.position[2] -= player.speed * math.cos(math.radians(camera.yaw))
    if keys[pygame.K_s]:
        player.position[0] += player.speed * math.sin(math.radians(camera.yaw))
        player.position[2] += player.speed * math.cos(math.radians(camera.yaw))

    camera.move(pygame.mouse.get_rel())

    pygame.mouse.set_pos(display_width // 2, display_height // 2)


def check_collision(position, size, point):
    min_x = position[0] - size / 2
    max_x = position[0] + size / 2
    min_y = position[1] - size / 2
    max_y = position[1] + size / 2
    min_z = position[2] - size / 2
    max_z = position[2] + size / 2

    if min_x <= point[0] <= max_x and min_y <= point[1] <= max_y and min_z <= point[2] <= max_z:
        return True
    return False


def render_scene():
    glViewport(0, 0, display_width, display_height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (display_width / display_height), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    camera.update(player.position)

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

    #if check_collision(cube_position, cube_size, (player_x, player_y, player_z)):
    #    player_x = 0.0
    #    player_y = 0.0
    #    player_z = 0.0

    render_scene()
