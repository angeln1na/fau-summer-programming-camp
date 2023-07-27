import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
width = 500
height = 500
window_size = (width, height)

# Set up the window
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Single Background Color")

# Set the background color
background_color = (100, 150, 200)  # RGB values for the color

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the window with the background color
    window.fill(background_color)

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()