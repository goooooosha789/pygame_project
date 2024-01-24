import pygame
from gun import Gun


class Scores():  # вывод игровой информации
    def __init__(self, screen, stats):  # инициализируем подсчет очков
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (237, 28, 36)
        self.font = pygame.font.Font(None, 20)
        self.image_score()
        self.image_lifes('lives.png')

    def image_score(self):
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_lifes(self, skin):
        self.lifes = pygame.sprite.Group()
        for life_count in range(self.stats.guns_left):
            life = Gun(self.screen, skin)
            life.rect.x = 15 + life_count * life.rect.width
            life.rect.y = 5
            self.lifes.add(life)

    def show_score(self):  # вывод счета на экран
        self.screen.blit(self.score_img, self.score_rect)
        self.lifes.draw(self.screen)
