import pygame

class Backgroud(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/Map.png")
        self.image = pygame.transform.scale(self.image, [820, 660])
        self.rect = self.image.get_rect()

