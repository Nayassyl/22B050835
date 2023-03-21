import pygame
import time

# Initialize Pygame
pygame.init()

# Set up the window and clock
WINDOW_SIZE = (830,830)
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Mickey Mouse Clock")
clock = pygame.time.Clock()
mickey = pygame.image.load("C:\python2\pygamepractise\main-clock.png")
mickey_width, mickey_height = mickey.get_size()

# Load the images for Mickey's hands
minute_hand = pygame.image.load("C:\\python2\\pygamepractise\\righthand.png")
second_hand = pygame.image.load("C:\python2\pygamepractise\lefthand.png")

# Set the starting position for Mickey's hands
minute_hand_pos = (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2)
second_hand_pos = (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2)

exit = False
while not exit:
    # Get the current time
    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    # Calculate the angle for Mickey's hands
    minute_angle = (minutes / 60) * 360
    second_angle = (seconds / 60) * 360

    # Rotate Mickey's hands to the correct angle
    minute_hand_rotated = pygame.transform.rotate(minute_hand, 90-minute_angle)
    second_hand_rotated = pygame.transform.rotate(second_hand, 90-second_angle)

    # Update the position of Mickey's hands based on the angle
    minute_hand_pos = (WINDOW_SIZE[0] // 2 - minute_hand_rotated.get_width() // 2,
                       WINDOW_SIZE[1] // 2 - minute_hand_rotated.get_height() // 2)
    second_hand_pos = (WINDOW_SIZE[0] // 2 - second_hand_rotated.get_width() // 2,
                       WINDOW_SIZE[1] // 2 - second_hand_rotated.get_height() // 2)

    # Clear the window
    window.fill((255, 255, 255))

    # Draw Mickey's hands on the window
    window.blit(mickey, (0,0))
    window.blit(minute_hand_rotated, minute_hand_pos)
    window.blit(second_hand_rotated, second_hand_pos)

    pygame.display.flip()
    pygame.time.wait(1000)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
