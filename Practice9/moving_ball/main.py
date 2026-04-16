import pygame
import sys
from ball import Ball

pygame.init()

# display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Red Ball")

clock = pygame.time.Clock()

# creating the ball
ball = Ball(WIDTH // 2, HEIGHT // 2)

# game
running = True
while running:
    clock.tick(60)  # 60 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # keystroke movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ball.move(-ball.speed, 0, WIDTH, HEIGHT)
            if event.key == pygame.K_RIGHT:
                ball.move(ball.speed, 0, WIDTH, HEIGHT)
            if event.key == pygame.K_UP:
                ball.move(0, -ball.speed, WIDTH, HEIGHT)
            if event.key == pygame.K_DOWN:
                ball.move(0, ball.speed, WIDTH, HEIGHT)

    #screen
    screen.fill((255, 255, 255))

    #draw the ball
    ball.draw(screen)

    pygame.display.update()