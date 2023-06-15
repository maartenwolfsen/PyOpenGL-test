import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from src.Scene import Scene
from src.Player import Player
from src.Texture import Texture
from src.math.Vector3 import Vector3
from src.GameObject import GameObject
from src.Collider import Collider
from src.components.Transform import Transform
from src.primitives.Cube import Cube
from src.primitives.Plane import Plane
from src.Camera import Camera
from src.Display import Display
from src.Ray import Ray

DEBUG = False
pygame.init()

display = Display(800, 600)
display.screen = pygame.display.set_mode((display.display_width, display.display_height), DOUBLEBUF | OPENGL)
pygame.mouse.set_visible(False)

player = Player()
camera = Camera()
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
scene = Scene(
    "world1",
    [
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
)

texture = Texture()

glMatrixMode(GL_PROJECTION)
gluPerspective(45, (display.display_width / display.display_height), 0.1, 50.0)
glLoadIdentity()

glEnable(GL_DEPTH_TEST)

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
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE and player.jumped:
                player.jumped = False
        if event.type == pygame.MOUSEBUTTONUP:
            ray = Ray(
                Vector3(
                    player.transform.position.x + (player.transform.scale.x / 2),
                    player.transform.position.y + (player.transform.scale.y / 2),
                    player.transform.position.z + (player.transform.scale.z / 2)
                ),
                camera.get_direction()
            )

            for o in scene.game_objects:
                hit = ray.intersect_ray_collider(o.collider)

                if hit is not None:
                    t = Transform(
                        hit,
                        Vector3(0, 0, 0),
                        Vector3(0.5, 0.5, 0.5)
                    )
                    scene.add(
                        GameObject(
                            "hit" + str(ray.count),
                            t,
                            Cube(),
                            Collider(t)
                        )
                    )

                    for x in scene.game_objects:
                        print(x.id)
                        print(x.transform.position)

                    break

    keys = pygame.key.get_pressed()

    if player.velocity.y < player.drag:
        player.velocity.y += player.gravity

    collide = False
    for o in scene.game_objects:
        if hasattr(o, "collider") and o.collider.is_colliding(
                Transform(
                    Vector3(
                        player.transform.position.x,
                        player.transform.position.y - player.velocity.y,
                        player.transform.position.z
                    ),
                    player.transform.rotation,
                    player.transform.scale
                )):
            collide = True
            break

    player.grounded = False

    if collide:
        player.velocity.y = 0
        player.grounded = True

    if keys[pygame.K_SPACE] and player.grounded and not player.jumped:
        player.velocity.y = -player.jump_force
        player.jumped = True

    player.transform.position.y -= player.velocity.y

    if keys[pygame.K_a]:
        player.move_player('a', camera, scene.game_objects)

    if keys[pygame.K_d]:
        player.move_player('d', camera, scene.game_objects)

    if keys[pygame.K_w]:
        player.move_player('w', camera, scene.game_objects)

    if keys[pygame.K_s]:
        player.move_player('s', camera, scene.game_objects)

    camera.move(pygame.mouse.get_rel())
    pygame.mouse.set_pos(display.display_width // 2, display.display_height // 2)


def render_scene():
    glViewport(0, 0, display.display_width, display.display_height)
    gluPerspective(45, (display.display_width / display.display_height), 0.1, 50.0)
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

    for o in scene.game_objects:
        o.draw()

        if DEBUG:
            o.collider.draw()

    glDisable(GL_TEXTURE_2D)
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)
    glDisable(GL_COLOR_MATERIAL)

    display.draw_crosshair()

    pygame.display.flip()
    pygame.time.wait(10)


texture_id = texture.load("assets/materials/brickwall.png")
normal_map_texture_id = texture.load("assets/materials/brickwall_normal.png")

while True:
    handle_input()
    render_scene()
