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
        self.distancia_x = 0
        self.distancia_y = 0
        self.volume_e = 1
        self.volume_d = 1
        self.speed = 1

        self.aux = 0

        self.fantasma = pygame.mixer.Sound("data/fantasma.mp3")
        self.fantasma1 = pygame.mixer.Channel(6)

        self.time = pygame.time.Clock()
    # Logica
    def update(self, *args):
        self.time.tick(60)
        self.fantasma1.set_volume(self.volume_e, self.volume_d)
        if self.aux % 300 == 0:
            #self.bolinha1.set_volume(self.volume_e, self.volume_d)
            self.fantasma1.play(self.fantasma)
        auxdistancia_x = self.distancia_x
        auxdistancia_y = self.distancia_y
        self.distancia_x = self.player.rect.x - self.rect.x
        self.distancia_y = self.player.rect.y - self.rect.y

        # pergunta se a chave esta destro do raio de alcance do som
        if self.distancia_x < 200 and self.distancia_y < 200 and self.distancia_x > -200 and self.distancia_y > -200:
            if self.volume_d >= 1:
                self.volume_d = 1
            if self.volume_e >= 1:
                self.volume_e = 1

            # pergunta se esta ao Sul do objeto
            if self.distancia_y > 0:

                if auxdistancia_y > self.distancia_y:  # aproximando
                    self.volume_d = 20 / self.distancia_y
                    self.volume_e = 20 / self.distancia_y
                elif auxdistancia_y < self.distancia_y:  # diminuindo
                    self.volume_d = 20 / self.distancia_y
                    self.volume_e = 20 / self.distancia_y

            # pergunta se esta ao Norte do objeto
            if self.distancia_y < 0:

                if auxdistancia_y > self.distancia_y:  # aproximando
                    self.volume_d = 20 / self.distancia_y
                    self.volume_d = self.volume_d * (-1)
                    self.volume_e = 20 / self.distancia_y
                    self.volume_e = self.volume_e * (-1)
                elif auxdistancia_y < self.distancia_y:  # diminuindo
                    self.volume_d = 20 / self.distancia_y
                    self.volume_d = self.volume_d * (-1)
                    self.volume_e = 20 / self.distancia_y
                    self.volume_e = self.volume_e * (-1)

            # pergunta se esta ao Oeste do objeto
            if self.distancia_x > 0:

                if auxdistancia_x > self.distancia_x:  # aproximando
                    self.volume_d = 20 / self.distancia_x
                elif auxdistancia_x < self.distancia_x:  # diminuindo
                    self.volume_d = 20 / self.distancia_x

            # pergunta se esta ao Leste do objeto
            if self.distancia_x < 0:

                if auxdistancia_x > self.distancia_x:  # aproximando
                    self.volume_e = 20 / self.distancia_x
                    self.volume_e = self.volume_e * (-1)
                elif auxdistancia_x < self.distancia_x:  # diminuindo
                    self.volume_e = 20 / self.distancia_x
                    self.volume_e = self.volume_e * (-1)
        else:
            self.volume_d = 0
            self.volume_e = 0
            pygame.mixer.pause()

        # vai definir de quanto em quanto tempo o jogo vai rodar
        self.aux += 1



        if self.rect.top < 20:
            self.rect.top = 20
        if self.rect.bottom > 640:
            self.rect.bottom = 640
        if self.rect.left < 20:
            self.rect.left = 20
        if self.rect.right > 800:
            self.rect.right = 800

        #controla a velocidade dele
        if self.aux % 4 == 0:
            if self.player.rect.x > self.rect.x:
                self.rect.x += 1 / self.speed
            if self.player.rect.y > self.rect.y:
                self.rect.y += 1 / self.speed
            if self.player.rect.x < self.rect.x:
                self.rect.x -=  1 / self.speed
            if self.player.rect.y < self.rect.y:
                self.rect.y -= 1 / self.speed


