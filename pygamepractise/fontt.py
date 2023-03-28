import pygame
pygame.init()
screen = pygame.display.set_mode((500 ,500))
clock = pygame.time.Clock()
exit = False

font = pygame.font.Font("C:\\python2\\fonts\\Dihil.ttf", 50)
text = font.render("Hello Frodo!", True , (255,255,255))

while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            exit = True

    screen.fill((0,0,0))
    screen.blit(text, (250 - text.get_width() // 2, 250 - text.get_height() // 2))
    pygame.display.flip()
        
        