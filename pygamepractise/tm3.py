import pygame
import time

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

mickey = pygame.image.load("C:\python2\week7\pygame\main-clock.png")
mickey_width, mickey_height = mickey.get_size()

clock_font = pygame.font.SysFont(None, 48)
clock_pos = (width/2, height/2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    current_time = time.localtime()
    seconds_angle = current_time.tm_sec * 6
    minutes_angle = current_time.tm_min * 6

    screen.fill((255, 255, 255))

    # draw the seconds hand
    seconds_hand = pygame.transform.rotate(mickey, seconds_angle)
    seconds_pos = (width/2 - seconds_hand.get_width()/2, height/2 - seconds_hand.get_height()/2)
    screen.blit(seconds_hand, seconds_pos)

    # draw the minutes hand
    minutes_hand = pygame.transform.rotate(mickey, minutes_angle)
    minutes_pos = (width/2 - minutes_hand.get_width()/2, height/2 - minutes_hand.get_height()/2)
    screen.blit(minutes_hand, minutes_pos)

    # draw the clock text
    clock_text = time.strftime("%H:%M:%S", current_time)
    clock_surface = clock_font.render(clock_text, True, (0, 0, 0))
    clock_rect = clock_surface.get_rect(center=clock_pos)
    screen.blit(clock_surface, clock_rect)

    pygame.display.flip()
    pygame.time.wait(1000)
