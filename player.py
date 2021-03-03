import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/Player.png")
        self.image = pygame.transform.scale(self.image, [6, 10])  # escalar de acordo com o display
        self.rect = self.image.get_rect()
        self.rect.x = 30
        self.rect.y = 30

        self.aux = 0
        self.time = pygame.time.Clock()

        # sounds

        # walk = pygame.mixer.Sound("data/Passos.wav")
        # walk.set_volume(0.1)
        self.walk = pygame.mixer.Sound("data/Passos.wav")
        self.walk1 = pygame.mixer.Channel(1)
        self.walk1.set_volume(0.6)

    # Logica
    def update(self, *args):
        self.time.tick(60)


        keys = pygame.key.get_pressed()

        #print("x -> ", self.rect.x, " y -> ", self.rect.y)

        if keys[pygame.K_d]:
            self.rect.x += 8

        if keys[pygame.K_a]:
           self.rect.x -= 8

        if keys[pygame.K_w]:
           self.rect.y -= 8

        if keys[pygame.K_s]:
           self.rect.y += 8

        if keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d] or keys[pygame.K_w]:
            if self.aux % 12 == 0:
                self.walk1.play(self.walk)
                self.aux += 1
            else:
                self.aux += 1
        else:
            self.aux = 0

        if self.rect.top < 20:
            self.rect.top = 20
        if self.rect.bottom > 640:
            self.rect.bottom = 640
        if self.rect.left < 20:
            self.rect.left = 20
        if self.rect.right > 800:
            self.rect.right = 800

