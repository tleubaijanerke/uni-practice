import pygame
import random

class Player:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 60
        self.img = img
        self.speed = 5
        self.nitro_active = False
        self.nitro_timer = 0
        self.shield_active = False
        self.shield_timer = 0
    
    def move_left(self):
        if self.x > 0:
            self.x -= self.speed
    
    def move_right(self):
        if self.x < 400 - self.width:
            self.x += self.speed
    
    def update(self):
        if self.nitro_active:
            self.nitro_timer -= 1
            if self.nitro_timer <= 0:
                self.nitro_active = False
        
        if self.shield_active:
            self.shield_timer -= 1
            if self.shield_timer <= 0:
                self.shield_active = False
    
    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))
        if self.shield_active:
            pygame.draw.circle(screen, (0,255,255), (self.x + 20, self.y + 30), 35, 3)
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

class Enemy:
    def __init__(self, x, y, speed, img):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 60
        self.speed = speed
        self.img = img
    
    def update(self):
        self.y += self.speed
    
    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

class Coin:
    def __init__(self, x, y, value, img):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.value = value
        self.speed = 4
        self.img = img
    
    def update(self):
        self.y += self.speed
    
    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))
        font = pygame.font.SysFont("Arial", 12)
        text = font.render(str(self.value), True, (0,0,0))
        screen.blit(text, (self.x + 6, self.y + 4))
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

class Obstacle:
    def __init__(self, x, y, obstacle_type, img):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.type = obstacle_type
        self.speed = 5
        self.img = img
    
    def update(self):
        self.y += self.speed
    
    def draw(self, screen):
        if self.type == "barrier":
            screen.blit(self.img, (self.x, self.y))
        elif self.type == "oil":
            pygame.draw.circle(screen, (50,50,50), (self.x + 15, self.y + 15), 15)
            pygame.draw.circle(screen, (80,80,80), (self.x + 15, self.y + 15), 10)
        elif self.type == "pothole":
            pygame.draw.circle(screen, (100,100,100), (self.x + 15, self.y + 15), 12)
            pygame.draw.circle(screen, (60,60,60), (self.x + 15, self.y + 15), 8)
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

class PowerUp:
    def __init__(self, x, y, power_type, img):
        self.x = x
        self.y = y
        self.width = 25
        self.height = 25
        self.type = power_type
        self.speed = 4
        self.lifetime = 300
        self.img = img
    
    def update(self):
        self.y += self.speed
        self.lifetime -= 1
    
    def is_alive(self):
        return self.lifetime > 0 and self.y < 600
    
    def draw(self, screen):
        screen.blit(self.img, (self.x, self.y))
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)