import pygame
import datetime
import os

def save_canvas(surface):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    folder = os.path.join(current_dir, "saves")
    
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"Folder created: {folder}")
    
    filename = datetime.datetime.now().strftime("paint_%Y%m%d_%H%M%S.png")
    path = os.path.join(folder, filename)
    
    pygame.image.save(surface, path)
    print(f"Saved: {path}")
    return path

def flood_fill(surface, x, y, new_color):
    if x < 0 or x >= surface.get_width() or y < 0 or y >= surface.get_height():
        return
    
    target_color = surface.get_at((x, y))
    if target_color == new_color:
        return
    
    width, height = surface.get_width(), surface.get_height()
    stack = [(x, y)]
    
    while stack:
        cx, cy = stack.pop()
        
        if 0 <= cx < width and 0 <= cy < height:
            try:
                if surface.get_at((cx, cy)) == target_color:
                    surface.set_at((cx, cy), new_color)
                    
                    if cx > 0:
                        stack.append((cx-1, cy))
                    if cx < width-1:
                        stack.append((cx+1, cy))
                    if cy > 0:
                        stack.append((cx, cy-1))
                    if cy < height-1:
                        stack.append((cx, cy+1))
            except:
                pass

def draw_preview_rect(screen, color, start_pos, end_pos, fill_mode, brush_size):
    x1, y1 = start_pos
    x2, y2 = end_pos
    rect = pygame.Rect(min(x1,x2), min(y1,y2), abs(x2-x1), abs(y2-y1))
    width = 0 if fill_mode else brush_size
    pygame.draw.rect(screen, color, rect, width)

def draw_preview_circle(screen, color, start_pos, end_pos, fill_mode, brush_size):
    x1, y1 = start_pos
    x2, y2 = end_pos
    r = int(((x2-x1)**2 + (y2-y1)**2)**0.5)
    width = 0 if fill_mode else brush_size
    pygame.draw.circle(screen, color, start_pos, r, width)

def draw_preview_square(screen, color, start_pos, end_pos, fill_mode, brush_size):
    x1, y1 = start_pos
    x2, y2 = end_pos
    
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
    width = 0 if fill_mode else brush_size
    pygame.draw.rect(screen, color, square, width)