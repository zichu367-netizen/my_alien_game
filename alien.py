import pygame

class Alien:
    def __init__(self, screen, settings, x, y):
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load("images/alien.png")
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def draw(self):
        self.screen.blit(self.image, self.rect)
