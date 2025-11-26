import sys
import pygame
import random

from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from alien_bullet import AlienBullet

def run_game():
    pygame.init()
    settings = Settings()

    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion - Class Version")

    stats = GameStats()
    ship = Ship(screen, settings)

    bullets = []
    aliens = []
    alien_bullets = []

    # ---- 创建外星人队列 ----
    for x in range(100, 700, 80):
        aliens.append(Alien(screen, settings, x, 50))

    font = pygame.font.SysFont(None, 36)
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)

        # 事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stats.save_high_score()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    ship.moving_left = True
                elif event.key == pygame.K_RIGHT:
                    ship.moving_right = True
                elif event.key == pygame.K_SPACE:
                    if len(bullets) < settings.bullets_allowed:
                        bullets.append(Bullet(screen, settings, ship))
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    ship.moving_left = False
                elif event.key == pygame.K_RIGHT:
                    ship.moving_right = False

        ship.update()

        # 玩家子弹
        for b in bullets[:]:
            b.update()
            if b.rect.bottom < 0:
                bullets.remove(b)

        # 玩家击中外星人
        for b in bullets[:]:
            for al in aliens[:]:
                if b.rect.colliderect(al.rect):
                    bullets.remove(b)
                    aliens.remove(al)

                    stats.score += 10
                    stats.high_score = max(stats.high_score, stats.score)
                    break

        # 外星人移动
        for al in aliens:
            al.update()

        # 外星人边界反向
        for al in aliens:
            if al.rect.right >= settings.screen_width or al.rect.left <= 0:
                settings.fleet_direction *= -1
                for a2 in aliens:
                    a2.rect.y += settings.fleet_drop_speed
                break

        # 外星人射击
        for al in aliens:
            if random.randint(1, settings.alien_shoot_chance) == 1:
                alien_bullets.append(AlienBullet(screen, settings, al))

        # 外星人子弹移动
        for ab in alien_bullets[:]:
            ab.update()
            if ab.rect.top > settings.screen_height:
                alien_bullets.remove(ab)

            if ab.rect.colliderect(ship.rect):
                stats.save_high_score()
                sys.exit()

        # 绘制
        screen.fill(settings.bg_color)
        ship.draw()

        for b in bullets:
            b.draw()

        for al in aliens:
            al.draw()

        for ab in alien_bullets:
            ab.draw()

        score_img = font.render(f"Score: {stats.score}", True, (50, 50, 50))
        high_score_img = font.render(
            f"High Score: {stats.high_score}", True, (200, 0, 0)
        )
        screen.blit(score_img, (10, 10))
        screen.blit(high_score_img, (10, 50))

        pygame.display.flip()

run_game()
