import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

clock = pygame.time.Clock()
FPS = 60

import os

# Get current file directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

player_img = pygame.image.load(os.path.join(BASE_DIR, "player.png"))
enemy_img = pygame.image.load(os.path.join(BASE_DIR, "enemy.png"))
road_img = pygame.image.load(os.path.join(BASE_DIR, "road.png"))
coin_img = pygame.image.load(os.path.join(BASE_DIR, "coin.png"))

# Resize images if needed
player_img = pygame.transform.scale(player_img, (50, 80))
enemy_img = pygame.transform.scale(enemy_img, (50, 80))
coin_img = pygame.transform.scale(coin_img, (30, 30))

# Player settings
player_x = WIDTH // 2 - 25
player_y = HEIGHT - 100
player_speed = 5

# Enemy settings
enemy_x = random.randint(0, WIDTH - 50)
enemy_y = -100
enemy_speed = 5

# Coin settings
coin_x = random.randint(0, WIDTH - 30)
coin_y = -50
coin_speed = 4

# Coin weight (random value)
coin_value = random.choice([1, 2, 5])

# Score
score = 0

# Speed increase condition
SPEED_INCREASE_SCORE = 10

# Font
font = pygame.font.SysFont(None, 30)

# Game loop
running = True
while running:
    screen.blit(road_img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - 50:
        player_x += player_speed

    # Enemy movement
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = -100
        enemy_x = random.randint(0, WIDTH - 50)

    # Coin movement
    coin_y += coin_speed
    if coin_y > HEIGHT:
        coin_y = -50
        coin_x = random.randint(0, WIDTH - 30)
        coin_value = random.choice([1, 2, 5])  # new weight

    # Collision (player & enemy)
    player_rect = pygame.Rect(player_x, player_y, 50, 80)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, 50, 80)

    if player_rect.colliderect(enemy_rect):
        print("Game Over")
        running = False

    # Collision (player & coin)
    coin_rect = pygame.Rect(coin_x, coin_y, 30, 30)

    if player_rect.colliderect(coin_rect):
        score += coin_value  # add weight
        coin_y = -50
        coin_x = random.randint(0, WIDTH - 30)
        coin_value = random.choice([1, 2, 5])

    # Increase difficulty
    if score >= SPEED_INCREASE_SCORE:
        enemy_speed = 8
    if score >= SPEED_INCREASE_SCORE * 2:
        enemy_speed = 12

    # Draw objects
    screen.blit(player_img, (player_x, player_y))
    screen.blit(enemy_img, (enemy_x, enemy_y))
    screen.blit(coin_img, (coin_x, coin_y))

    # Draw score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()