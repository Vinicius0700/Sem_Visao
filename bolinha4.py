import pygame

class Bolinha4(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/bolinha.png")
        self.image = pygame.transform.scale(self.image, [4, 4])  # escalar dde acordo com o display
        self.rect = self.image.get_rect()

        self.speed = 4
        self.aux = 0

    def update(self, *args):
        self.rect.y += self.speed

        self.bolinha = pygame.mixer.Sound("data/Bolinha.wav")
        self.bolinha1 = pygame.mixer.Channel(1)
        self.bolinha1.set_volume(0.2)

        if self.kill != self.bolinha1:
            if self.aux % 12 == 0:
                self.bolinha1.play(self.bolinha)
                self.aux += 1
            else:
                self.aux += 1

#bottom
        if self.rect.y > 640:
            pygame.mixer.unpause()
            self.kill()




