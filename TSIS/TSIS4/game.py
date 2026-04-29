import pygame
import random
from config import *

def draw_grid(screen):
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(screen, (50,50,50), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(screen, (50,50,50), (0, y), (WIDTH, y))

def get_random_position(snake, obstacles):
    while True:
        x = random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE)
        y = random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
        if [x, y] not in snake and [x, y] not in obstacles:
            return [x, y]

def game(screen, username, settings):
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 24)
    
    # Snake
    snake = [[WIDTH//2, HEIGHT//2]]
    direction = [BLOCK_SIZE, 0]
    snake_color = tuple(settings["snake_color"])
    grid_on = settings["grid_overlay"]
    length = 1
    score = 0
    level = 1
    food_eaten = 0
    
    # Speed
    base_speed = 10
    current_speed = base_speed
    
    # Power-up effects
    speed_boost_end = 0
    slow_motion_end = 0
    shield_active = False
    
    # Food
    obstacles = []
    food = None
    powerup = None
    powerup_cooldown = 0
    
    def spawn_food():
        nonlocal food
        pos = get_random_position(snake, obstacles)
        is_poison = random.random() < 0.2
        value = random.choice([1,2,5]) if not is_poison else 1
        return {"x": pos[0], "y": pos[1], "value": value, "poison": is_poison, "spawn_time": pygame.time.get_ticks()}
    
    def spawn_powerup():
        nonlocal powerup
        if powerup_cooldown <= 0:
            pos = get_random_position(snake, obstacles)
            types = ["speed", "slow", "shield"]
            return {"x": pos[0], "y": pos[1], "type": random.choice(types), "spawn_time": pygame.time.get_ticks()}
        return None
    
    def spawn_obstacles():
        nonlocal obstacles
        if level >= 3:
            obstacles = []
            num = min(level, 6)
            for _ in range(num):
                pos = get_random_position(snake, obstacles)
                obstacles.append(pos)
    
    food = spawn_food()
    spawn_obstacles()
    
    # Personal best
    from db import get_personal_best
    personal_best = get_personal_best(username)
    
    running = True
    last_move = pygame.time.get_ticks()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direction != [BLOCK_SIZE, 0]:
                    direction = [-BLOCK_SIZE, 0]
                elif event.key == pygame.K_RIGHT and direction != [-BLOCK_SIZE, 0]:
                    direction = [BLOCK_SIZE, 0]
                elif event.key == pygame.K_UP and direction != [0, BLOCK_SIZE]:
                    direction = [0, -BLOCK_SIZE]
                elif event.key == pygame.K_DOWN and direction != [0, -BLOCK_SIZE]:
                    direction = [0, BLOCK_SIZE]
        
        # Move snake
        now = pygame.time.get_ticks()
        move_delay = 1000 // current_speed
        
        if now - last_move >= move_delay:
            new_head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]
            
            # Check wall collision
            if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT:
                if shield_active:
                    shield_active = False
                else:
                    running = False
                    break
            
            # Check obstacle collision
            if new_head in obstacles:
                if shield_active:
                    shield_active = False
                else:
                    running = False
                    break
            
            snake.insert(0, new_head)
            if len(snake) > length:
                snake.pop()
            
            # Check self collision
            if snake[0] in snake[1:]:
                if shield_active:
                    shield_active = False
                else:
                    running = False
                    break
            
            last_move = now
        
        # Check food collision
        if snake[0][0] == food["x"] and snake[0][1] == food["y"]:
            if food["poison"]:
                length = max(1, length - 2)
                if length <= 1 and len(snake) > 1:
                    while len(snake) > length:
                        snake.pop()
                score = max(0, score - 10)
                if len(snake) <= 1:
                    running = False
                    break
            else:
                score += food["value"]
                length += 1
                food_eaten += 1
            
            food = spawn_food()
            
            # Level up
            if food_eaten >= 5 + (level - 1) * 2:
                level += 1
                food_eaten = 0
                base_speed = min(20, base_speed + 1)
                spawn_obstacles()
        
        # Check power-up collision
        if powerup and snake[0][0] == powerup["x"] and snake[0][1] == powerup["y"]:
            now = pygame.time.get_ticks()
            if powerup["type"] == "speed":
                speed_boost_end = now + 5000
            elif powerup["type"] == "slow":
                slow_motion_end = now + 5000
            elif powerup["type"] == "shield":
                shield_active = True
            powerup = None
            powerup_cooldown = 90
        
        # Update current speed
        now = pygame.time.get_ticks()
        if now < speed_boost_end:
            current_speed = base_speed + 5
        elif now < slow_motion_end:
            current_speed = max(3, base_speed - 3)
        else:
            current_speed = base_speed
        
        # Update cooldown
        if powerup_cooldown > 0:
            powerup_cooldown -= 1
        
        # Spawn power-up
        if powerup is None and powerup_cooldown <= 0 and random.random() < 0.003:
            powerup = spawn_powerup()
        
        # Check food expiration
        if pygame.time.get_ticks() - food["spawn_time"] > 8000:
            food = spawn_food()
        
        # Check power-up expiration
        if powerup and pygame.time.get_ticks() - powerup["spawn_time"] > 8000:
            powerup = None
        
        # Draw everything
        screen.fill(BLACK)
        
        if grid_on:
            draw_grid(screen)
        
        # Draw obstacles
        for obs in obstacles:
            pygame.draw.rect(screen, GRAY, [obs[0], obs[1], BLOCK_SIZE, BLOCK_SIZE])
        
        # Draw food
        if food["poison"]:
            pygame.draw.rect(screen, DARK_RED, [food["x"], food["y"], BLOCK_SIZE, BLOCK_SIZE])
        else:
            color = WHITE if food["value"] == 1 else YELLOW if food["value"] == 2 else ORANGE
            pygame.draw.rect(screen, color, [food["x"], food["y"], BLOCK_SIZE, BLOCK_SIZE])
        
        # Draw power-up
        if powerup:
            color = CYAN if powerup["type"] == "speed" else PURPLE if powerup["type"] == "slow" else BLUE
            pygame.draw.rect(screen, color, [powerup["x"], powerup["y"], BLOCK_SIZE, BLOCK_SIZE])
        
        # Draw snake
        for block in snake:
            pygame.draw.rect(screen, snake_color, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])
        
        if shield_active:
            pygame.draw.circle(screen, BLUE, (snake[0][0] + 10, snake[0][1] + 10), 15, 2)
        
        # Draw UI
        score_text = font.render(f"Score: {score}", True, WHITE)
        level_text = font.render(f"Level: {level}", True, WHITE)
        best_text = font.render(f"Best: {personal_best}", True, WHITE)
        
        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (10, 35))
        screen.blit(best_text, (10, 60))
        
        # Power-up indicators
        y = 90
        if now < speed_boost_end:
            sec = (speed_boost_end - now) // 1000 + 1
            screen.blit(font.render(f"SPEED: {sec}s", True, CYAN), (10, y))
            y += 25
        if now < slow_motion_end:
            sec = (slow_motion_end - now) // 1000 + 1
            screen.blit(font.render(f"SLOW: {sec}s", True, PURPLE), (10, y))
            y += 25
        if shield_active:
            screen.blit(font.render("SHIELD ACTIVE", True, BLUE), (10, y))
        
        pygame.display.update()
        clock.tick(60)
    
    # Game over - save result
    from db import save_result
    save_result(username, score, level)
    
    # Show game over screen
    waiting = True
    while waiting:
        screen.fill(BLACK)
        go_text = pygame.font.SysFont("Arial", 48).render("GAME OVER", True, RED)
        screen.blit(go_text, (WIDTH//2 - go_text.get_width()//2, 100))
        
        s_text = pygame.font.SysFont("Arial", 32).render(f"Score: {score}", True, WHITE)
        l_text = pygame.font.SysFont("Arial", 32).render(f"Level: {level}", True, WHITE)
        b_text = pygame.font.SysFont("Arial", 32).render(f"Best: {personal_best}", True, YELLOW)
        
        screen.blit(s_text, (WIDTH//2 - s_text.get_width()//2, 200))
        screen.blit(l_text, (WIDTH//2 - l_text.get_width()//2, 250))
        screen.blit(b_text, (WIDTH//2 - b_text.get_width()//2, 300))
        
        retry_btn = pygame.Rect(100, 400, 180, 40)
        menu_btn = pygame.Rect(320, 400, 180, 40)
        
        pygame.draw.rect(screen, GREEN, retry_btn)
        pygame.draw.rect(screen, BLUE, menu_btn)
        
        screen.blit(pygame.font.SysFont("Arial", 24).render("RETRY", True, WHITE), (160, 410))
        screen.blit(pygame.font.SysFont("Arial", 24).render("MENU", True, WHITE), (380, 410))
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retry_btn.collidepoint(event.pos):
                    game(screen, username, settings)
                    return
                elif menu_btn.collidepoint(event.pos):
                    return