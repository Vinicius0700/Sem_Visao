import pygame

class Bolinha(pygame.sprite.Sprite):
    def __init__(self, direcaobolinha, player,  *groups):
        super().__init__(*groups)

        self.player = player

        self.image = pygame.image.load("data/bolinha.png")
        self.image = pygame.transform.scale(self.image, [4, 4])  # escalar dde acordo com o display
        self.rect = self.image.get_rect()

        self.position = self.player.rect.y
        self.distancia = 0
        self.volume_d = 1
        self.volume_e = 1
        self.speed = 4
        self.aux = 0
        self.direcao = direcaobolinha

        self.bolinha = pygame.mixer.Sound("data/Bolinha.wav")
        self.bolinha1 = pygame.mixer.Channel(7)
        self.time = pygame.time.Clock()


    def update(self, *args):

        self.time.tick(60)

# up
        if self.direcao == 5:

            self.rect.y -= self.speed
            self.distancia = self.player.rect.y - self.rect.y
            self.volume_e = 1 - (self.distancia / 200)
            self.volume_d = 1 - (self.distancia / 200)
            self.bolinha1.set_volume(self.volume_e, self.volume_d)

            if self.aux % 10 == 0:
                self.bolinha1.play(self.bolinha)
                self.aux += 1
            else:
                self.aux += 1

            if self.rect.y < 20 or self.volume_e < 0.2 or self.volume_d < 0.2:
                pygame.mixer.unpause()
                self.kill()
#left
        if self.direcao == 1:

            self.rect.x -= self.speed
            self.distancia = self.player.rect.x - self.rect.x
            self.volume_e = 0.6 - (self.distancia / 300)
            self.volume_d = 0
            self.bolinha1.set_volume(self.volume_e, self.volume_d)

            if self.aux % 10 == 0:
                self.bolinha1.play(self.bolinha)
                self.aux += 1
            else:
                self.aux += 1

            if self.rect.x < 20 or self.volume_e < 0.1:
                pygame.mixer.unpause()
                self.kill()

# right
        if self.direcao == 3:

            self.rect.x += self.speed
            self.distancia = self.rect.x - self.player.rect.x
            self.volume_d = 0.6 - (self.distancia / 300)
            self.volume_e = 0
            self.bolinha1.set_volume(self.volume_e, self.volume_d)

            if self.aux % 10 == 0:
                self.bolinha1.play(self.bolinha)
                self.aux += 1
            else:
                self.aux += 1

            if self.rect.x > 800 or self.volume_d < 0.1:
                pygame.mixer.unpause()
                self.kill()

# bottom
        if self.direcao == 2:

            self.rect.y += self.speed
            self.distancia = self.rect.y - self.player.rect.y
            self.volume_d = 0.5 - (self.distancia / 500)
            self.volume_e = 0.5 - (self.distancia / 500)
            self.bolinha1.set_volume(self.volume_e, self.volume_d)

            if self.aux % 10 == 0:
                self.bolinha1.play(self.bolinha)
                self.aux += 1
            else:
                self.aux += 1

            if self.rect.y > 640 or self.volume_d < 0.1 or self.volume_e < 0.1:
                pygame.mixer.unpause()
                self.kill()



