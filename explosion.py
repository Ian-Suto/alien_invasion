import pygame
from pygame.sprite import Sprite

class Explosion(Sprite):
    """A class to represent a bullet-alien explosion following collision."""
    def __init__(self, ai_game, centre):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.images = []
        for i in range(1, 5):
            img = pygame.image.load(f"images/explosion/bubble0{i}.png")
            img = pygame.transform.scale(img, (50, 58))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = centre
        self.counter = 0

    def update(self):
        explosion_speed = 4
        self.counter += 1

        if self.counter >= explosion_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
            self.kill()