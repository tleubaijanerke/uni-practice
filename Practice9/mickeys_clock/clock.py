import pygame
import datetime
import os

class MickeyClock:
    def __init__(self, width, height):
        self.center = (width // 2, height // 2)

        base = os.path.dirname(__file__)
        path = os.path.join(base, "images", "mickey_hand.png")

        self.hand = pygame.image.load(path)  # БЕЗ convert_alpha (безопаснее)
        self.hand = pygame.transform.scale(self.hand, (200, 200))

        self.min_angle = 0
        self.sec_angle = 0

    def update(self):
        now = datetime.datetime.now()

        minutes = now.minute
        seconds = now.second

        self.min_angle = -minutes * 6
        self.sec_angle = -seconds * 6

    def rotate(self, img, angle):
        rotated = pygame.transform.rotate(img, angle)
        rect = rotated.get_rect(center=self.center)
        return rotated, rect

    def draw(self, screen):
        sec_img, sec_rect = self.rotate(self.hand, self.sec_angle)
        screen.blit(sec_img, sec_rect)

        min_img, min_rect = self.rotate(self.hand, self.min_angle)
        screen.blit(min_img, min_rect)