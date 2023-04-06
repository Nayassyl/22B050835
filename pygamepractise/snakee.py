import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 600
window_height = 400
game_display = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Snake Game')

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set up the clock
clock = pygame.time.Clock()

# Define the snake
snake_block_size = 10
snake_speed = 15
font_style = pygame.font.SysFont(None, 50)

def message(msg, color):
    message = font_style.render(msg, True, color)
    game_display.blit(message, [window_width/6, window_height/3])

def gameLoop():
    game_over = False
    game_close = False

    # Set the initial position of the snake
    x1 = window_width / 2
    y1 = window_height / 2
    x1_change = 0
    y1_change = 0

    # Set up the food
    foodx = round(random.randrange(0, window_width - snake_block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, window_height - snake_block_size) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            game_display.fill(white)
            message("You lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block_size
                    x1_change = 0

        # Update the position of the snake
        x1 += x1_change
        y1 += y1_change

        # Draw the snake and the food
        game_display.fill(white)
        pygame.draw.rect(game_display, black, [x1, y1, snake_block_size, snake_block_size])
        pygame.draw.rect(game_display, red, [foodx, foody, snake_block_size, snake_block_size])
        pygame.display.update()

        # Check if the snake has hit the boundaries or itself
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_close = True
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, window_width - snake_block_size) / 10.0) * 10.0
            foody
