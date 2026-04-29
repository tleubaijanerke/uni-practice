import pygame
import random
import os
import sys
from racer import Player, Enemy, Coin, Obstacle, PowerUp
from persistence import load_settings, save_settings, load_leaderboard, save_leaderboard, add_score
from ui import Button, TextInput

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")
clock = pygame.time.Clock()
FPS = 60

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

# Load images
player_img = pygame.image.load(os.path.join(ASSETS_DIR, "player.png"))
player_img = pygame.transform.scale(player_img, (40, 60))

enemy_img = pygame.image.load(os.path.join(ASSETS_DIR, "enemy.png"))
enemy_img = pygame.transform.scale(enemy_img, (40, 60))

coin_img = pygame.image.load(os.path.join(ASSETS_DIR, "coin.png"))
coin_img = pygame.transform.scale(coin_img, (20, 20))

nitro_img = pygame.image.load(os.path.join(ASSETS_DIR, "nitro.png"))
nitro_img = pygame.transform.scale(nitro_img, (25, 25))

shield_img = pygame.image.load(os.path.join(ASSETS_DIR, "shield.png"))
shield_img = pygame.transform.scale(shield_img, (25, 25))

repair_img = pygame.image.load(os.path.join(ASSETS_DIR, "repair.png"))
repair_img = pygame.transform.scale(repair_img, (25, 25))

obstacle_img = pygame.image.load(os.path.join(ASSETS_DIR, "obstacle.png"))
obstacle_img = pygame.transform.scale(obstacle_img, (30, 30))

road_img = pygame.image.load(os.path.join(ASSETS_DIR, "road.png"))
road_img = pygame.transform.scale(road_img, (WIDTH, HEIGHT))

