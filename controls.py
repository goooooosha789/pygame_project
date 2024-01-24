import pygame
import sys
from bullet import Bullet
from alien import Alien
import time


def events(screen, gun, buletts):
    """обработка событий"""

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            # начало движения вправо
            if event.key in (pygame.K_d, pygame.K_RIGHT):
                gun.mright = True
            elif event.key in (pygame.K_a, pygame.K_LEFT):
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                buletts.add(new_bullet)
        elif event.type == pygame.KEYUP:
            # вправо
            if event.key in (pygame.K_d, pygame.K_RIGHT):
                gun.mright = False
                # начало движения влево
            elif event.key in (pygame.K_a, pygame.K_LEFT):
                gun.mleft = False


def update(bg_color, screen, stats, sc, gun, aliens, bullets, fon):
    """обновление экрана"""
    sp_fons = fon
    screen.fill(bg_color)
    screen.blit(sp_fons[stats.level % len(sp_fons)], (0, 0))
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    aliens.draw(screen)
    pygame.display.flip()


def update_bullets(screen, stats, sc, aliens, bullets, width, height, skin):
    # обновлять позиции пуль
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += 10 * len(aliens)  # 10

        sc.image_score()
        sc.image_lifes('lives.png')
    if len(aliens) == 0:
        stats.level += 1
        bullets.empty()
        create_army(screen, aliens, width, height, stats)


def gun_kill(stats, screen, sc, gun, aliens, bullets, width, height, skin):  # столкновение пушки с прешельцем
    if stats.guns_left > 0:
        stats.guns_left -= 1
        image = pygame.image.load('boom.png')
        rect = image.get_rect()
        rect.centerx = gun.rect.centerx
        rect.centery = gun.rect.centery
        screen.blit(image, rect)
        pygame.display.flip()
        time.sleep(1)
        sc.image_lifes('lives.png')
        aliens.empty()
        bullets.empty()
        create_army(screen, aliens, width, height, stats)
        gun.create_gun()
        time.sleep(1)
    else:
        image = pygame.image.load('boom.png')
        rect = image.get_rect()
        rect.centerx = gun.rect.centerx
        rect.centery = gun.rect.centery
        screen.blit(image, rect)
        pygame.display.flip()
        stats.level = 0
        time.sleep(1)
        stats.run_game = False


def update_aliens(stats, screen, sc, gun, aliens, bullets, width, height, skin):  # обновляет позицию прешельцев
    aliens.update()
    if pygame.sprite.spritecollideany(gun, aliens):
        gun_kill(stats, screen, sc, gun, aliens, bullets, width, height, skin)
    aliens_check(stats, screen, sc, gun, aliens, bullets, width, height, skin)


def aliens_check(stats, screen, sc, gun, aliens, bullets, wight, height, skin):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, sc, gun, aliens, bullets, wight, height, skin)
            break


def create_army(screen, aliens, width, height, stats):  # создание армии прешельцев
    alien = Alien(screen, stats)
    alien_width = alien.rect.width + 5
    number_alien_x = int((width - 2 * alien_width) / alien_width)
    alien_height = alien.rect.height + 5
    number_alien_y = int((height - 100 - 2 * alien_height) / alien_height)

    for row_number in range(number_alien_y - 2):
        for alien_number in range(number_alien_x):
            alien = Alien(screen, stats)
            alien.x = alien_width + (alien_width * alien_number)
            alien.y = alien_height + (alien_height * row_number)
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + alien.rect.height * row_number
            aliens.add(alien)
