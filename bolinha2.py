import pygame


class Bolinha2(pygame.sprite.Sprite):
    def __init__(self, player, *groups):
        super().__init__(*groups)

        self.player = player

        self.image = pygame.image.load("data/bolinha.png")
        self.image = pygame.transform.scale(self.image, [4, 4])  # escalar dde acordo com o display
        self.rect = self.image.get_rect()

        self.position = self.player.rect.y
        self.distancia = 0
        self.volume = 0.6
        self.speed = 4
        self.aux = 0

    def update(self, *args):
        self.rect.x -= self.speed

        self.distancia = self.player.rect.x - self.rect.x
        self.volume = 0.6 - (self.distancia / 500)

        self.bolinha = pygame.mixer.Sound("data/Bolinha.wav")
        self.bolinha1 = pygame.mixer.Channel(0)
        self.bolinha1.set_volume(self.volume, 0.0)

        if self.aux % 12 == 0:
            self.bolinha1.play(self.bolinha)
            self.aux += 1
        else:
            self.aux += 1

#left
        if self.rect.x < 20 or self.volume < 0.2:
            pygame.mixer.unpause()
            self.kill()



