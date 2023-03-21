import pygame
import time

pygame.init()

# Set up the clock display window
screen = pygame.display.set_mode((200, 100))
pygame.display.set_caption("Pygame Clock")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up font
font = pygame.font.Font(None, 36)

# Run the clock
while True:
    # Get the current time
    current_time = time.strftime("%M:%S")

    # Clear the display
    screen.fill(WHITE)

    # Render the time
    text = font.render(current_time, True, BLACK)
    text_rect = text.get_rect(center=(100, 50))
    screen.blit(text, text_rect)

    # Update the display
    pygame.display.update()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
