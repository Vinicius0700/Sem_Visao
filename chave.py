import pygame

class Chave(pygame.sprite.Sprite):
    def __init__(self, player,  *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/chave.png")
        self.image = pygame.transform.scale(self.image, [10, 6])  # escalar dde acordo com o display
        self.rect = self.image.get_rect()

        self.chavesom = pygame.mixer.Sound("data/chaveSom.wav")
        self.chavesom1 = pygame.mixer.Channel(1)
        self.chavesom1.set_volume(1)

        self.aux = 0


    def update(self, *args):

        if self.aux % 12 == 0:
            self.chavesom1.play(self.chavesom)
            self.aux += 1
        else:
            self.aux += 1





