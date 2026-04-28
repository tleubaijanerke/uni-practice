import pygame
import random
import time

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

# Snake settings
snake_block = 20
snake_speed = 10

# Font
font = pygame.font.SysFont(None, 30)

# Function to draw snake
def draw_snake(snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], snake_block, snake_block])

# Function to show score
def show_score(score):
    value = font.render(f"Score: {score}", True, WHITE)
    screen.blit(value, [10, 10])

# Game loop
def game():
    game_over = False

    # Snake starting position
    x = WIDTH // 2
    y = HEIGHT // 2

    x_change = 0
    y_change = 0

    snake_list = []
    snake_length = 1

    score = 0

    # Food settings
    food_x = random.randrange(0, WIDTH - snake_block, snake_block)
    food_y = random.randrange(0, HEIGHT - snake_block, snake_block)

    # Food weight (points)
    food_value = random.choice([1, 2, 5])

    # Timer for food disappearing
    food_spawn_time = time.time()
    FOOD_LIFETIME = 5  # seconds

    while not game_over:
        screen.fill(BLACK)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        # Move snake
        x += x_change
        y += y_change

        # Game over if hitting wall
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            game_over = True

        # Snake body
        snake_head = [x, y]
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        # Collision with itself
        for block in snake_list[:-1]:
            if block == snake_head:
                game_over = True

        # Food timer (disappears after time)
        current_time = time.time()
        if current_time - food_spawn_time > FOOD_LIFETIME:
            # Respawn food
            food_x = random.randrange(0, WIDTH - snake_block, snake_block)
            food_y = random.randrange(0, HEIGHT - snake_block, snake_block)
            food_value = random.choice([1, 2, 5])
            food_spawn_time = time.time()

        # Draw food (color depends on value)
        if food_value == 1:
            food_color = WHITE
        elif food_value == 2:
            food_color = GREEN
        else:
            food_color = RED

        pygame.draw.rect(screen, food_color, [food_x, food_y, snake_block, snake_block])

        # Check if snake eats food
        if x == food_x and y == food_y:
            score += food_value
            snake_length += 1

            # New food
            food_x = random.randrange(0, WIDTH - snake_block, snake_block)
            food_y = random.randrange(0, HEIGHT - snake_block, snake_block)
            food_value = random.choice([1, 2, 5])
            food_spawn_time = time.time()

        # Draw snake
        draw_snake(snake_list)

        # Draw score
        show_score(score)

        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()

# Run game
game()