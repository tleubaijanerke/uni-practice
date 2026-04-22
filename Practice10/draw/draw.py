import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

clock = pygame.time.Clock()

# --- COLORS ---
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


# --- SETUP ---
screen.fill(WHITE)

color = BLACK
radius = 5
drawing = False
mode = "paint"
fill = False

start_pos = None
last_pos = None
canvas_copy = None

# --- COLOR PALETTE ---
colors = [BLACK, RED, GREEN, BLUE]
selected_color_index = 0

running = True

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # --- KEYBOARD ---
        elif event.type == pygame.KEYDOWN:

            # COLOR SELECTION
            if event.key == pygame.K_r:
                selected_color_index = 1
            elif event.key == pygame.K_g:
                selected_color_index = 2
            elif event.key == pygame.K_b:
                selected_color_index = 3
            elif event.key == pygame.K_k:
                selected_color_index = 0

            color = colors[selected_color_index]

            # MODES
            if event.key == pygame.K_e:
                mode = "erase"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_p:
                mode = "paint"
            elif event.key == pygame.K_q:
                mode = "rect"

            # FILL MODE
            elif event.key == pygame.K_f:
                fill = not fill

            # BRUSH SIZE
            elif event.key in [pygame.K_EQUALS, pygame.K_KP_PLUS]:
                radius += 1
            elif event.key in [pygame.K_MINUS, pygame.K_KP_MINUS]:
                radius -= 1

            # CLEAR SCREEN
            elif event.key == pygame.K_x:
                screen.fill(WHITE)

            radius = max(1, radius)

        # --- MOUSE DOWN ---
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
            last_pos = event.pos
            canvas_copy = screen.copy()

        # --- MOUSE UP ---
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False

            if mode == "rect":
                x1, y1 = start_pos
                x2, y2 = event.pos

                rect = pygame.Rect(min(x1,x2), min(y1,y2),
                                   abs(x2-x1), abs(y2-y1))

                width = 0 if fill else 2
                pygame.draw.rect(screen, color, rect, width)

            elif mode == "circle":
                x1, y1 = start_pos
                x2, y2 = event.pos

                r = int(((x2-x1)**2 + (y2-y1)**2)**0.5)
                width = 0 if fill else 2
                pygame.draw.circle(screen, color, start_pos, r, width)

        # --- DRAWING ---
        elif event.type == pygame.MOUSEMOTION and drawing:
            x, y = event.pos

            if mode == "paint":
                pygame.draw.line(screen, color, last_pos, (x, y), radius)
                last_pos = (x, y)

            elif mode == "erase":
                pygame.draw.circle(screen, WHITE, (x, y), radius * 2)

            elif mode == "rect":
                screen.blit(canvas_copy, (0,0))
                x1, y1 = start_pos
                rect = pygame.Rect(min(x1,x), min(y1,y),
                                   abs(x-x1), abs(y-y1))
                width = 0 if fill else 2
                pygame.draw.rect(screen, color, rect, width)

            elif mode == "circle":
                screen.blit(canvas_copy, (0,0))
                x1, y1 = start_pos
                r = int(((x-x1)**2 + (y-y1)**2)**0.5)
                width = 0 if fill else 2
                pygame.draw.circle(screen, color, start_pos, r, width)

    # --- UI (COLOR PALETTE) ---
    pygame.draw.rect(screen, BLACK, (10, 10, 20, 20))
    pygame.draw.rect(screen, RED, (40, 10, 20, 20))
    pygame.draw.rect(screen, GREEN, (70, 10, 20, 20))
    pygame.draw.rect(screen, BLUE, (100, 10, 20, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()