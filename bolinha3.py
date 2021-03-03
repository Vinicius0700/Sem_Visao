import pygame

class Bolinha3(pygame.sprite.Sprite):
    def __init__(self, player, *groups):
        super().__init__(*groups)

        self.player = player

        self.image = pygame.image.load("data/bolinha.png")
        self.image = pygame.transform.scale(self.image, [4, 4])  # escalar dde acordo com o display
        self.rect = self.image.get_rect()

        self.position = self.player.rect.x
        self.distancia = 0
        self.volume = 0.6
        self.speed = 4
        self.aux = 0

    def update(self, *args):
        self.rect.x += self.speed

        self.distancia = self.rect.x - self.player.rect.x
        self.volume = 0.6 - (self.distancia / 500)

        self.bolinha = pygame.mixer.Sound("data/Bolinha.wav")
        self.bolinha1 = pygame.mixer.Channel(6)
        self.bolinha1.set_volume(0.0, self.volume)

        if self.aux % 12 == 0:
            self.bolinha1.play(self.bolinha)
            self.aux += 1
        else:
            self.aux += 1

# right
        if self.rect.x > 800 or self.volume < 0.2:

            pygame.mixer.unpause()
            self.kill()



