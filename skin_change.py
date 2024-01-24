import pygame


def skin_change():
    pygame.init()
    size = width, height = 720, 576
    screen = pygame.display.set_mode(size)
    fon = pygame.image.load('wallpapersden.com_k-nebula-and-stars_1024x576.jpg')
    running = True

    text_color = (200, 20, 20)
    btn_color_inactive = (120, 120, 120)
    btn_color_active = (170, 170, 170)
    btn_1_color = btn_color_inactive
    btn_2_color = btn_color_inactive
    btn_3_color = btn_color_inactive
    btn_4_color = btn_color_inactive
    btn_5_color = btn_color_inactive

    font_buttons = pygame.font.SysFont('Arial', 30)
    btn_txt = font_buttons.render('Выбрать', True, text_color)

    btn_y_down = 0.64 * height
    btn_y_up = 0.36 * height
    btn_x = 25
    btn_width = 185
    btn_height = 75
    btn_shift_x = width // 6
    btn_1_x = btn_x
    btn_2_x = btn_1_x + btn_shift_x
    btn_3_x = btn_2_x + btn_shift_x
    btn_4_x = btn_3_x + btn_shift_x
    btn_5_x = btn_4_x + btn_shift_x

    skin_1_btn = pygame.rect.Rect(btn_1_x, btn_y_down, btn_width, btn_height)
    skin_2_btn = pygame.rect.Rect(btn_2_x, btn_y_up, btn_width, btn_height)
    skin_3_btn = pygame.rect.Rect(btn_3_x, btn_y_down, btn_width, btn_height)
    skin_4_btn = pygame.rect.Rect(btn_4_x, btn_y_up, btn_width, btn_height)
    skin_5_btn = pygame.rect.Rect(btn_5_x, btn_y_down, btn_width, btn_height)

    skin_1 = 'основной персонаж (2) .png'
    skin_2 = 'зеленый скин (2).png'
    skin_3 = 'эчпочмак (2) .png'
    skin_4 = "Thor's hammer.png"
    skin_5 = 'skibidi_toilet.png'

    image_1 = pygame.image.load(skin_1)
    image_2 = pygame.image.load(skin_2)
    image_3 = pygame.image.load(skin_3)
    image_4 = pygame.image.load(skin_4)
    image_5 = pygame.image.load(skin_5)

    image_1_rect_x = skin_1_btn.centerx - image_1.get_width() // 2
    image_2_rect_x = skin_2_btn.centerx - image_2.get_width() // 2
    image_3_rect_x = skin_3_btn.centerx - image_3.get_width() // 2
    image_4_rect_x = skin_4_btn.centerx - image_4.get_width() // 2
    image_5_rect_x = skin_5_btn.centerx - image_5.get_width() // 2

    image_1_rect_y = height // 2
    image_2_rect_y = height // 5
    image_3_rect_y = height // 2
    image_4_rect_y = height // 5
    image_5_rect_y = height // 2

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            mouse_pos_x, mouse_pos_y = pygame.mouse.get_pos()
            if btn_y_down <= mouse_pos_y <= btn_y_down + btn_height:
                if btn_1_x <= mouse_pos_x <= btn_1_x + btn_width:
                    btn_1_color = btn_color_active
                    if event.type == pygame.MOUSEBUTTONUP:
                        return skin_1
                else:
                    btn_1_color = btn_color_inactive
                if btn_3_x <= mouse_pos_x <= btn_3_x + btn_width:
                    btn_3_color = btn_color_active
                    if event.type == pygame.MOUSEBUTTONUP:
                        return skin_3
                else:
                    btn_3_color = btn_color_inactive
                if btn_5_x <= mouse_pos_x <= btn_5_x + btn_width:
                    btn_5_color = btn_color_active
                    if event.type == pygame.MOUSEBUTTONUP:
                        return skin_5
                else:
                    btn_5_color = btn_color_inactive

            else:
                btn_1_color = btn_color_inactive
                btn_3_color = btn_color_inactive
                btn_5_color = btn_color_inactive
            if btn_y_up <= mouse_pos_y <= btn_y_up + btn_height:
                if btn_2_x <= mouse_pos_x <= btn_2_x + btn_width:
                    btn_2_color = btn_color_active
                    if event.type == pygame.MOUSEBUTTONUP:
                        return skin_2
                else:
                    btn_2_color = btn_color_inactive
                if btn_4_x <= mouse_pos_x <= btn_4_x + btn_width:
                    btn_4_color = btn_color_active
                    if event.type == pygame.MOUSEBUTTONUP:
                        return skin_4
                else:
                    btn_4_color = btn_color_inactive
            else:
                btn_2_color = btn_color_inactive
                btn_4_color = btn_color_inactive

        pygame.display.flip()
        screen.blit(fon, (0, 0))
        pygame.draw.rect(screen, btn_1_color, skin_1_btn)
        pygame.draw.rect(screen, btn_2_color, skin_2_btn)
        pygame.draw.rect(screen, btn_3_color, skin_3_btn)
        pygame.draw.rect(screen, btn_4_color, skin_4_btn)
        pygame.draw.rect(screen, btn_5_color, skin_5_btn)
        screen.blit(btn_txt, (btn_1_x + 35, btn_y_down + 15))
        screen.blit(btn_txt, (btn_2_x + 35, btn_y_up + 15))
        screen.blit(btn_txt, (btn_3_x + 35, btn_y_down + 15))
        screen.blit(btn_txt, (btn_4_x + 35, btn_y_up + 15))
        screen.blit(btn_txt, (btn_5_x + 35, btn_y_down + 15))
        screen.blit(image_1, (image_1_rect_x, image_1_rect_y))
        screen.blit(image_2, (image_2_rect_x, image_2_rect_y))
        screen.blit(image_3, (image_3_rect_x, image_3_rect_y))
        screen.blit(image_4, (image_4_rect_x, image_4_rect_y))
        screen.blit(image_5, (image_5_rect_x, image_5_rect_y))

# skin_change()
