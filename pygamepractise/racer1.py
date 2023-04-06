import pygame , sys
import random, time

from pygame.locals import *
pygame.init()



color_black = pygame.Color(0, 0, 0)         # Black
color_white = pygame.Color(255, 255, 255)   # White
color_grey = pygame.Color(128, 128, 128)   # Grey
color_red = pygame.Color(255, 0, 0)       # Red
color_green = pygame.Color(0, 255, 0)      #Green

clock = pygame.time.Clock()

screen_w, screen_h = 400, 600
speed = 5
score = 0

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, color_black )

background = pygame.image.load("C:\python2\pygamepractise\AnimatedStreet.png")



screen = pygame.display.set_mode((400, 600))
screen.fill(color_white)
pygame.display.set_caption("Game")



class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:\python2\pygamepractise\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, screen_w - 40), 0)

    def move(self):
        global score
        self.rect.move_ip(0,speed)
        if (self.rect.top > 600):
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, screen_w - 40), 0)





class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:\python2\pygamepractise\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < screen_w:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
    


p1 = Player()
e1 = Enemy()


enemies = pygame.sprite.Group()
enemies.add(e1)
all_sprites = pygame.sprite.Group()
all_sprites.add(e1)
all_sprites.add(p1)

inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 1000)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == inc_speed:
            speed += 0.5

    screen.blit(background, (0, 0))
    scores = font_small.render(str(score), True, color_black)
    screen.blit(scores, (10, 10))

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    if pygame.sprite.spritecollideany(p1, enemies):
        pygame.mixer.Sound('C:\python2\pygamepractise\crash.wav').play()
        time.sleep(0.5)

        screen.fill(color_red)
        screen.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    clock.tick(60)