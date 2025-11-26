import pygame

class Bullet:
    def __init__(self, screen, settings, ship):
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load("images/laser.png")
        self.image = pygame.transform.scale(self.image, (6, 20))

        self.rect = self.image.get_rect()
        self.rect.midbottom = ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw(self):
        self.screen.blit(self.image, self.rect)
