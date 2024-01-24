import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        # создаем пулю в позиции пушки
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 5, 12)  # размеры пуль 0, 0 = координаты, ширина = 5, высота = 12
        self.color = 237, 28, 36
        self.speed = 4
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        # перемещение пули вверх
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        # рисуем пулю на экране
        pygame.draw.rect(self.screen, self.color, self.rect)
