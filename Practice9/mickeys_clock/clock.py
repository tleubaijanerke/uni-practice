import pygame
import datetime
import os

class MickeyClock:
    def __init__(self, width, height):
        self.center = (width // 2, height // 2)

        base = os.path.dirname(__file__)
        img_path = os.path.join(base, "images")

        self.clock_img = pygame.image.load(os.path.join(img_path, "clock.png")).convert_alpha()
        self.mickey_img = pygame.image.load(os.path.join(img_path, "mUmrP.png")).convert_alpha()

        self.left_arm = pygame.image.load(os.path.join(img_path, "hand_left.png")).convert_alpha()
        self.right_arm = pygame.image.load(os.path.join(img_path, "hand_right.png")).convert_alpha()

        self.clock_img = pygame.transform.scale(self.clock_img, (800, 600))
        self.mickey_img = pygame.transform.scale(self.mickey_img, (300, 300))

        self.left_arm = pygame.transform.scale(self.left_arm, (160, 160))
        self.right_arm = pygame.transform.scale(self.right_arm, (160, 160))

        self.left_shoulder = (self.center[0] - 70, self.center[1] - 30)
        self.right_shoulder = (self.center[0] + 40, self.center[1] - 0)

        self.min_angle = 0
        self.sec_angle = 0

    def update(self):
        now = datetime.datetime.now()

        minutes = now.minute
        seconds = now.second

        self.min_angle = -minutes * 6
        self.sec_angle = -seconds * 6

    def draw_arm(self, screen, image, angle, pivot):
        rotated = pygame.transform.rotate(image, angle)
        rect = rotated.get_rect(center=pivot)
        screen.blit(rotated, rect)

    def draw(self, screen):
        screen.blit(self.clock_img, (self.center[0] - 400, self.center[1] - 300))

        screen.blit(self.mickey_img, self.mickey_img.get_rect(center=self.center))

        self.draw_arm(screen, self.right_arm, self.sec_angle, self.right_shoulder)

        self.draw_arm(screen, self.left_arm, self.min_angle, self.left_shoulder)