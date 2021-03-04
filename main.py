import pygame
import random
from player import Player
from bolinha import Bolinha
from backgroud import Backgroud
from fantasma import Fantasma
from chave import Chave
from porta import Porta



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

    # inicialização
    player = Player(playerGroup)
    fantasma = Fantasma(player, fantasmaGroup)
    bg = Backgroud(mapGroup)
    porta = Porta(player, objectGroup, portaGroup)

    chaves1 = Chave(player, objectGroup, chave1Group)
    chaves1.rect.x = 366
    chaves1.rect.y = 50

    chaves2 = Chave(player, objectGroup, chave2Group)
    chaves2.rect.x = 48
    chaves2.rect.y = 362

    chaves3 = Chave(player, objectGroup, chave3Group)
    chaves3.rect.x = 564
    chaves3.rect.y = 542

    chaves4 = Chave(player, objectGroup, chave4Group)
    chaves4.rect.x = 700
    chaves4.rect.y = 185

    # music
    musicFundo = pygame.mixer.music.load("data/MusicFundo.ogg")
    pygame.mixer.music.play(-1, 0.0, 5000)

    # sounds

    ai = pygame.mixer.Sound("data/ai.wav")
    ai1 = pygame.mixer.Channel(3)
    ai1.set_volume(1)

    jumpscares = pygame.mixer.Sound("data/jumpscares.mp3")
    jumpscares1 = pygame.mixer.Channel(6)
    jumpscares1.set_volume(1)

    chave_insuficiente = pygame.mixer.Sound("data/chaveInsuficiente.wav")
    chave_insuficiente1 = pygame.mixer.Channel(1)
    chave_insuficiente1.set_volume(2)

    pegou = pygame.mixer.Sound("data/pegou.mp3")
    pegou1 = pygame.mixer.Channel(5)
    pegou1.set_volume(1)


    fugir = pygame.mixer.Sound("data/fugiu.mp3")
    fugir1 = pygame.mixer.Channel(0)
    fugir1.set_volume(1)

    gameover = pygame.mixer.Sound("data/gameover.mp3")
    gameover1 = pygame.mixer.Channel(1)
    gameover1.set_volume(1)

    # variaveis auxiliares

    playerx = player.rect.x
    playery = player.rect.y
    quantchave = 4
    passarporta = False
    direcaobolinha = 0

    visao = False
    gameLoopTela = True

    while gameLoopTela:
        clock.tick(60)

        #introducao1.play(introducao)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                #gameLoop = False
                exit()
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_l):
                    visao = True

                if event.key == pygame.K_UP:
                    direcaobolinha = 5
                    newBolinha1 = Bolinha(direcaobolinha, player, objectGroup, bolinha1Group)
                    newBolinha1.rect.center = player.rect.center

                if event.key == pygame.K_LEFT:
                    direcaobolinha = 1
                    newBolinha2 = Bolinha(direcaobolinha, player, objectGroup, bolinha2Group)
                    newBolinha2.rect.center = player.rect.center

                if event.key == pygame.K_RIGHT:
                    direcaobolinha = 3
                    newBolinha3 = Bolinha(direcaobolinha, player, objectGroup, bolinha3Group)
                    newBolinha3.rect.center = player.rect.center

                if event.key == pygame.K_DOWN:
                    direcaobolinha = 2
                    newBolinha4 = Bolinha(direcaobolinha, player, objectGroup, bolinha4Group)
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
            chaves1.kill()
            pegou1.play(pegou)
            quantchave -= 1

        chave2colission = pygame.sprite.spritecollide(player, chave2Group, False, pygame.sprite.collide_mask)
        if chave2colission:
            chaves2.kill()
            pegou1.play(pegou)
            quantchave -= 1

        chave3colission = pygame.sprite.spritecollide(player, chave3Group, False, pygame.sprite.collide_mask)
        if chave3colission:
            chaves3.kill()
            pegou1.play(pegou)
            quantchave -= 1

        chave4colission = pygame.sprite.spritecollide(player, chave4Group, False, pygame.sprite.collide_mask)
        if chave4colission:
            chaves4.kill()
            pegou1.play(pegou)
            quantchave -= 1

        if quantchave == 0:
            passarporta = True

        portacolission = pygame.sprite.spritecollide(player, portaGroup, False, pygame.sprite.collide_mask)
        if portacolission:
            player.rect.y = playery - 3
            if passarporta == True:
                fugirsom()
                gameLoopTela = False
            elif passarporta == False:
                chave_insuficiente1.play(chave_insuficiente)

        fantasmacolission = pygame.sprite.spritecollide(player, fantasmaGroup, False, pygame.sprite.collide_mask)
        if fantasmacolission:
            fantasma.kill()
            jumpscares1.play(jumpscares)
            gameoversom()
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

def fugirsom ():

    # music
    musicFundo = pygame.mixer.music.load("data/fugiu.mp3")
    pygame.mixer.music.play(1, 0.0, 5000)

    gameLoopTela = True

    while gameLoopTela:
        clock.tick(60)

        display.fill([30, 30, 30])
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE):
                    gameLoopTela = False



def gameoversom ():

    # music
    musicFundo = pygame.mixer.music.load("data/gameover.mp3")
    pygame.mixer.music.play(1, 0.0, 5000)

    gameLoopTela = True

    while gameLoopTela:
        clock.tick(60)

        display.fill([30, 30, 30])
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE):
                    gameLoopTela = False

def introducao ():

    # music
    musicFundo = pygame.mixer.music.load("data/introducao.mp3")
    pygame.mixer.music.play(1, 0.0, 5000)
    r = 30
    g = 30
    b = 30
    aux = 0
    auxR = True
    auxG = True
    auxB = True

    gameLoopTela = True

    while gameLoopTela:
        clock.tick(60)

        aux1 = random.randint(1, 3)
        aux += 1
#ver se esta dentro da faixa de cores
        if r > 248:
            auxR = False
        if g > 248:
            auxG = False
        if b > 248:
            auxB = False
        if r < 20:
            auxR = True
        if g < 20:
            auxG = True
        if b < 20:
            auxB = True

#algoritmo para mudar as cores
        if aux % 3 == 0 and auxR == True:
            r += 5 + aux1
        if aux % 3 == 0 and auxG == True:
            g += 3 + aux1
        if aux % 3 == 0 and auxB == True:
            b += 4 + aux1
        if aux % 3 == 0 and auxR == False:
            r -= 4 - aux1
        if aux % 3 == 0 and auxG == False:
            g -= 5 - aux1
        if aux % 3 == 0 and auxB == False:
            b -= 3 - aux1

        display.fill([r, g, b])
        pygame.display.update()

        for event in pygame.event.get():
            print("oi")
            if event.type == pygame.QUIT:
                #gameLoop = False
                exit()
            elif event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE):
                    gameLoopTela = False
                    print("oi")

if __name__ == "__main__":
    while gameLoop:
        introducao()
        criaObject()



#fugir = pygame.mixer.Sound("data/fugiu.wav")
    #fugir1 = pygame.mixer.Channel(0)
    #fugir1.set_volume(1)

