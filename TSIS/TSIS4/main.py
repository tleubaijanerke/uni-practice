import pygame
import json
import os
from db import init_db, get_top10
from game import game

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Snake Game")
font = pygame.font.SysFont("Arial", 32)
small_font = pygame.font.SysFont("Arial", 24)

init_db()

# Get the folder where this file is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SETTINGS_PATH = os.path.join(BASE_DIR, "settings.json")

# Load settings
def load_settings():
    if os.path.exists(SETTINGS_PATH):
        with open(SETTINGS_PATH, "r") as f:
            return json.load(f)
    return {"snake_color": [0,200,0], "grid_overlay": True, "sound": True}

def save_settings(settings):
    with open(SETTINGS_PATH, "w") as f:
        json.dump(settings, f, indent=4)

settings = load_settings()

def draw_button(text, y, color=(100,100,100)):
    rect = pygame.Rect(200, y, 200, 50)
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, (255,255,255), rect, 2)
    img = font.render(text, True, (255,255,255))
    screen.blit(img, (rect.x + 60, rect.y + 12))
    return rect

def input_name():
    name = ""
    while True:
        screen.fill((0,0,0))
        
        txt = font.render("Enter username:", True, (255,255,255))
        screen.blit(txt, (200, 100))
        
        name_txt = font.render(name + "_", True, (255,255,255))
        screen.blit(name_txt, (250, 180))
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and name:
                    return name
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.unicode.isprintable() and len(name) < 15:
                    name += event.unicode

def leaderboard_screen():
    data = get_top10()
    
    while True:
        screen.fill((0,0,0))
        
        title = font.render("LEADERBOARD", True, (255,255,0))
        screen.blit(title, (200, 30))
        
        y = 90
        for i, row in enumerate(data[:10]):
            text = f"{i+1}. {row[0]}  {row[1]} pts  Lvl:{row[2]}"
            img = small_font.render(text, True, (255,255,255))
            screen.blit(img, (50, y))
            y += 30
        
        back_btn = pygame.Rect(200, 350, 200, 40)
        pygame.draw.rect(screen, (100,100,100), back_btn)
        screen.blit(font.render("BACK", True, (255,255,255)), (270, 355))
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_btn.collidepoint(event.pos):
                    return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return

def settings_screen():
    global settings
    
    snake_colors = [
        (0,200,0),   # Green
        (255,0,0),   # Red
        (0,0,255),   # Blue
        (255,255,0), # Yellow
        (255,165,0), # Orange
    ]
    color_names = ["Green", "Red", "Blue", "Yellow", "Orange"]
    
    color_index = 0
    for i, c in enumerate(snake_colors):
        if list(c) == settings["snake_color"]:
            color_index = i
            break
    
    while True:
        screen.fill((0,0,0))
        
        title = font.render("SETTINGS", True, (255,255,0))
        screen.blit(title, (230, 30))
        
        # Grid toggle
        grid_text = f"Grid: {'ON' if settings['grid_overlay'] else 'OFF'}"
        grid_rect = pygame.Rect(200, 120, 200, 40)
        pygame.draw.rect(screen, (0,100,0), grid_rect)
        screen.blit(font.render(grid_text, True, (255,255,255)), (230, 128))
        
        # Color selection
        color_rect = pygame.Rect(200, 190, 200, 40)
        pygame.draw.rect(screen, (0,100,0), color_rect)
        screen.blit(font.render(f"Color: {color_names[color_index]}", True, (255,255,255)), (230, 198))
        
        # Color preview
        preview = pygame.Rect(420, 195, 30, 30)
        pygame.draw.rect(screen, snake_colors[color_index], preview)
        pygame.draw.rect(screen, (255,255,255), preview, 2)
        
        # Left/Right arrows
        left_arrow = pygame.Rect(160, 195, 30, 30)
        right_arrow = pygame.Rect(460, 195, 30, 30)
        pygame.draw.rect(screen, (100,100,100), left_arrow)
        pygame.draw.rect(screen, (100,100,100), right_arrow)
        screen.blit(small_font.render("<", True, (255,255,255)), (170, 200))
        screen.blit(small_font.render(">", True, (255,255,255)), (470, 200))
        
        # Save & Back button
        save_rect = pygame.Rect(200, 280, 200, 50)
        pygame.draw.rect(screen, (0,0,150), save_rect)
        screen.blit(font.render("SAVE & BACK", True, (255,255,255)), (220, 290))
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if grid_rect.collidepoint(event.pos):
                    settings["grid_overlay"] = not settings["grid_overlay"]
                elif left_arrow.collidepoint(event.pos):
                    color_index = (color_index - 1) % len(snake_colors)
                    settings["snake_color"] = list(snake_colors[color_index])
                elif right_arrow.collidepoint(event.pos):
                    color_index = (color_index + 1) % len(snake_colors)
                    settings["snake_color"] = list(snake_colors[color_index])
                elif save_rect.collidepoint(event.pos):
                    save_settings(settings)
                    return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return

def main_menu():
    username = input_name()
    if username is None:
        return
    
    while True:
        screen.fill((0,0,0))
        
        play_btn = draw_button("PLAY", 100, (0,100,0))
        lb_btn = draw_button("LEADERBOARD", 170, (0,100,0))
        set_btn = draw_button("SETTINGS", 240, (0,100,0))
        quit_btn = draw_button("QUIT", 310, (100,0,0))
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_btn.collidepoint(event.pos):
                    game(screen, username, settings)
                elif lb_btn.collidepoint(event.pos):
                    leaderboard_screen()
                elif set_btn.collidepoint(event.pos):
                    settings_screen()
                elif quit_btn.collidepoint(event.pos):
                    return

if __name__ == "__main__":
    main_menu()