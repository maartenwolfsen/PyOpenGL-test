import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Initialize Pygame
pygame.init()

# Set up the display
display_width = 800
display_height = 600
pygame.display.set_mode((display_width, display_height), DOUBLEBUF | OPENGL)

# Set up the initial position of the player
player_x = 0.0
player_y = 0.0
player_z = 0.0

# Set up the initial movement speed of the player
player_speed = 0.1

# Set the initial viewport and initialize the model view matrix
glViewport(0, 0, display_width, display_height)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(45, (display_width / display_height), 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

# Enable lighting and set up light sources
glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)
glLightfv(GL_LIGHT0, GL_POSITION, [1.0, 1.0, 1.0, 0.0])
glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 1.0])
glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])

# Enable depth testing
glEnable(GL_DEPTH_TEST)

# Set up the material properties of the cube
glMaterialfv(GL_FRONT, GL_AMBIENT, [0.2, 0.2, 0.2, 1.0])
glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.8, 0.8, 0.8, 1.0])
glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
glMaterialfv(GL_FRONT, GL_SHININESS, 50.0)


# Define the cube drawing function
def draw_cube(size):
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
            glVertex3fv(vertices[vertex])
    glEnd()


# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Get the state of the keyboard
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_d]:
        player_x += player_speed
    if keys[pygame.K_w]:
        player_z -= player_speed
    if keys[pygame.K_s]:
        player_z += player_speed

    # Clear the screen and depth buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Set up the player's view
    glLoadIdentity()
    gluLookAt(0.0, 0.0, 10.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    # Render the cube
    glPushMatrix()
    glTranslatef(player_x, player_y, player_z)
    draw_cube(0.5)
    glPopMatrix()

    # Update the display
    pygame.display.flip()
    pygame.time.wait(10)
