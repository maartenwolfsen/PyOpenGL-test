import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

pygame.init()

display_width = 800
display_height = 600
pygame.display.set_mode((display_width, display_height), DOUBLEBUF | OPENGL)

player_x = 0.0
player_y = 0.0
player_z = 0.0

player_speed = 0.1
player_rotation_speed = 0.5  # Adjust the sensitivity here
mouse_sensitivity = 0.01  # Adjust the mouse sensitivity here

camera_yaw = 0.0
camera_pitch = 0.0

glViewport(0, 0, display_width, display_height)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(45, (display_width / display_height), 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

glEnable(GL_DEPTH_TEST)

def draw_cube(size, position):
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

    glBegin(GL_QUADS)
    for face in faces:
        normal = normals[faces.index(face)]
        glNormal3fv(normal)
        for vertex in face:
            glVertex3fv([vertices[vertex][0] + position[0], vertices[vertex][1] + position[1], vertices[vertex][2] + position[2]])
    glEnd()

def handle_input():
    global player_x, player_z, camera_yaw, camera_pitch

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_d]:
        player_x += player_speed
    if keys[pygame.K_w]:
        player_z -= player_speed
    if keys[pygame.K_s]:
        player_z += player_speed

    mouse_position = pygame.mouse.get_pos()
    screen_center = (display_width // 2, display_height // 2)
    mouse_movement = (mouse_position[0] - screen_center[0], mouse_position[1] - screen_center[1])

    pygame.mouse.set_pos(screen_center)  # Reset mouse position to the center of the screen

    camera_yaw += mouse_movement[0] * mouse_sensitivity  # Horizontal looking
    camera_pitch -= mouse_movement[1] * mouse_sensitivity  # Vertical looking

def update_camera():
    glLoadIdentity()
    glRotatef(-camera_pitch, 1, 0, 0)
    glRotatef(camera_yaw, 0, 1, 0)
    glTranslatef(-player_x, -player_y, -player_z)

def render_scene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    draw_cube(0.5, (0, 0, 0))
    glPopMatrix()

    pygame.display.flip()
    pygame.time.wait(10)

while True:
    handle_input()
    update_camera()
    render_scene()