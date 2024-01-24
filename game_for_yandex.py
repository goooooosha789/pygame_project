import pygame
import controls
from end_window import gameover
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores
import sqlite3


def run(skin='основной персонаж (2) .png', name='Player'):
    pygame.init()
    name = name
    skin = skin
    size = width, height = 720, 576
    screen = pygame.display.set_mode(size)

    images = ['wallpapersden.com_k-nebula-and-stars_1024x576.jpg', 'fotooboikosmos.(8).sm.jpg', 'scale_1200.jpg',
              'setwalls.ru-60792-1024x576.jpg', '6152420882_84e7c5a57f_b.jpg']
    fons = []
    for image in images:
        fon = pygame.image.load(image)
        fons.append(fon)
    bg_color = (0, 0, 0)
    gun = Gun(screen, skin)
    bullets = Group()
    aliens = Group()
    stats = Stats()
    sc = Scores(screen, stats)
    controls.create_army(screen, aliens, width, height, stats)

    while True:

        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            controls.update(bg_color, screen, stats, sc, gun, aliens, bullets,
                            fons)
            controls.update_bullets(screen, stats, sc,
                                    aliens, bullets, width, height, skin)
            controls.update_aliens(stats, screen, sc,
                                   gun, aliens, bullets, width, height, skin)
        else:
            con = sqlite3.connect('dog.sqlite')
            cur_2 = con.cursor()
            result_2 = cur_2.execute('Select * From scores').fetchall()
            not_have = True
            for i in result_2:
                if i[0] == name:
                    cur_3 = con.cursor()
                    record = max(i[1], sc.stats.score)
                    update = cur_3.execute(f"UPDATE scores SET score = {record} WHERE name = '{name}'")
                    not_have = False
                    break
            if not_have:
                cur = con.cursor()
                result = cur.execute(f"INSERT INTO scores(name, score) VALUES('{str(name)}', {stats.score})")
            con.commit()
            con.close()
            return sc, name, skin
