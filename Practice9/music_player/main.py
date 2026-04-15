import pygame
from player import MusicPlayer

pygame.init()

WIDTH, HEIGHT = 700, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

clock = pygame.time.Clock()

#fonts
font_small = pygame.font.SysFont("Arial", 18)
font_big = pygame.font.SysFont("Arial", 24, bold=True)

player = MusicPlayer()

running = True

while running:
    screen.fill((18, 18, 28))  # dark background (nice aesthetic)

    # ---- "card" background ----
    pygame.draw.rect(screen, (30, 30, 45), (40, 60, 620, 250), border_radius=15)

    # ---- title ----
    title = font_big.render("🎵 Music Player", True, (255, 255, 255))
    screen.blit(title, (60, 80))

    # ---- controls ----
    controls = font_small.render(
        "P Play | S Stop | N Next | B Back | Q Quit",
        True,
        (180, 180, 180)
    )
    screen.blit(controls, (60, 130))

    # ---- current track ----
    track_name = font_big.render(
        "Now Playing: " + player.get_track_name(),
        True,
        (0, 200, 255)
    )
    screen.blit(track_name, (60, 180))

    # ---- hint ----
    hint = font_small.render(
        "Use keyboard to control playback",
        True,
        (120, 120, 120)
    )
    screen.blit(hint, (60, 230))

    # ---- events ----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_p:
                player.play()

            if event.key == pygame.K_s:
                player.stop()

            if event.key == pygame.K_n:
                player.next()

            if event.key == pygame.K_b:
                player.back()

            if event.key == pygame.K_q:
                running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()