import pygame
import random
import sys

pygame.init()

# window
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

# colours
white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
green = (0,200,0)
blue = (50,153,213)

# font
font = pygame.font.SysFont("Arial", 25, bold=True)

# snake
snake_block = 10
snake_speed = 10

# score
score = 0
level = 1

# coordinates
x = WIDTH // 2
y = HEIGHT // 2

x_change = 0
y_change = 0

snake_body = []
length = 1

# food
foodx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0


# food
def generate_food():
    while True:
        fx = round(random.randrange(0, WIDTH - snake_block) / 10.0) * 10.0
        fy = round(random.randrange(0, HEIGHT - snake_block) / 10.0) * 10.0

        if [fx, fy] not in snake_body:
            return fx, fy


# loop
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # control
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

    # movement
    x += x_change
    y += y_change

    # WALL COLLISION 
    if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
        running = False

    # food
    if x == foodx and y == foody:
        foodx, foody = generate_food()
        length += 1
        score += 1

        # levels
        if score % 3 == 0:
            level += 1
            snake_speed += 2   # ускорение

    # snake's body
    head = [x, y]
    snake_body.append(head)

    if len(snake_body) > length:
        del snake_body[0]

    # confrontation with yourself
    for block in snake_body[:-1]:
        if block == head:
            running = False

    # screen
    screen.fill(blue)

    # food
    pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])

    # snake
    for block in snake_body:
        pygame.draw.rect(screen, green, [block[0], block[1], snake_block, snake_block])

    # text (score + level)
    score_text = font.render(f"Score: {score}", True, white)
    level_text = font.render(f"Level: {level}", True, white)

    screen.blit(score_text, (10,10))
    screen.blit(level_text, (WIDTH - 120, 10))

    pygame.display.update()

    clock.tick(snake_speed)

pygame.quit()
sys.exit()