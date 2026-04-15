import pygame
import os

class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()

        base = os.path.dirname(__file__)
        music_path = os.path.join(base, "music")

        self.playlist = [
            os.path.join(music_path, "track1.wav"),
            os.path.join(music_path, "track2.wav"),
        ]

        self.index = 0
        self.current = self.playlist[self.index]

    def play(self):
        pygame.mixer.music.load(self.current)
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()

    def next(self):
        self.index = (self.index + 1) % len(self.playlist)
        self.current = self.playlist[self.index]
        self.play()

    def back(self):
        self.index = (self.index - 1) % len(self.playlist)
        self.current = self.playlist[self.index]
        self.play()

    def get_track_name(self):
        return os.path.basename(self.current)