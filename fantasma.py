import pygame
from player import Player

class Fantasma(pygame.sprite.Sprite):



    def __init__(self, *groups):
        super().__init__(*groups)

        self.player = Player()

        self.image = pygame.image.load("data/fantasma.png")
        self.image = pygame.transform.scale(self.image, [6, 10])  # escalar dde acordo com o display
        self.rect = self.image.get_rect()
        self.rect.x = 810
        self.rect.y = 650

    # Logica
    def update(self, *args):

        self.player = Player()
        print("x -> ", self.player.rect.x, " y -> ", self.player.rect.y)

        if self.rect.top < 20:
            self.rect.top = 20
        if self.rect.bottom > 640:
            self.rect.bottom = 640
        if self.rect.left < 20:
            self.rect.left = 20
        if self.rect.right > 800:
            self.rect.right = 800

        if self.player.rect.x > self.rect.x:
            self.rect.x += 1
        if self.player.rect.y > self.rect.y:
            self.rect.y += 1
        if self.player.rect.x < self.rect.x:
            self.rect.x -= 1
        if self.player.rect.y < self.rect.y:
            self.rect.y -= 1


