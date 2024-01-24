import pygame


class Alien(pygame.sprite.Sprite):  # класс одного пришельца

    def __init__(self, screen, stats):  # задаем начальную позицию
        super(Alien, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("инопланетянин (2) .png")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.level = stats.level

    def draw(self):  # вывод прешельца на экран
        self.screen.blit(self.image, self.rect)

    def update(self):  # перемещает пришельцев
        self.y += 0.01 + 0.01 * self.level  # 0.01
        self.rect.y = self.y
