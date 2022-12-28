import pygame
import math

# Set the width and height of the window
width, height = 640, 480

# Initialize pygame
pygame.init()

# Set the window caption
pygame.display.set_caption("Animated 3D Cube")

# Create a clock to control the frame rate
clock = pygame.time.Clock()

# Set the background color to black
screen = pygame.display.set_mode((width, height))

# Define the vertices of the cube in 3D space
vertices = [
    (1, 1, 1),
    (1, -1, 1),
    (-1, -1, 1),
    (-1, 1, 1),
    (1, 1, -1),
    (1, -1, -1),
    (-1, -1, -1),
    (-1, 1, -1)
]
vertices = [(x * 0.5, y * 0.5, z * 0.5) for x, y, z in vertices]
# Define the edges of the cube
edges = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (4, 5),
    (5, 6),
    (6, 7),
    (7, 4),
    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7)
]

# Set the field of view and the distance from the camera to the origin
fov = math.pi / 4
camera_distance = 5

# Set the rotation angles for the cube
x_angle, y_angle = 0, 0

# Set the animation loop to run indefinitely
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Clear the screen
    screen.fill((40, 0, 0))
    color = (255, 0, 0)

    # Update the rotation angles
    x_angle += 0.1
    y_angle += 0.1

    # Rotate the vertices of the cube
    rotated_vertices = []
    for vertex in vertices:
        x, y, z = vertex
        # Rotate the point around the X axis
        rotated_y = y * math.cos(x_angle) - z * math.sin(x_angle)
        rotated_z = y * math.sin(x_angle) + z * math.cos(x_angle)
        y, z = rotated_y, rotated_z
        # Rotate the point around the Y axis
        rotated_x = x * math.cos(y_angle) - z * math.sin(y_angle)
        rotated_z = x * math.sin(y_angle) + z * math.cos(y_angle)
        x, z = rotated_x, rotated_z
        # vertices = [(x * 0.5, y * 0.5, z * 0.5) for x, y, z in vertices]
        # Add the rotated point to the list of rotated vertices
        rotated_vertices.append((x, y, z))

    # Project the vertices onto the 2D screen
    projected_vertices = []
    for vertex in rotated_vertices:
        x, y, z = vertex
        # Calculate the perspective projection
        perspective = camera_distance / (camera_distance - z)
        x = x * perspective
        y = y * perspective
        # Add the projected point to the list of projected vertices
        projected_vertices.append((int(x * width / 2 + width / 2), int(y * height / 2 + height / 2)))

    # Draw the edges of the cube
    for edge in edges:
        point1, point2 = edge
        pygame.draw.line(screen, (255, 255, 255), projected_vertices[point1], projected_vertices[point2])

    # Update the display
    pygame.display.flip()

    # Limit the frame rate to 60 FPS
    clock.tick(15)
