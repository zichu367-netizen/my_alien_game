import pygame

class AlienBullet:
    def __init__(self, screen, settings, alien):
        self.screen = screen
        self.settings = settings

        self.image = pygame.image.load("images/laser.png")
        self.image = pygame.transform.scale(self.image, (6, 20))

        self.rect = self.image.get_rect()
        self.rect.centerx = alien.rect.centerx
        self.rect.top = alien.rect.bottom

        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.alien_bullet_speed
        self.rect.y = self.y

    def draw(self):
        self.screen.blit(self.image, self.rect)
