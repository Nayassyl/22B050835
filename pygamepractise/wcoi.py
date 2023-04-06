import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Set the width and height of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define the player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = SCREEN_HEIGHT // 2
        self.speed = 0

    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > SCREEN_HEIGHT - self.rect.height:
            self.rect.y = SCREEN_HEIGHT - self.rect.height

    def move_up(self):
        self.speed = -5

    def move_down(self):
        self.speed = 5

    def stop(self):
        self.speed = 0

# Define the coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([25, 25])
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)

    def update(self):
        self.rect.x -= 5
        if self.rect.right < 0:
            self.kill()

# Define the enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 50])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)

    def update(self):
        self.rect.x -= 8
        if self.rect.right < 0:
            self.kill()

# Initialize Pygame
pygame.init()

# Set the screen size
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# Set the game caption
pygame.display.set_caption('Races Game')

# Create the player
player = Player()

# Create a sprite group for the coins
coin_group = pygame.sprite.Group()

# Create a sprite group for the enemies
enemy_group = pygame.sprite.Group()

# Set the starting scores
coin_score = 0
enemy_score = 0

# Set the fonts for the score trackers
font = pygame.font.Font(None, 36)
coin_font = pygame.font.Font(None, 24)
enemy_font = pygame.font.Font(None, 24)

# Set the clock for the game
clock = pygame.time.Clock()

# Loop until the user clicks the close button
done = False

while not done:
    # --- Event processing ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move_up()
            elif event.key == pygame.K_DOWN:
                player.move_down()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player.stop()

    # --- Game logic ---
    # Create
