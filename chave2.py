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
        self.chavesom1 = pygame.mixer.Channel(1)
        self.chavesom1.set_volume(self.volume)

    def update(self, *args):
        print(self.volume)
        auxdistancia_x = self.distancia_x
        auxdistancia_y = self.player.rect.y
        self.distancia_x = self.player.rect.x - self.rect.x
        print("aux dist ", auxdistancia_x, " dist ", self.distancia_x)
        if auxdistancia_x < self.distancia_x:
            print("IR DIREITA")
        elif auxdistancia_x > self.distancia_x:
            print("IR ESQUERDA")
        else:
            print("PARADO")
        #print("player", self.player.rect.x, " chave", self.rect.x, " Distancia", self.distancia_x)
        #print(self.distancia_x)
        if self.aux % 12 == 0:
            self.chavesom1.play(self.chavesom)
            self.aux += 1
        else:
            self.aux += 1


        if self.volume >= 0.1:
            if self.volume >= 1:
                self.volume = 1
            #volume -
            # Sul
            #keys = pygame.key.get_pressed()
            #if keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d] or keys[pygame.K_w]:
             #   self.auxdistancia_x = self.player.rect.x
             #   self.auxdistancia_x = self.player.rect.x

          #  if self.player.rect.y >= self.rect.y:# descobre se ele ta ao norte, sul, leste, este, do player
              #  #self.auxdistancia_y
              #  if self.auxdistancia_y > self.player.rect.y:# descobre a distancia entre o player e diminui o volume
              #      self.distancia_y = self.player.rect.y - self.rect.y
              #      self.volume = self.volume + (self.distancia_y / 1000)
             #   else:# almenta o volume
             #       self.distancia_y = self.player.rect.y - self.rect.y
             #       self.volume = self.volume - (self.distancia_y / 1000)
            #Norte
            #if self.player.rect.y <= self.rect.y:
             #   if self.auxdistancia_y < self.player.rect.y:
              #      self.distancia_y = self.rect.y - self.player.rect.y
             #       self.volume = self.volume + (self.distancia_y / 1000)
             #   else:
              #      self.distancia_y = self.rect.y - self.player.rect.y
              #      self.volume = self.volume - (self.distancia_y / 1000)
            #Oeste
            if self.distancia_x > 0 and self.distancia_x < 100:
                #print("distacia->", auxdistancia_x, "player->", self.player.rect.x)
                #aproximando
                self.distancia_x = self.player.rect.x - self.rect.x
                if auxdistancia_x > self.distancia_x:
                    #print("TENHO QUE ALMENTAR")
                    self.volume = 10 / self.distancia_x
                elif auxdistancia_x < self.distancia_x:
                    # print("TENHO QUE DIMINUIR")
                    self.volume = 10 / self.distancia_x
                else:
                    self.volume = self.volume
            #Leste
            #if self.player.rect.x <= self.rect.x:
            #    print("esquerda")
            #    if self.auxdistancia_x < self.player.rect.x:
             #       self.distancia_x = self.rect.x - self.player.rect.x
             #       self.volume = self.volume + (self.distancia_x / 1000)
            #    else:
             #       self.distancia_x = self.rect.x - self.player.rect.x
             #       self.volume = self.volume - (self.distancia_x / 1000)
            #else:
                #print("falou tudo")
             #   pass

            #if self.player.rect.x <= self.rect.x:
            #    self.distancia = self.player.rect.x - self.rect.x
            #    self.volume = self.volume - (self.distancia / 300)
            #if self.player.rect.x >= self.rect.x:
            #    self.distancia = self.player.rect.x - self.rect.x
            #    self.volume = self.volume - (self.distancia / 300)
            #    #volume +
            #if self.player.rect.y >= self.rect.y:
            #    self.distancia = self.player.rect.y - self.rect.y
            #    self.volume = self.volume - (self.distancia / 300)
            #if self.player.rect.y <= self.rect.y:
            #    self.distancia = self.rect.y - self.player.rect.y
            #    self.volume = self.volume - (self.distancia / 300)
            #if self.player.rect.x <= self.rect.x:
            #    self.distancia = self.player.rect.x - self.rect.x
            #    self.volume = self.volume - (self.distancia / 300)
            #if self.player.rect.x >= self.rect.x:
            #    self.distancia = self.player.rect.x - self.rect.x
            #    self.volume = self.volume - (self.distancia / 300)



                #self.distancia = self.player.rect.y - self.rect.y
                #self.volume = 1 - (self.distancia / 500)


        else:
            self.volume = 0



