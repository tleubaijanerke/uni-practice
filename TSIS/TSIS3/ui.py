import pygame

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.font = pygame.font.SysFont("Arial", 24)
        self.hovered = False
    
    def draw(self, screen):
        color = self.hover_color if self.hovered else self.color
        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, (255,255,255), self.rect, 2)
        text_surface = self.font.render(self.text, True, (255,255,255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
    
    def update(self, mouse_pos):
        self.hovered = self.rect.collidepoint(mouse_pos)
    
    def is_clicked(self, mouse_pos, mouse_click):
        return self.rect.collidepoint(mouse_pos) and mouse_click[0]

class TextInput:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = ""
        self.active = False
        self.font = pygame.font.SysFont("Arial", 24)
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                self.active = False
                return True
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pygame.K_ESCAPE:
                self.active = False
            else:
                # Обработка обычных символов
                if event.unicode and event.unicode.isprintable():
                    if len(self.text) < 15:
                        self.text += event.unicode
        return False
    
    def draw(self, screen):
        # Рисуем рамку
        color = (255,255,255) if self.active else (150,150,150)
        pygame.draw.rect(screen, color, self.rect, 2)
        
        # Рисуем текст
        text_surface = self.font.render(self.text, True, (255,255,255))
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 8))
        
        # Рисуем курсор если активен
        if self.active:
            cursor_x = self.rect.x + 5 + self.font.size(self.text)[0]
            # Мигающий курсор
            if pygame.time.get_ticks() % 1000 < 500:
                pygame.draw.line(screen, (255,255,255), 
                               (cursor_x, self.rect.y + 5),
                               (cursor_x, self.rect.y + self.rect.height - 5), 2)