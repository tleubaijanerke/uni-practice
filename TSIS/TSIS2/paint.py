import pygame
import math
from tools import save_canvas, flood_fill, draw_preview_rect, draw_preview_circle, draw_preview_square

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint")

clock = pygame.time.Clock()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

screen.fill(WHITE)

color = BLACK
radius = 5
drawing = False
mode = "paint"
fill = False

start_pos = None
last_pos = None

font = pygame.font.SysFont(None, 30)
text = ""
text_pos = None
typing = False

running = True
while running:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = RED
            elif event.key == pygame.K_g:
                color = GREEN
            elif event.key == pygame.K_b:
                color = BLUE
            elif event.key == pygame.K_k:
                color = BLACK

            elif event.key == pygame.K_e:
                mode = "erase"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_p:
                mode = "paint"
            elif event.key == pygame.K_q:
                mode = "rect"
            elif event.key == pygame.K_o:
                mode = "square"
            elif event.key == pygame.K_t:
                mode = "right triangle"
            elif event.key == pygame.K_l:
                mode = "equilateral triangle"
            elif event.key == pygame.K_h:
                mode = "rhombus"
            elif event.key == pygame.K_d:
                mode = "line"

            elif event.key == pygame.K_u:
                mode = "fill"
            elif event.key == pygame.K_y:
                mode = "text"
            elif event.key == pygame.K_1:
                radius = 2
            elif event.key == pygame.K_2:
                radius = 5
            elif event.key == pygame.K_3:
                radius = 10

            elif event.key == pygame.K_f:
                fill = not fill

            elif event.key == pygame.K_EQUALS or event.key == pygame.K_KP_PLUS:
                radius += 1
            elif event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                radius -= 1

            elif event.key == pygame.K_x:
                screen.fill(WHITE)
            
            #(Command+S или Ctrl+S)
            elif event.key == pygame.K_s and (pygame.key.get_mods() & pygame.KMOD_META or pygame.key.get_mods() & pygame.KMOD_CTRL):
                save_canvas(screen)
            
            if typing:
                if event.key == pygame.K_RETURN:
                    img = font.render(text, True, color)
                    screen.blit(img, text_pos)
                    typing = False
                    text = ""
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                elif event.key == pygame.K_ESCAPE:
                    typing = False
                    text = ""
                else:
                    text += event.unicode
            
            radius = max(1, min(radius, 50))

        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos
            last_pos = event.pos
            canvas_copy = screen.copy()
            
            if mode == "fill":
                flood_fill(screen, event.pos[0], event.pos[1], color)
            if mode == "text":
                typing = True
                text_pos = event.pos
                text = ""

        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False

            if mode == "rect":
                x1, y1 = start_pos
                x2, y2 = event.pos
                rect = pygame.Rect(min(x1,x2), min(y1,y2), abs(x2-x1), abs(y2-y1))
                width = 0 if fill else radius
                pygame.draw.rect(screen, color, rect, width)

            elif mode == "circle":
                x1, y1 = start_pos
                x2, y2 = event.pos
                r = int(((x2-x1)**2 + (y2-y1)**2)**0.5)
                width = 0 if fill else radius
                pygame.draw.circle(screen, color, start_pos, r, width)
            
            elif mode == "square":
                x1, y1 = start_pos
                x2, y2 = event.pos
                side = min(x2-x1, y2-y1)
                if (x2-x1) < 0:
                    x = x1 - side
                else:
                    x = x1
                if (y2-y1) < 0:
                    y = y1 - side
                else:
                    y = y1
                square = pygame.Rect(x, y, side, side)
                width = 0 if fill else radius
                pygame.draw.rect(screen, color, square, width)

            elif mode == "right triangle":
                x1, y1 = start_pos
                x2, y2 = event.pos
                points = [(x1, y1), (x1, y2), (x2, y2)]
                width = 0 if fill else radius
                pygame.draw.polygon(screen, color, points, width)
            
            elif mode == "equilateral triangle":
                x1, y1 = start_pos
                x2, y2 = event.pos
                side = min(abs(x2-x1), abs(y2-y1))
                h = side * (math.sqrt(3)/2)
                if y2 >= y1:
                    p1, p2, p3 = (x1, y1), (x1 + side, y1), (x1 + side // 2, y1 - h)
                else:
                    p1, p2, p3 = (x1, y1), (x1 + side, y1), (x1 + side // 2, y1 + h)
                width = 0 if fill else radius
                pygame.draw.polygon(screen, color, [p1, p2, p3], width)

            elif mode == "rhombus":
                x1, y1 = start_pos
                x2, y2 = event.pos
                cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
                points = [(cx, y1), (x2, cy), (cx, y2), (x1, cy)]
                width = 0 if fill else radius
                pygame.draw.polygon(screen, color, points, width)
            
            elif mode == "line":
                pygame.draw.line(screen, color, start_pos, event.pos, radius)

        elif event.type == pygame.MOUSEMOTION and drawing:
            x, y = event.pos

            if mode == "paint":
                pygame.draw.line(screen, color, last_pos, (x, y), radius)
                last_pos = (x, y)

            elif mode == "erase":
                pygame.draw.line(screen, WHITE, last_pos, (x, y), radius)
                last_pos = (x, y)

            elif mode == "rect":
                screen.blit(canvas_copy, (0,0))
                x1, y1 = start_pos
                x2, y2 = event.pos
                rect = pygame.Rect(min(x1,x2), min(y1,y2), abs(x2-x1), abs(y2-y1))
                width = 0 if fill else radius
                pygame.draw.rect(screen, color, rect, width)

            elif mode == "circle":
                screen.blit(canvas_copy, (0,0))
                x1, y1 = start_pos
                x2, y2 = event.pos
                r = int(((x2-x1)**2 + (y2-y1)**2)**0.5)
                width = 0 if fill else radius
                pygame.draw.circle(screen, color, start_pos, r, width)
            
            elif mode == "square":
                screen.blit(canvas_copy, (0,0))
                x1, y1 = start_pos
                x2, y2 = event.pos
                side = min(x2-x1, y2-y1)
                if (x2-x1) < 0:
                    x = x1 - side
                else:
                    x = x1
                if (y2-y1) < 0:
                    y = y1 - side
                else:
                    y = y1
                square = pygame.Rect(x, y, side, side)
                width = 0 if fill else radius
                pygame.draw.rect(screen, color, square, width)
            
            elif mode == "right triangle":
                screen.blit(canvas_copy, (0,0))
                x1, y1 = start_pos
                x2, y2 = event.pos
                points = [(x1, y1), (x1, y2), (x2, y2)]
                width = 0 if fill else radius
                pygame.draw.polygon(screen, color, points, width)

            elif mode == "equilateral triangle":
                screen.blit(canvas_copy, (0,0))
                x1, y1 = start_pos
                x2, y2 = event.pos
                side = min(abs(x2-x1), abs(y2-y1))
                h = side * math.sqrt(3)/2
                if y2 >= y1:
                    p1, p2, p3 = (x1, y1), (x1 + side, y1), (x1 + side // 2, y1 - h)
                else:
                    p1, p2, p3 = (x1, y1), (x1 + side, y1), (x1 + side // 2, y1 + h)
                width = 0 if fill else radius
                pygame.draw.polygon(screen, color, [p1, p2, p3], width)

            elif mode == "rhombus":
                screen.blit(canvas_copy, (0,0))
                x1, y1 = start_pos
                x2, y2 = event.pos
                cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
                points = [(cx, y1), (x2, cy), (cx, y2), (x1, cy)]
                width = 0 if fill else radius
                pygame.draw.polygon(screen, color, points, width)
            
            elif mode == "line":
                screen.blit(canvas_copy, (0,0))
                pygame.draw.line(screen, color, start_pos, event.pos, radius)

    if typing and text_pos:
        img = font.render(text, True, color)
        screen.blit(img, text_pos)
        if pygame.time.get_ticks() % 1000 < 500:
            cursor_x = text_pos[0] + font.size(text)[0]
            cursor_rect = pygame.Rect(cursor_x, text_pos[1], 2, font.get_height())
            pygame.draw.rect(screen, color, cursor_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()