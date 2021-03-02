import pygame
import random
from pygame import mixer
from player import Player
from bolinha1 import Bolinha1
from bolinha2 import Bolinha2
from bolinha3 import Bolinha3
from bolinha4 import Bolinha4
from backgroud import Backgroud
from fantasma import Fantasma


#pygame.mixer.pre_init(44100, 16, 2, 512)
#mixer.init()
pygame.init()# iniciando o pygame

display = pygame.display.set_mode([820, 660]) # resolução do jogo
pygame.display.set_caption("Joguinho do Vini") # Legenda do jogo

#Groups
objectGroup = pygame.sprite.Group()
mapGroup = pygame.sprite.Group()
bolinha1Group = pygame.sprite.Group()
bolinha2Group = pygame.sprite.Group()
bolinha3Group = pygame.sprite.Group()
bolinha4Group = pygame.sprite.Group()
playerGroup = pygame.sprite.Group()
fantasmaGroup = pygame.sprite.Group()



# criando
player = Player(playerGroup)
fantasma = Fantasma(player, fantasmaGroup)
bg = Backgroud(mapGroup)

# music
musicFundo = pygame.mixer.music.load("data/MusicFundo.ogg")
pygame.mixer.music.play(-1, 0.0, 5000)

# sounds


gameLoop = True # variavel que define se o jogo vai continuar rodando ou não
visao = False

clock = pygame.time.Clock()
if __name__ == "__main__":
    while gameLoop:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
            elif event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_l):
                    visao = True

                if event.key == pygame.K_UP:
                    newBolinha1 = Bolinha1(player, objectGroup, bolinha1Group)
                    newBolinha1.rect.center = player.rect.center

                if event.key == pygame.K_LEFT:
                    newBolinha2 = Bolinha2(player, objectGroup,bolinha2Group)
                    newBolinha2.rect.center = player.rect.center

                if event.key == pygame.K_RIGHT:
                    newBolinha3 = Bolinha3(player, objectGroup, bolinha3Group)
                    newBolinha3.rect.center = player.rect.center

                if event.key == pygame.K_DOWN:
                    newBolinha4 = Bolinha4(player, objectGroup, bolinha4Group)
                    newBolinha4.rect.center = player.rect.center




        # Update Logic
        objectGroup.update()
        mapGroup.update()
        playerGroup.update()
        fantasmaGroup.update()

        collisions = pygame.sprite.spritecollide(player, mapGroup, False, pygame.sprite.collide_mask)


        if collisions:
            print("parou")



        hits1 = pygame.sprite.groupcollide(bolinha1Group, mapGroup, True, False, pygame.sprite.collide_mask)
        hits2 = pygame.sprite.groupcollide(bolinha2Group, mapGroup, True, False, pygame.sprite.collide_mask)
        hits3 = pygame.sprite.groupcollide(bolinha3Group, mapGroup, True, False, pygame.sprite.collide_mask)
        hits4 = pygame.sprite.groupcollide(bolinha4Group, mapGroup, True, False, pygame.sprite.collide_mask)



        # Draw:
        display.fill([40, 40, 40])
        if visao:
            mapGroup.draw(display)
            fantasmaGroup.draw(display)
            playerGroup.draw(display)
            objectGroup.draw(display)
        pygame.display.update()