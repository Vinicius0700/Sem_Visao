import pygame

class Chave1(pygame.sprite.Sprite):
    def __init__(self, player,  *groups):
        super().__init__(*groups)

        self.player = player

        self.image = pygame.image.load("data/chave.png")
        self.image = pygame.transform.scale(self.image, [10, 6])  # escalar dde acordo com o display
        self.rect = self.image.get_rect()
        self.rect.x = 40
        self.rect.y = 30
        self.volume = 1
        self.distancia = 0
        self.aux = 0

        self.chavesom = pygame.mixer.Sound("data/chaveSom.wav")
        self.chavesom1 = pygame.mixer.Channel(1)
        self.chavesom1.set_volume(1)

    def update(self, *args):

        if self.aux % 12 == 0:
            self.chavesom1.play(self.chavesom)
            self.aux += 1
        else:
            self.aux += 1
        if self.rect.y < 20 or self.volume < 0.2:
            self.distancia = self.player.rect.y - self.rect.y
            self.volume = 1 - (self.distancia / 500)





