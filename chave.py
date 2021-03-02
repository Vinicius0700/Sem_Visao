import pygame

class Chave(pygame.sprite.Sprite):
    def __init__(self, player,  *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/chave.png")
        self.image = pygame.transform.scale(self.image, [10, 6])  # escalar dde acordo com o display
        self.rect = self.image.get_rect()


    def update(self, *args):
        pass




