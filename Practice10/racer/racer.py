import pygame
import sys
import random 
from pygame.locals import *

pygame.init()
pygame.mixer.init()

# window
width = 400
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Racer")

# colours
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

# variables
score = 0
speed = 4
coins = 0
bg_y = 0

# fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Arial", 22, bold=True)
game_over = font.render("Game Over", True, black)

# images
import os

BASE_DIR = os.path.dirname(__file__)

background = pygame.transform.scale(
    pygame.image.load(os.path.join(BASE_DIR, "road.png")),
    (width, height)
)

player = pygame.transform.scale(
    pygame.image.load(os.path.join(BASE_DIR, "player.png")), (60,100)
)

enemy = pygame.transform.scale(
    pygame.image.load(os.path.join(BASE_DIR, "enemy.png")), (60,100)
)

coin = pygame.transform.scale(
    pygame.image.load(os.path.join(BASE_DIR, "coin.png")), (30,30)
)

# rect
playerrect = player.get_rect()
playerrect.center = (160,520)

enemyrect = enemy.get_rect()
enemyrect.center = (random.randint(40, width - 40), -100)

coinrect = coin.get_rect()
coinrect.center = (random.randint(40, width - 40), -200)

# speed
inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 1000)

# move
def move_player():
    pressed_keys = pygame.key.get_pressed()

    if pressed_keys[K_LEFT] and playerrect.left > 0:
        playerrect.move_ip(-5,0)

    if pressed_keys[K_RIGHT] and playerrect.right < width:
        playerrect.move_ip(5,0)

# move - enemy
def move_enemy():
    global score

    enemyrect.move_ip(0, speed)

    if enemyrect.top > height:
        score += 1
        enemyrect.center = (random.randint(40, width - 40), -100)

# move - coin
def move_coin():
    global coins

    coinrect.move_ip(0, speed-2)

    if coinrect.top > height:
        coinrect.center = (random.randint(40, width -40), -150)

    if playerrect.colliderect(coinrect):
        coins += 1
        coinrect.center = (random.randint(40, width - 40), -150)

# game
clock = pygame.time.Clock()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True

        if event.type == inc_speed:
            speed += 0.5

    # background
    bg_y += speed

    if bg_y >= height:
       bg_y = 0

    screen.blit(background, (0, bg_y))
    screen.blit(background, (0, bg_y - height))

    #text
    scoretext = font_small.render("Score: " + str(score), True, white)
    screen.blit(scoretext, (10,10))

    coin_text = font_small.render("Coins: " + str(coins), True, white)
    screen.blit(coin_text, (280,10))

    # movement
    move_player()
    move_enemy()
    move_coin()

    # screen
    screen.blit(player, playerrect)
    screen.blit(enemy, enemyrect)
    screen.blit(coin, coinrect)

    # colliderect
    if playerrect.colliderect(enemyrect):
        screen.fill(red)
        screen.blit(game_over, (30,250))
        pygame.display.update()

        pygame.time.delay(2000)
        done = True

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()