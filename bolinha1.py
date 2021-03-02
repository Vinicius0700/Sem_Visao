import pygame
from player import Player

class Bolinha1(pygame.sprite.Sprite):
    def __init__(self,  *groups):
        super().__init__(*groups)

        self.player = Player()

        self.image = pygame.image.load("data/bolinha.png")
        self.image = pygame.transform.scale(self.image, [4, 4])  # escalar dde acordo com o display
        self.rect = self.image.get_rect()

        self.position = self.player.y
        self.distancia = 0
        self.volume = 1
        self.speed = 4
        self.aux = 0

    def update(self, *args):
        self.rect.y -= self.speed
        self.distancia = self.player.rect.y - self.rect.y
        self.volume = 1 - (self.distancia / 10)

        self.bolinha = pygame.mixer.Sound("data/Bolinha.wav")
        self.bolinha1 = pygame.mixer.Channel(1)
        self.bolinha1.set_volume(self.volume)

        if self.kill != self.bolinha1:
            if self.aux % 12 == 0:
                self.bolinha1.play(self.bolinha)
                self.aux += 1
            else:
                self.aux += 1



#provisorio em quanto não tem colião
        # up
        if self.rect.y < 20:
            pygame.mixer.unpause()
            self.kill()