# Game objects
player = Player(WIDTH // 2 - 20, HEIGHT - 80, player_img)
enemies = []
coins = []
obstacles = []
powerups = []

# Score
score = 0
distance = 0
coins_collected = 0

# Spawn timers
enemy_timer = 0
coin_timer = 0
obstacle_timer = 0
powerup_timer = 0

# Load settings
settings = load_settings()
difficulty = settings["difficulty"]

if difficulty == "easy":
    enemy_speed = 3
    spawn_delay = 90
elif difficulty == "medium":
    enemy_speed = 5
    spawn_delay = 60
else:
    enemy_speed = 7
    spawn_delay = 40

current_enemy_speed = enemy_speed

# Game state
game_state = "menu"
username = ""
final_score = 0
final_distance = 0
final_coins = 0

# Leaderboard
leaderboard = load_leaderboard()

# UI elements
username_input = TextInput(100, 300, 200, 40)

play_btn = Button(100, 250, 200, 50, "PLAY", (0,100,0), (0,200,0))
leaderboard_btn = Button(100, 320, 200, 50, "LEADERBOARD", (0,100,0), (0,200,0))
settings_btn = Button(100, 390, 200, 50, "SETTINGS", (0,100,0), (0,200,0))
quit_btn = Button(100, 460, 200, 50, "QUIT", (100,0,0), (200,0,0))
back_btn = Button(100, 500, 200, 40, "BACK", (100,100,100), (150,150,150))
retry_btn = Button(60, 500, 130, 40, "RETRY", (0,100,0), (0,200,0))
menu_btn = Button(210, 500, 130, 40, "MENU", (0,100,0), (0,200,0))

easy_btn = Button(50, 350, 90, 40, "EASY", (0,150,0) if difficulty == "easy" else (100,100,100), (0,200,0))
medium_btn = Button(155, 350, 90, 40, "MEDIUM", (0,150,0) if difficulty == "medium" else (100,100,100), (0,200,0))
hard_btn = Button(260, 350, 90, 40, "HARD", (0,150,0) if difficulty == "hard" else (100,100,100), (0,200,0))

# Fonts
font_large = pygame.font.SysFont("Arial", 48)
font_medium = pygame.font.SysFont("Arial", 32)
font_small = pygame.font.SysFont("Arial", 20)

def reset_game():
    global player, enemies, coins, obstacles, powerups
    global score, distance, coins_collected, current_enemy_speed
    global enemy_timer, coin_timer, obstacle_timer, powerup_timer
    
    player = Player(WIDTH // 2 - 20, HEIGHT - 80, player_img)
    enemies = []
    coins = []
    obstacles = []
    powerups = []
    score = 0
    distance = 0
    coins_collected = 0
    current_enemy_speed = enemy_speed
    enemy_timer = 0
    coin_timer = 0
    obstacle_timer = 0
    powerup_timer = 0

def spawn_enemy():
    global enemy_timer
    if enemy_timer <= 0:
        x = random.randint(0, WIDTH - 40)
        enemies.append(Enemy(x, -60, current_enemy_speed, enemy_img))
        enemy_timer = spawn_delay

def spawn_coin():
    global coin_timer
    if coin_timer <= 0:
        x = random.randint(0, WIDTH - 20)
        value = random.choice([1, 2, 5])
        coins.append(Coin(x, -20, value, coin_img))
        coin_timer = random.randint(30, 60)

def spawn_obstacle():
    global obstacle_timer
    if obstacle_timer <= 0 and distance > 500:
        x = random.randint(0, WIDTH - 30)
        typ = random.choice(["oil", "pothole", "barrier"])
        obstacles.append(Obstacle(x, -30, typ, obstacle_img))
        obstacle_timer = random.randint(120, 200)

def spawn_powerup():
    global powerup_timer
    if powerup_timer <= 0 and distance > 300:
        x = random.randint(0, WIDTH - 25)
        typ = random.choice(["nitro", "shield", "repair"])
        if typ == "nitro":
            powerups.append(PowerUp(x, -25, typ, nitro_img))
        elif typ == "shield":
            powerups.append(PowerUp(x, -25, typ, shield_img))
        else:
            powerups.append(PowerUp(x, -25, typ, repair_img))
        powerup_timer = random.randint(400, 800)

def update_game():
    global score, distance, coins_collected, current_enemy_speed
    global enemy_timer, coin_timer, obstacle_timer, powerup_timer
    
    player.update()
    
    enemy_timer -= 1
    coin_timer -= 1
    obstacle_timer -= 1
    powerup_timer -= 1
    
    spawn_enemy()
    spawn_coin()
    spawn_obstacle()
    spawn_powerup()
    
    for e in enemies[:]:
        e.update()
        if e.y > HEIGHT:
            enemies.remove(e)
        
        if player.get_rect().colliderect(e.get_rect()):
            if player.shield_active:
                enemies.remove(e)
                player.shield_active = False
            else:
                return True
    
    for c in coins[:]:
        c.update()
        if c.y > HEIGHT:
            coins.remove(c)
        
        if player.get_rect().colliderect(c.get_rect()):
            score += c.value
            coins_collected += c.value
            coins.remove(c)
    
    for o in obstacles[:]:
        o.update()
        if o.y > HEIGHT:
            obstacles.remove(o)
        
        if player.get_rect().colliderect(o.get_rect()):
            if o.type == "oil":
                current_enemy_speed = max(2, current_enemy_speed - 2)
            elif o.type == "pothole":
                score = max(0, score - 50)
            elif o.type == "barrier":
                if player.shield_active:
                    player.shield_active = False
                else:
                    return True
            obstacles.remove(o)
    
    for p in powerups[:]:
        p.update()
        if not p.is_alive():
            powerups.remove(p)
        
        if player.get_rect().colliderect(p.get_rect()):
            if p.type == "nitro":
                player.nitro_active = True
                player.nitro_timer = 180
                current_enemy_speed = enemy_speed + 3
            elif p.type == "shield":
                player.shield_active = True
                player.shield_timer = 180
            powerups.remove(p)
    
    distance += current_enemy_speed
    score += int(current_enemy_speed)
    
    if distance > 2000:
        current_enemy_speed = enemy_speed + 3
    elif distance > 1000:
        current_enemy_speed = enemy_speed + 2
    elif distance > 500:
        current_enemy_speed = enemy_speed + 1
    
    return False

def draw_game():
    screen.blit(road_img, (0, 0))
    
    for c in coins:
        c.draw(screen)
    for o in obstacles:
        o.draw(screen)
    for p in powerups:
        p.draw(screen)
    for e in enemies:
        e.draw(screen)
    
    player.draw(screen)
    
    score_text = font_small.render(f"Score: {score}", True, (255,255,255))
    coin_text = font_small.render(f"Coins: {coins_collected}", True, (255,215,0))
    dist_text = font_small.render(f"Distance: {int(distance)}", True, (255,255,255))
    
    screen.blit(score_text, (10, 10))
    screen.blit(coin_text, (10, 35))
    screen.blit(dist_text, (10, 60))
    
    y = 90
    if player.nitro_active:
        nitro_text = font_small.render(f"NITRO: {player.nitro_timer//60}s", True, (255,0,0))
        screen.blit(nitro_text, (10, y))
        y += 25
    if player.shield_active:
        shield_text = font_small.render(f"SHIELD: {player.shield_timer//60}s", True, (0,255,255))
        screen.blit(shield_text, (10, y))

def draw_menu():
    screen.fill((0,0,0))
    title = font_large.render("RACER GAME", True, (255,255,0))
    screen.blit(title, (WIDTH//2 - title.get_width()//2, 100))
    play_btn.draw(screen)
    leaderboard_btn.draw(screen)
    settings_btn.draw(screen)
    quit_btn.draw(screen)

def draw_username():
    screen.fill((0,0,0))
    prompt = font_medium.render("Enter your name:", True, (255,255,255))
    screen.blit(prompt, (WIDTH//2 - prompt.get_width()//2, 250))
    username_input.draw(screen)
    hint = font_small.render("Press ENTER to start", True, (200,200,200))
    screen.blit(hint, (WIDTH//2 - hint.get_width()//2, 360))

def draw_game_over():
    screen.fill((0,0,0))
    game_over = font_large.render("GAME OVER", True, (255,0,0))
    screen.blit(game_over, (WIDTH//2 - game_over.get_width()//2, 100))
    
    score_text = font_medium.render(f"Score: {final_score}", True, (255,255,255))
    dist_text = font_medium.render(f"Distance: {final_distance}", True, (255,255,255))
    coins_text = font_medium.render(f"Coins: {final_coins}", True, (255,215,0))
    
    screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, 200))
    screen.blit(dist_text, (WIDTH//2 - dist_text.get_width()//2, 250))
    screen.blit(coins_text, (WIDTH//2 - coins_text.get_width()//2, 300))
    
    retry_btn.draw(screen)
    menu_btn.draw(screen)

def draw_leaderboard_screen():
    screen.fill((0,0,0))
    title = font_medium.render("LEADERBOARD", True, (255,255,0))
    screen.blit(title, (WIDTH//2 - title.get_width()//2, 50))
    
    y = 120
    headers = ["#", "Name", "Score", "Dist", "Coins"]
    for i, h in enumerate(headers):
        text = font_small.render(h, True, (255,255,255))
        screen.blit(text, (20 + i*75, y))
    
    y += 30
    for i, entry in enumerate(leaderboard[:8]):
        text = font_small.render(str(i+1), True, (255,255,255))
        screen.blit(text, (25, y))
        text = font_small.render(entry["name"][:10], True, (255,255,255))
        screen.blit(text, (60, y))
        text = font_small.render(str(entry["score"]), True, (255,255,255))
        screen.blit(text, (135, y))
        text = font_small.render(str(entry["distance"]), True, (255,255,255))
        screen.blit(text, (210, y))
        text = font_small.render(str(entry["coins"]), True, (255,215,0))
        screen.blit(text, (275, y))
        y += 30
    
    back_btn.draw(screen)

def draw_settings_screen():
    screen.fill((0,0,0))
    title = font_medium.render("SETTINGS", True, (255,255,0))
    screen.blit(title, (WIDTH//2 - title.get_width()//2, 50))
    
    diff_label = font_small.render("Difficulty:", True, (255,255,255))
    screen.blit(diff_label, (WIDTH//2 - 60, 300))
    
    easy_btn.draw(screen)
    medium_btn.draw(screen)
    hard_btn.draw(screen)
    
    back_btn.draw(screen)

# Main loop
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Обработка ввода для username
        if game_state == "username":
            if username_input.handle_event(event):
                username = username_input.text
                if username == "":
                    username = "Player"
                reset_game()
                game_state = "playing"
    
    if game_state == "menu":
        play_btn.update(mouse_pos)
        leaderboard_btn.update(mouse_pos)
        settings_btn.update(mouse_pos)
        quit_btn.update(mouse_pos)
        
        if play_btn.is_clicked(mouse_pos, mouse_click):
            game_state = "username"
            username_input.text = ""
            username_input.active = True
        elif leaderboard_btn.is_clicked(mouse_pos, mouse_click):
            leaderboard = load_leaderboard()
            game_state = "leaderboard"
        elif settings_btn.is_clicked(mouse_pos, mouse_click):
            game_state = "settings"
        elif quit_btn.is_clicked(mouse_pos, mouse_click):
            running = False
        
        draw_menu()
    
    elif game_state == "username":
        draw_username()
    
    elif game_state == "playing":
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move_left()
        if keys[pygame.K_RIGHT]:
            player.move_right()
        
        game_over = update_game()
        if game_over:
            final_score = score
            final_distance = int(distance)
            final_coins = coins_collected
            leaderboard = add_score(leaderboard, username, final_score, final_distance, final_coins)
            save_leaderboard(leaderboard)
            game_state = "game_over"
        
        draw_game()
    
    elif game_state == "game_over":
        retry_btn.update(mouse_pos)
        menu_btn.update(mouse_pos)
        
        if retry_btn.is_clicked(mouse_pos, mouse_click):
            reset_game()
            game_state = "playing"
        elif menu_btn.is_clicked(mouse_pos, mouse_click):
            game_state = "menu"
        
        draw_game_over()
    
    elif game_state == "leaderboard":
        back_btn.update(mouse_pos)
        if back_btn.is_clicked(mouse_pos, mouse_click):
            game_state = "menu"
        draw_leaderboard_screen()
    
    elif game_state == "settings":
        easy_btn.update(mouse_pos)
        medium_btn.update(mouse_pos)
        hard_btn.update(mouse_pos)
        back_btn.update(mouse_pos)
        
        if easy_btn.is_clicked(mouse_pos, mouse_click):
            settings["difficulty"] = "easy"
            save_settings(settings)
            easy_btn.color = (0,150,0)
            medium_btn.color = (100,100,100)
            hard_btn.color = (100,100,100)
        elif medium_btn.is_clicked(mouse_pos, mouse_click):
            settings["difficulty"] = "medium"
            save_settings(settings)
            easy_btn.color = (100,100,100)
            medium_btn.color = (0,150,0)
            hard_btn.color = (100,100,100)
        elif hard_btn.is_clicked(mouse_pos, mouse_click):
            settings["difficulty"] = "hard"
            save_settings(settings)
            easy_btn.color = (100,100,100)
            medium_btn.color = (100,100,100)
            hard_btn.color = (0,150,0)
        elif back_btn.is_clicked(mouse_pos, mouse_click):
            game_state = "menu"
        
        draw_settings_screen()
    
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()