import pygame
from skin_change import skin_change
import sqlite3
from end_window import gameover


class Start:
    def __init__(self):
        pygame.init()
        self.size = self.width, self.height = 720, 576
        self.screen = pygame.display.set_mode(self.size)
        self.background = pygame.image.load('wallpapersden.com_k-nebula-and-stars_1024x576.jpg')
        self.running = True

        self.game_name = 'Защитники космоса'

        pygame.display.set_caption(self.game_name)
        pygame_icon = pygame.image.load('инопланетянин (2) .png')
        pygame.display.set_icon(pygame_icon)

        self.name_color_inactive = (200, 20, 20)
        self.text_color = (50, 50, 255)
        self.color_active = (255, 0, 0)
        self.color = self.name_color_inactive
        self.btn_color_inactive = (120, 120, 120)
        self.btn_color_active = (170, 170, 170)
        self.BLACK = (0, 0, 0)
        self.skin_color_btn = self.btn_color_inactive
        self.start_color_btn = self.btn_color_inactive

        self.font_buttons = pygame.font.SysFont('Arial', 30)
        self.font_game_title = pygame.font.SysFont('Arial', 45)
        self.font_score = pygame.font.SysFont('Arial', 25)
        self.game_title = self.font_game_title.render(self.game_name, True, self.text_color)

        self.skin = 'основной персонаж (2) .png'
        self.image = pygame.image.load(self.skin)

        self.name_active = False
        self.name = 'Player'
        self.name_input_x = 530
        self.name_input_y = 70
        self.name_input = pygame.Rect(self.name_input_x, self.name_input_y, 150, 40)

        self.btn_width = 210
        self.btn_height = 75
        self.btn_y = 0.64 * self.height
        self.start_game_btn = pygame.Rect(100, self.btn_y, self.btn_width, self.btn_height)
        self.skin_change_btn = pygame.Rect(400, self.btn_y, self.btn_width, self.btn_height)
        self.start_text_btn = self.font_buttons.render('Начать игру', True, self.text_color)
        self.skin_text_btn = self.font_buttons.render('Сменить скин', True, self.text_color)

        self.con = sqlite3.connect('dog.sqlite')
        self.cur = self.con.cursor()
        self.req = 'SELECT * FROM scores'
        self.res = self.cur.execute(self.req).fetchall()
        self.score_sp = []
        for f in self.res:
            self.score_sp.append(f)
        self.score_sp.sort(key=lambda x: x[1], reverse=True)
        self.score_sp = self.score_sp[:10]
        self.score_x = 10
        self.score_y = 10

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
                if self.btn_y <= mouse_pos_y <= self.btn_y + self.btn_height:
                    if 100 <= mouse_pos_x <= 100 + self.btn_width:
                        self.start_color_btn = self.btn_color_active
                        if event.type == pygame.MOUSEBUTTONUP:
                            self.start()
                    else:
                        self.start_color_btn = self.btn_color_inactive
                    if 400 <= mouse_pos_x <= 400 + self.btn_width:
                        self.skin_color_btn = self.btn_color_active
                        if event.type == pygame.MOUSEBUTTONUP:
                            self.skin_change()
                    else:
                        self.skin_color_btn = self.btn_color_inactive
                else:
                    self.start_color_btn = self.btn_color_inactive
                    self.skin_color_btn = self.btn_color_inactive

                if self.name_input_y <= mouse_pos_y <= self.name_input_y + self.name_input.height:
                    if self.name_input_x <= mouse_pos_x <= self.name_input_x + self.name_input.width:
                        if event.type == pygame.MOUSEBUTTONUP:
                            self.color = self.color_active
                            self.name_active = True
                if self.name_active:
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_RETURN:
                            self.name_active = False
                            self.color = self.name_color_inactive
                        elif event.key == pygame.K_BACKSPACE:
                            self.name = self.name[:-1]

                        else:
                            if len(self.name) <= 7:
                                self.name += event.unicode

            pygame.display.flip()
            self.screen.fill(self.BLACK)
            self.screen.blit(self.background, (0, 0))

            pygame.draw.rect(self.screen, self.color, self.name_input, 2)
            pygame.draw.rect(self.screen, self.start_color_btn, self.start_game_btn)
            self.screen.blit(self.start_text_btn, (125, self.btn_y + 20))
            pygame.draw.rect(self.screen, self.skin_color_btn, self.skin_change_btn)
            self.screen.blit(self.skin_text_btn, (425, self.btn_y + 20))
            self.name_txt = self.font_buttons.render(self.name, True, self.text_color)
            self.screen.blit(self.name_txt, (self.name_input_x + 10, self.name_input_y + 2))
            self.screen.blit(self.game_title, (self.width // 4, 25))
            self.screen.blit(self.image, (630, self.btn_y))
            for text_score in self.score_sp:
                text_score = f'{text_score[0]} {text_score[1]}'
                text_score = self.font_score.render(text_score, True, self.text_color)
                self.screen.blit(text_score, (self.score_x, self.score_y))
                self.score_y += 25
            self.score_y = 10

    def start(self):
        from game_for_yandex import run
        score, name, skin = run(self.skin, self.name)
        gameover(score.stats.score, name, skin)
        self.con = sqlite3.connect('dog.sqlite')
        self.cur = self.con.cursor()
        self.req = 'SELECT * FROM scores'
        self.res = self.cur.execute(self.req).fetchall()
        self.score_sp = []
        for f in self.res:
            self.score_sp.append(f)
        self.score_sp.sort(key=lambda x: x[1], reverse=True)
        self.score_sp = self.score_sp[:10]

    def skin_change(self):
        self.skin_new = skin_change()
        if self.skin_new != None:
            self.skin = self.skin_new
        self.image = pygame.image.load(self.skin)


Start()
