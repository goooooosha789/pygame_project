import sys

import pygame


def gameover(score, name, skin):
    pygame.init()
    score_text = f'{name}: {score}'
    size = width, height = 720, 576
    screen = pygame.display.set_mode(size)
    fon = pygame.image.load('wallpapersden.com_k-nebula-and-stars_1024x576.jpg')

    skin = pygame.image.load(skin)
    rect = skin.get_rect()
    rect.center = width // 2, 150

    font_result = pygame.font.SysFont('Arial', 43)
    font_buttons = pygame.font.SysFont('Arial', 30)

    text_color = (200, 20, 20)
    btn_color_inactive = (120, 120, 120)
    btn_color_active = (170, 170, 170)
    BLACK = (0, 0, 0)
    end_color_btn = btn_color_inactive
    restart_color_btn = btn_color_inactive

    btn_width = 210
    btn_height = 75
    btn_y = 0.64 * height
    restart_game_btn = pygame.Rect(100, btn_y, btn_width, btn_height)
    restart_btn_click = False
    end_btn = pygame.Rect(400, btn_y, btn_width, btn_height)
    restart_text_btn = font_buttons.render('Начать заново', True, text_color)
    end_text_btn = font_buttons.render('Закрыть игру', True, text_color)

    result_txt = font_result.render(score_text, True, text_color)
    text_x = width // 2 - result_txt.get_width() // 2
    text_y = 50
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
            if btn_y <= mouse_pos_y <= btn_y + btn_height:
                if 100 <= mouse_pos_x <= 100 + btn_width:
                    restart_color_btn = btn_color_active
                    if event.type == pygame.MOUSEBUTTONUP:
                        return None
                else:
                    restart_color_btn = btn_color_inactive
                if 400 <= mouse_pos_x <= 400 + btn_width:
                    end_color_btn = btn_color_active
                    if event.type == pygame.MOUSEBUTTONUP:
                        end_game()
                else:
                    end_color_btn = btn_color_inactive
            else:
                restart_color_btn = btn_color_inactive
                end_color_btn = btn_color_inactive
        screen.fill(BLACK)
        screen.blit(fon, (0, 0))
        pygame.draw.rect(screen, restart_color_btn, restart_game_btn)
        screen.blit(restart_text_btn, (120, btn_y + 20))
        pygame.draw.rect(screen, end_color_btn, end_btn)
        screen.blit(end_text_btn, (425, btn_y + 20))
        screen.blit(result_txt, (text_x, text_y))
        screen.blit(skin, rect)
        pygame.display.flip()


def end_game():
    sys.exit()
