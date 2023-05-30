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

# Set up the perspective
gluPerspective(45, (display_width / display_height), 0.1, 50.0)

# Set up the initial position of the player
player_x = 0.0
player_y = 0.0
player_z = 0.0

# Set up the initial movement speed of the player
player_speed = 0.1

# Set the initial viewport and initialize the model view matrix
glViewport(0, 0, display_width, display_height)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

# Enable lighting and set up a light source
glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)
glLightfv(GL_LIGHT0, GL_POSITION, [1.0, 1.0, 1.0, 0.0])
glLightfv(GL_LIGHT0, GL_AMBIENT, [0.5, 0.5, 0.5, 1.0])
glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])

# Enable depth testing
glEnable(GL_DEPTH_TEST)

# Main game loop
while True:
    # Clear the screen and depth buffer
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

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

    # Limit the player's position to within the screen boundaries
    if player_x < -display_width / 2:
        player_x = -display_width / 2
    elif player_x > display_width / 2:
        player_x = display_width / 2

    # Set up the player's view
    glLoadIdentity()
    gluLookAt(0.0, 0.0, 0.0, 0.0, 0.0, -1.0, 0.0, 1.0, 0.0)

    # Calculate the distance from the light source to the cube
    distance_to_light = abs(player_z) + 0.1  # Adjust the parameters to control the transition

    # Calculate the interpolated color
    start_color = [1.0, 0.0, 0.0]  # Red
    end_color = [0.0, 0.0, 0.0]  # Black
    interpolated_color = [start + (end - start) * distance_to_light for start, end in zip(start_color, end_color)]

    # Set up the material properties
    glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, interpolated_color)
    glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
    glMaterialfv(GL_FRONT, GL_SHININESS, 50.0)

    # Render the player cube
    cube_size = 0.5 + abs(player_z) * 0.01  # Adjust the parameters to control the scaling
    half_width = cube_size / 2.0
    glTranslatef(player_x, player_y, player_z)
    glScalef(cube_size, cube_size, cube_size)  # Scale the cube based on z-value
    glBegin(GL_QUADS)
    # Front face
    glNormal3f(0.0, 0.0, 1.0)
    glVertex3f(-half_width, -half_width, half_width)
    glVertex3f(half_width, -half_width, half_width)
    glVertex3f(half_width, half_width, half_width)
    glVertex3f(-half_width, half_width, half_width)
    glEnd()
    glScalef(1.0 / cube_size, 1.0 / cube_size, 1.0 / cube_size)  # Restore the scale
    glTranslatef(-player_x, -player_y, -player_z)

    # Update the display
    pygame.display.flip()
    pygame.time.wait(10)
