import pygame

class Chave2(pygame.sprite.Sprite):
    def __init__(self, player,  *groups):
        super().__init__(*groups)

        self.player = player

        self.image = pygame.image.load("data/chave.png")
        self.image = pygame.transform.scale(self.image, [10, 6])  # escalar dde acordo com o display
        self.rect = self.image.get_rect()
        self.rect.x = 48
        self.rect.y = 362
        self.volume = 1
        self.distancia_x = 0
        self.distancia_y = 0
        self.aux = 0

        self.chavesom = pygame.mixer.Sound("data/chaveSom.wav")
        self.chavesom1 = pygame.mixer.Channel(3)
        self.chavesom1.set_volume(self.volume)

    def update(self, *args):
        self.chavesom1.set_volume(self.volume)
        if self.aux % 45 == 0:
            self.chavesom1.play(self.chavesom)
        auxdistancia_x = self.distancia_x
        auxdistancia_y = self.distancia_y
        self.distancia_x = self.player.rect.x - self.rect.x
        self.distancia_y = self.player.rect.y - self.rect.y

        # pergunta se a chave esta destro do raio de alcance do som
        if self.distancia_x < 100 and self.distancia_y < 100 and self.distancia_x > -100 and self.distancia_y > -100:
            if self.volume >= 1:
                self.volume = 1

            # pergunta se esta ao Sul do objeto
            if self.distancia_y > 0:

                if auxdistancia_y > self.distancia_y:  # aproximando
                    self.volume = 15 / self.distancia_y
                elif auxdistancia_y < self.distancia_y:  # diminuindo
                    self.volume = 15 / self.distancia_y

            # pergunta se esta ao Norte do objeto
            if self.distancia_y < 0:

                if auxdistancia_y > self.distancia_y:  # aproximando
                    self.volume = 15 / self.distancia_y
                    self.volume = self.volume * (-1)
                elif auxdistancia_y < self.distancia_y:  # diminuindo
                    self.volume = 15 / self.distancia_y
                    self.volume = self.volume * (-1)

            # pergunta se esta ao Oeste do objeto
            if self.distancia_x > 0:

                if auxdistancia_x > self.distancia_x: #aproximando
                    self.volume = 15 / self.distancia_x
                elif auxdistancia_x < self.distancia_x: #diminuindo
                    self.volume = 15 / self.distancia_x

            # pergunta se esta ao Leste do objeto
            if self.distancia_x < 0:

                if auxdistancia_x > self.distancia_x:  # aproximando
                    self.volume = 15 / self.distancia_x
                    self.volume = self.volume * (-1)
                elif auxdistancia_x < self.distancia_x:  # diminuindo
                    self.volume = 15 / self.distancia_x
                    self.volume = self.volume * (-1)
        else:
            self.volume = 0

        # vai definir de quanto em quanto tempo o jogo vai rodar
        self.aux += 1



