import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GL.framebufferobjects import *
from OpenGL.GL.ARB.shadow import *
import math
from PIL import Image

pygame.init()

display_width = 800
display_height = 600
pygame.display.set_mode((display_width, display_height), DOUBLEBUF | OPENGL)
pygame.mouse.set_visible(False)

player_x = 0.0
player_y = 0.0
player_z = 0.0

player_speed = 0.05
player_rotation_speed = 0.5
mouse_sensitivity = 0.1

camera_yaw = 0.0
camera_pitch = 0.0

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

def draw_plane(size, position):
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    vertices = [
        [size / 2, 0.0, -size / 2],
        [size / 2, 0.0, size / 2],
        [-size / 2, 0.0, size / 2],
        [-size / 2, 0.0, -size / 2]
    ]

    normal = [0.0, 1.0, 0.0]

    tex_coords = [
        [0, 0],
        [1, 0],
        [1, 1],
        [0, 1]
    ]

    glDisable(GL_TEXTURE_2D)  # Disable texturing for the shadow plane

    glBegin(GL_QUADS)
    glNormal3fv(normal)
    for vertex, tex_coord in zip(vertices, tex_coords):
        glTexCoord2fv(tex_coord)
        glVertex3fv([vertex[0] + position[0], vertex[1] + position[1], vertex[2] + position[2]])
    glEnd()

    glEnable(GL_TEXTURE_2D)  # Re-enable texturing

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)


def draw_cube(size, position):
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    vertices = [
        [size / 2, -size / 2, -size / 2],
        [size / 2, -size / 2, size / 2],
        [-size / 2, -size / 2, size / 2],
        [-size / 2, -size / 2, -size / 2],
        [size / 2, size / 2, -size / 2],
        [size / 2, size / 2, size / 2],
        [-size / 2, size / 2, size / 2],
        [-size / 2, size / 2, -size / 2]
    ]

    faces = [
        [0, 1, 2, 3],
        [3, 2, 6, 7],
        [7, 6, 5, 4],
        [4, 5, 1, 0],
        [5, 6, 2, 1],
        [7, 4, 0, 3]
    ]

    normals = [
        [0.0, -1.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
        [0.0, 0.0, -1.0],
        [1.0, 0.0, 0.0],
        [-1.0, 0.0, 0.0]
    ]

    tex_coords = [
        [0, 0],
        [1, 0],
        [1, 1],
        [0, 1]
    ]

    glBegin(GL_QUADS)
    for face in faces:
        normal = normals[faces.index(face)]
        glNormal3fv(normal)
        for vertex, tex_coord in zip(face, tex_coords):
            glTexCoord2fv(tex_coord)
            glVertex3fv([vertices[vertex][0] + position[0], vertices[vertex][1] + position[1],
                         vertices[vertex][2] + position[2]])
    glEnd()


def handle_input():
    global player_x, player_z, camera_yaw, camera_pitch

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
        player_x += player_speed * math.sin(math.radians(camera_yaw - 90))
        player_z += player_speed * math.cos(math.radians(camera_yaw - 90))
    if keys[pygame.K_d]:
        player_x -= player_speed * math.sin(math.radians(camera_yaw - 90))
        player_z -= player_speed * math.cos(math.radians(camera_yaw - 90))
    if keys[pygame.K_w]:
        player_x -= player_speed * math.sin(math.radians(camera_yaw))
        player_z -= player_speed * math.cos(math.radians(camera_yaw))
    if keys[pygame.K_s]:
        player_x += player_speed * math.sin(math.radians(camera_yaw))
        player_z += player_speed * math.cos(math.radians(camera_yaw))

    mouse_movement = pygame.mouse.get_rel()
    camera_yaw -= mouse_movement[0] * mouse_sensitivity
    camera_pitch -= mouse_movement[1] * mouse_sensitivity

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


def load_texture(filename):
    image = Image.open(filename)
    image = image.transpose(Image.FLIP_TOP_BOTTOM)
    image_data = image.convert("RGBA").tobytes()

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.width, image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)
    glGenerateMipmap(GL_TEXTURE_2D)

    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    return texture_id


def update_camera():
    glLoadIdentity()
    glRotatef(-camera_pitch, 1, 0, 0)
    glRotatef(-camera_yaw, 0, 1, 0)
    glTranslatef(-player_x, -player_y, -player_z)

def render_scene():
    glViewport(0, 0, display_width, display_height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (display_width / display_height), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    update_camera()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glEnable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texture_id)

    glActiveTexture(GL_TEXTURE1)
    glBindTexture(GL_TEXTURE_2D, normal_map_texture_id)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    draw_cube(1, (1, 0, 0))
    draw_cube(1, (-1, 0, 0))
    draw_plane(10, (0, -0.5, 0))

    glDisable(GL_TEXTURE_2D)
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)

    pygame.display.flip()
    pygame.time.wait(10)


texture_id = load_texture("assets/materials/brickwall.png")
normal_map_texture_id = load_texture("assets/materials/brickwall_normal.png")

while True:
    handle_input()

    #if check_collision(cube_position, cube_size, (player_x, player_y, player_z)):
    #    player_x = 0.0
    #    player_y = 0.0
    #    player_z = 0.0

    update_camera()
    render_scene()
