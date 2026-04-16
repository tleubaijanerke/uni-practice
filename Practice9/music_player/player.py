import pygame
import os

class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()

        base = os.path.dirname(__file__)
        music_path = os.path.join(base, "music")

        self.playlist = [
            os.path.join(music_path, "Babydoll.wav"),
            os.path.join(music_path, "Dracula.wav"),
        ]

        self.index = 0
        self.current = self.playlist[self.index]

        # state
        self.is_playing = False

    def play(self):
        pygame.mixer.music.load(self.current)
        pygame.mixer.music.play()
        self.is_playing = True

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False

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

    # 🔥 CURRENT TIME (seconds)
    def get_pos(self):
        return pygame.mixer.music.get_pos() / 1000  # ms → sec