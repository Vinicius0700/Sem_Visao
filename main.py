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
from chave1 import Chave1
from chave2 import Chave2
from chave3 import Chave3
from chave4 import Chave4
from porta import Porta


#pygame.mixer.pre_init(44100, 16, 2, 512)
#mixer.init()
pygame.init()# iniciando o pygame

display = pygame.display.set_mode([820, 660]) # resolução do jogo
pygame.display.set_caption("Joguinho do Vini") # Legenda do jogo

gameLoop = True # variavel que define se o jogo vai continuar rodando ou não

clock = pygame.time.Clock()

def criaObject ():
    # Groups
    objectGroup = pygame.sprite.Group()
    mapGroup = pygame.sprite.Group()
    bolinha1Group = pygame.sprite.Group()
    bolinha2Group = pygame.sprite.Group()
    bolinha3Group = pygame.sprite.Group()
    bolinha4Group = pygame.sprite.Group()
    playerGroup = pygame.sprite.Group()
    fantasmaGroup = pygame.sprite.Group()
    chave1Group = pygame.sprite.Group()
    chave2Group = pygame.sprite.Group()
    chave3Group = pygame.sprite.Group()
    chave4Group = pygame.sprite.Group()
    portaGroup = pygame.sprite.Group()


    player = Player(playerGroup)
    fantasma = Fantasma(player, fantasmaGroup)
    bg = Backgroud(mapGroup)
    porta = Porta(portaGroup)

    #chaves1 = Chave1(player, objectGroup, chave1Group)

    chaves2 = Chave2(player, objectGroup, chave2Group)

    #chaves3 = Chave3(player, objectGroup, chave3Group)

    #chaves4 = Chave4(player, objectGroup, chave4Group)

    # music
    musicFundo = pygame.mixer.music.load("data/MusicFundo.ogg")
    pygame.mixer.music.play(-1, 0.0, 5000)

    # sounds

    ai = pygame.mixer.Sound("data/ai.wav")
    ai1 = pygame.mixer.Channel(1)
    ai1.set_volume(1)

    chave_insuficiente = pygame.mixer.Sound("data/chaveInsuficiente.wav")
    chave_insuficiente1 = pygame.mixer.Channel(1)
    chave_insuficiente1.set_volume(1)

    fugir = pygame.mixer.Sound("data/fugiu.wav")
    fugir1 = pygame.mixer.Channel(1)
    fugir1.set_volume(1)

    introducao = pygame.mixer.Sound("data/introducao.wav")
    introducao1 = pygame.mixer.Channel(1)
    introducao1.set_volume(1)

    gameover = pygame.mixer.Sound("data/gameover.wav")
    gameover1 = pygame.mixer.Channel(1)
    gameover1.set_volume(1)

    # variaveis auxiliares

    playerx = player.rect.x
    playery = player.rect.y
    quantchave = 4
    passarporta = False

    visao = False
    gameLoopTela = True


    while gameLoopTela:
        clock.tick(60)

        introducao1.play(introducao)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameLoop = False
                exit()
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_l):
                    visao = True

                if event.key == pygame.K_UP:
                    newBolinha1 = Bolinha1(player, objectGroup, bolinha1Group)
                    newBolinha1.rect.center = player.rect.center

                if event.key == pygame.K_LEFT:
                    newBolinha2 = Bolinha2(player, objectGroup, bolinha2Group)
                    newBolinha2.rect.center = player.rect.center

                if event.key == pygame.K_RIGHT:
                    newBolinha3 = Bolinha3(player, objectGroup, bolinha3Group)
                    newBolinha3.rect.center = player.rect.center

                if event.key == pygame.K_DOWN:
                    newBolinha4 = Bolinha4(player, objectGroup, bolinha4Group)
                    newBolinha4.rect.center = player.rect.center

        collisions = pygame.sprite.spritecollide(player, mapGroup, False, pygame.sprite.collide_mask)

        if collisions:
            player.rect.x = playerx
            player.rect.y = playery
            ai1.play(ai)
        else:
            playerx = player.rect.x
            playery = player.rect.y

        chave1colission = pygame.sprite.spritecollide(player, chave1Group, False, pygame.sprite.collide_mask)
        if chave1colission:
            #chaves1.kill()
            quantchave -= 1

        chave2colission = pygame.sprite.spritecollide(player, chave2Group, False, pygame.sprite.collide_mask)
        if chave2colission:
            chaves2.kill()
            quantchave -= 1

        chave3colission = pygame.sprite.spritecollide(player, chave3Group, False, pygame.sprite.collide_mask)
        if chave3colission:
           # chaves3.kill()
            quantchave -= 1

        chave4colission = pygame.sprite.spritecollide(player, chave4Group, False, pygame.sprite.collide_mask)
        if chave4colission:
            #chaves4.kill()
            quantchave -= 1

        if quantchave == 0:
            passarporta = True

        portacolission = pygame.sprite.spritecollide(player, portaGroup, False, pygame.sprite.collide_mask)
        if portacolission:
            player.rect.y = playery - 3
            if passarporta == True:
                fugir1.play(fugir)
                gameLoopTela = False
                #print("Parabens voce zerou o jogo")
            elif passarporta == False:
                chave_insuficiente1.play(chave_insuficiente)
                #print("quantidade de chave insuficiente")

        fantasmacolission = pygame.sprite.spritecollide(player, fantasmaGroup, False, pygame.sprite.collide_mask)
        if fantasmacolission:
            #print("Game over")
            gameover1.play(gameover)
            gameLoopTela = False

        # Update Logic
        objectGroup.update()
        mapGroup.update()
        playerGroup.update()
        fantasmaGroup.update()
        chave1Group.update()
        chave2Group.update()
        chave3Group.update()
        chave4Group.update()
        portaGroup.update()

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
            chave1Group.draw(display)
            chave2Group.draw(display)
            chave3Group.draw(display)
            chave4Group.draw(display)
            portaGroup.draw(display)

            objectGroup.draw(display)
        pygame.display.update()




if __name__ == "__main__":
    while gameLoop:
        criaObject()