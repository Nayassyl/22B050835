import pygame
pygame.init()
  
color = (255,255,255)
rect_color = (255,0,0)
position = (0,0)
  
canvas = pygame.display.set_mode((500,500))
pygame.display.set_caption("Show Image")
  
image = pygame.image.load('C:\\Users\\Queen\\OneDrive\\Изображения\\Снимки экрана\\1.png')
exit = False
pygame.time.wait(5000)
while not exit:
    canvas.fill(color)
    canvas.blit(image, dest = position)
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    
    pygame.draw.rect(canvas, rect_color, pygame.Rect(30,30,60,60))
    pygame.display.update()