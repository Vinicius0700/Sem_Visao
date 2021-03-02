import pygame

class Porta(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/porta.png")
        self.image = pygame.transform.scale(self.image, [15, 25])
        self.rect = self.image.get_rect()
        self.rect.x = 403
        self.rect.y = 290


