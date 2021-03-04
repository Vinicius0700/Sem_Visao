import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/Player.png")
        self.image = pygame.transform.scale(self.image, [6, 10])  # escalar de acordo com o display
        self.rect = self.image.get_rect()
        self.rect.x = 30
        self.rect.y = 30
        self.speed = 2

        self.aux = 0
        self.time = pygame.time.Clock()

        # sounds

        self.walk = pygame.mixer.Sound("data/Passos.wav")
        self.walk1 = pygame.mixer.Channel(4)
        self.walk1.set_volume(0.6)

    # Logica
    def update(self, *args):
        self.time.tick(60)
        self.walk1.set_volume(0.6)


        keys = pygame.key.get_pressed()

        #caso eu precise saber a localização do player
        #print("x -> ", self.rect.x, " y -> ", self.rect.y)

        if keys[pygame.K_d]:
            self.rect.x += self.speed

        if keys[pygame.K_a]:
           self.rect.x -= self.speed

        if keys[pygame.K_w]:
           self.rect.y -= self.speed

        if keys[pygame.K_s]:
           self.rect.y += self.speed

        if keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d] or keys[pygame.K_w]:
            if self.aux % 12 == 0:
                self.walk1.play(self.walk)
                self.aux += 1
            else:
                self.aux += 1
        else:
            self.aux = 0

        if self.rect.top < 18:
            self.rect.top = 18
        if self.rect.bottom > 638:
            self.rect.bottom = 638
        if self.rect.left < 18:
            self.rect.left = 18
        if self.rect.right > 798:
            self.rect.right = 798

