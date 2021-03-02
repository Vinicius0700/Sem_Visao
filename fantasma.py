import pygame
from player import Player

class Fantasma(pygame.sprite.Sprite):

    def __init__(self, player, *groups):
        super().__init__(*groups)

        self.player = player

        self.image = pygame.image.load("data/fantasma.png")
        self.image = pygame.transform.scale(self.image, [6, 10])  # escalar dde acordo com o display
        self.rect = self.image.get_rect()
        self.rect.x = 810
        self.rect.y = 650

        self.aux = 0

        self.fantasm = pygame.mixer.Sound("data/fantasma.mp3")
        self.fantasma1 = pygame.mixer.Channel(1)


    # Logica
    def update(self, *args):

        self.volume_w = 0.3
        self.volume_l = 0.3
        self.fantasma1.set_volume(self.volume_l, self.volume_w)

        if self.aux % 30 == 0:
            self.fantasma1.play(self.fantasm)
            self.aux += 1
        else:
            if self.aux >= 500:
                self.aux = 0
            self.aux += 1


        #pygame.mixer.unpause()

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


