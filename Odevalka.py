import pygame
from pygame.locals import *

pygame.init()

# Окно
WIDTH, HEIGHT = 720, 1400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Фон
background = pygame.image.load('Фон2.jpg').convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Кукла
doll = pygame.image.load('Кукла.png').convert_alpha()
doll = pygame.transform.scale(doll, (270 // 1.2, 922 // 1.2))
logo = pygame.transform.scale(pygame.image.load('Логотип.png').convert_alpha(), (577 // 6, 433 // 6))
# Звук
Dressound = pygame.mixer.Sound("Одежды.ogg")

# вешалка
veshalka1 = pygame.transform.scale(pygame.image.load('Вешалка1.png').convert_alpha(), (500 // 6, 500 // 6))
veshalka2 = pygame.transform.scale(pygame.image.load('Вешалкабрюки.png').convert_alpha(), (500 // 6, 500 // 6))
veshalka3 = pygame.transform.scale(pygame.image.load('Вешалкашапка.png').convert_alpha(), (500 // 8, 500 // 8))
veshalka4 = pygame.transform.scale(pygame.image.load('Вешалкабантик2.png').convert_alpha(), (521 // 12, 479 // 12))
polka = pygame.transform.scale(pygame.image.load('Полка.png').convert_alpha(), (85 * 2.9, 238 // 1.3))

polka4 = pygame.transform.scale(pygame.image.load('Полка4.png').convert_alpha(), (313 // 1.5, 96 // 1.5))
# Одежда (маленькие иконки)
doll_small = pygame.transform.scale(pygame.image.load('Долл.png').convert_alpha(), (141 // 2, 270 // 2))

# 1. БАШ КИЙИМ:
jashilkepka_small = pygame.transform.scale(pygame.image.load('Тумак/Жашылкепка.png').convert_alpha(), (54 * 1.5,  41 * 1.5))
kizilshlyapa_small = pygame.transform.scale(pygame.image.load('Тумак/Кызылшляпа.png').convert_alpha(), (48 * 1.4,  41 * 1.4))
shapka_small = pygame.transform.scale(pygame.image.load('Тумак/Шапка.png').convert_alpha(), (581 // 10,  429 // 10))
shlyapa_small = pygame.transform.scale(pygame.image.load('Тумак/Шляпа.png').convert_alpha(), (569 // 9,  343 // 9))
tumak_small = pygame.transform.scale(pygame.image.load('Тумак/Акшляпа.png').convert_alpha(), (160 // 3,  124 // 3))
tumak1_small = pygame.transform.scale(pygame.image.load('Тумак/Карашляпа.png').convert_alpha(), (231 // 4,  182 // 4))
tumak2_small = pygame.transform.scale(pygame.image.load('Тумак/Сарышляпа.png').convert_alpha(), (190 // 3,  136 // 3))
tumak3_small = pygame.transform.scale(pygame.image.load('Тумак/Тумак.png').convert_alpha(), (301 // 5,  193 // 5))

# 2. КӨЙНӨКТӨР:
akoinok_small = pygame.transform.scale(pygame.image.load('Койнок/Аккойнок1.png').convert_alpha(), (438 // 5, 570 // 5))

zebrakoinok_small = pygame.transform.scale(pygame.image.load('Койнок/Зебракойнок.png').convert_alpha(), (356 // 3.7, 701 // 3.7))

kemsel_small = pygame.transform.scale(pygame.image.load('Жемпер/Кемсел.png').convert_alpha(), (427 // 4, 584 // 4))

jashiljemper_small = pygame.transform.scale(pygame.image.load('Жемпер/Каражемпер.png').convert_alpha(), (427 // 4.5, 584 // 4.5))

sarijemper_small = pygame.transform.scale(pygame.image.load('Жемпер/Сарыжемпер.png').convert_alpha(), (458 // 4.5, 545 // 4.5))

kokoinok_small = pygame.transform.scale(pygame.image.load('Койнок/Кокойнок.png').convert_alpha(), (438 // 4.9, 570 // 4.9))

kizilkoinok_small = pygame.transform.scale(pygame.image.load('Койнок/Кызылкойнок.png').convert_alpha(), (48*3.5, 48*3.5))

purpurkoinok_small = pygame.transform.scale(pygame.image.load('Койнок/Пурпуркойнок.png').convert_alpha(), (396 // 3.6, 629 // 3.6))

karakoinok_small = pygame.transform.scale(pygame.image.load('Койнок/Каракойнок.png').convert_alpha(), (66 * 1.5, 117 * 1.5))

sarikoinok_small = pygame.transform.scale(pygame.image.load('Койнок/Сарыкойнок.png').convert_alpha(), (475 // 4, 526 // 4))

kizillyamka_small = pygame.transform.scale(pygame.image.load('Койнок/Кызыллямка.png').convert_alpha(), (63 * 1.6, 108 * 1.6))



# 3. ШЫМДАР:
jashilshim_small = pygame.transform.scale(pygame.image.load('Шым/Жашылшым.png').convert_alpha(), (362 // 5, 688 // 5))
kokshim_small = pygame.transform.scale(pygame.image.load('Шым/Кокшым.png').convert_alpha(), (364 // 5, 686 // 5))
akshim_small = pygame.transform.scale(pygame.image.load('Шым/Акшым.png').convert_alpha(), (430 // 4.2, 580 // 4.2))
bozshim_small = pygame.transform.scale(pygame.image.load('Шым/Бозшым.png').convert_alpha(), (402 // 4.5, 620 // 4.5))
jinsi_small = pygame.transform.scale(pygame.image.load('Шым/Джинсы1.png').convert_alpha(), (432 // 4, 576 // 4))
klesh_small = pygame.transform.scale(pygame.image.load('Шым/Шорта2.png').convert_alpha(), (548 // 7, 456 // 7))

karayubka_small = pygame.transform.scale(pygame.image.load('Юбка/Караюбка.png').convert_alpha(), (460 // 7, 542 // 7))
sariyubka_small = pygame.transform.scale(pygame.image.load('Юбка/Сарыюбка.png').convert_alpha(), (70, 102))
yubka_small = pygame.transform.scale(pygame.image.load('Юбка/Акюбка.png').convert_alpha(), (370 // 4.5, 481 // 4.5))
yubka1_small = pygame.transform.scale(pygame.image.load('Юбка/Жашылюбка.png').convert_alpha(), (445 // 7, 561 // 7))
yubka2_small = pygame.transform.scale(pygame.image.load('Юбка/Кызылюбка.png').convert_alpha(), (370 // 4.2, 480 // 4.2))
yubka3_small = pygame.transform.scale(pygame.image.load('Юбка/Кызылюбка1.png').convert_alpha(), (348 // 4.2, 367 // 4.2))

# 4. БУТ КИЙИМДЕР:
bozsapog_small = pygame.transform.scale(pygame.image.load('Ботинке/Бозсапог.png').convert_alpha(), (283 // 3, 309 // 3))
sapog_small = pygame.transform.scale(pygame.image.load('Ботинке/Сапог.png').convert_alpha(), (297 // 3, 211 // 3))

karabuts_small = pygame.transform.scale(pygame.image.load('Ботинке/Карабутс.png').convert_alpha(), (297 // 3, 156 // 3))

kokbuts_small = pygame.transform.scale(pygame.image.load('Ботинке/Кокбутс.png').convert_alpha(), (280 // 3, 181 // 3))

kizilbuts_small = pygame.transform.scale(pygame.image.load('Ботинке/Кызылбутс.png').convert_alpha(), (269 // 3, 169 // 3))



# 5. АКСЕССУАРЛАР:
ochka_small = pygame.transform.scale(pygame.image.load('Очки/Очка.png').convert_alpha(), (348 // 8, 196 // 8))
ochka1_small = pygame.transform.scale(pygame.image.load('Очки/Очка1.png').convert_alpha(), (191 // 3.6, 102 // 3.6))
ochka2_small = pygame.transform.scale(pygame.image.load('Очки/Очка2.png').convert_alpha(), (354 // 7.1, 236 // 7.1))

sumka_small = pygame.transform.scale(pygame.image.load('Сумка/Сумка.png').convert_alpha(), (337 // 5, 277 // 5))
sumka1_small = pygame.transform.scale(pygame.image.load('Сумка/Колсумка.png').convert_alpha(), (198 // 3, 163 // 3))
sumka2_small = pygame.transform.scale(pygame.image.load('Сумка/Кызылсумка.png').convert_alpha(), (264 // 4, 187 // 4))
sumka3_small = pygame.transform.scale(pygame.image.load('Сумка/Кошелек.png').convert_alpha(), (430 // 8, 280 // 8))

jashilbantik_small = pygame.transform.scale(pygame.image.load('Бантик/Жашылбантик.png').convert_alpha(), (246 // 3.8, 223 // 3.8))

kizilbantik_small = pygame.transform.scale(pygame.image.load('Бантик/Кызылбантик.png').convert_alpha(), (30 * 2.5, 25 * 2.5))
bantik_small = pygame.transform.scale(pygame.image.load('Бантик/Бантик.png').convert_alpha(), (164 // 2.2, 119 // 2.2))
bantik1_small = pygame.transform.scale(pygame.image.load('Бантик/Бантик1.png').convert_alpha(), (163 // 2.2, 124 // 2.2))
bantik2_small = pygame.transform.scale(pygame.image.load('Бантик/Бантик2.png').convert_alpha(), (146 // 2.2, 104 // 2.2))
bantik3_small = pygame.transform.scale(pygame.image.load('Бантик/Бантик3.png').convert_alpha(), (159 // 2.2, 104 // 2.2))
bantik4_small = pygame.transform.scale(pygame.image.load('Бантик/Бантик4.png').convert_alpha(), (178 // 2.2, 148 // 2.2))
bantik5_small = pygame.transform.scale(pygame.image.load('Бантик/Бантик5.png').convert_alpha(), (146 // 2, 96 // 2))

# Одежда (большой размер)

doll_big = pygame.transform.scale(pygame.image.load('Кукла.png').convert_alpha(), (270 // 1.2, 922 // 1.2))

# 1. БАШ КИЙИМ:
jashilkepka_big = pygame.transform.scale(pygame.image.load('Тумак/Жашылкепка.png').convert_alpha(), (54 * 5,  41 * 4))
kizilshlyapa_big = pygame.transform.scale(pygame.image.load('Тумак/Кызылшляпа.png').convert_alpha(), (48 * 4,  41 * 4))
shapka_big = pygame.transform.scale(pygame.image.load('Тумак/Шапка.png').convert_alpha(), (581 // 2.8,  429 // 2.5))
shlyapa_big = pygame.transform.scale(pygame.image.load('Тумак/Шляпа.png').convert_alpha(), (569 // 2.8,  343 // 2.8))
tumak_big = pygame.transform.scale(pygame.image.load('Тумак/Акшляпа.png').convert_alpha(), (160 * 1.2,  124 * 1.2))
tumak1_big = pygame.transform.scale(pygame.image.load('Тумак/Карашляпа.png').convert_alpha(), (231 // 1.2,  182 // 1.2))
tumak2_big = pygame.transform.scale(pygame.image.load('Тумак/Сарышляпа.png').convert_alpha(), (190 // 1,  136 // 1))
tumak3_big = pygame.transform.scale(pygame.image.load('Тумак/Тумак.png').convert_alpha(), (301 // 1.33,  193 // 1.35))

# 2. КӨЙНӨКТӨР:
akoinok_big = pygame.transform.scale(pygame.image.load('Койнок/Аккойнок1.png').convert_alpha(), (438 // 2.8, 570 // 2.9))

zebrakoinok_big= pygame.transform.scale(pygame.image.load('Койнок/Зебракойнок.png').convert_alpha(), (356 // 2, 701 // 2))

kemsel_big = pygame.transform.scale(pygame.image.load('Жемпер/Кемсел.png').convert_alpha(), (427 // 2.3, 584 // 2.6))

jashiljemper_big = pygame.transform.scale(pygame.image.load('Жемпер/Каражемпер.png').convert_alpha(), (427 // 2.16, 584 // 2.8))

sarijemper_big = pygame.transform.scale(pygame.image.load('Жемпер/Сарыжемпер.png').convert_alpha(), (458 // 2.13, 545 // 2.2))

kokoinok_big = pygame.transform.scale(pygame.image.load('Койнок/Кокойнок.png').convert_alpha(), (438 // 3.1, 570 // 2.8))

kizilkoinok_big = pygame.transform.scale(pygame.image.load('Койнок/Кызылкойнок.png').convert_alpha(), (48*7.5, 48*7))

purpurkoinok_big = pygame.transform.scale(pygame.image.load('Койнок/Пурпуркойнок.png').convert_alpha(), (396 // 1.75, 629 // 1.9))

karakoinok_big = pygame.transform.scale(pygame.image.load('Койнок/Каракойнок.png').convert_alpha(), (66 * 2.7, 117 * 2.3))

sarikoinok_big = pygame.transform.scale(pygame.image.load('Койнок/Сарыкойнок.png').convert_alpha(), (475 // 2.35, 526 // 2.4))

kizillyamka_big = pygame.transform.scale(pygame.image.load('Койнок/Кызыллямка.png').convert_alpha(), (63 * 3, 108 * 3))

# 3. ШЫМДАР:
jashilshim_big = pygame.transform.scale(pygame.image.load('Шым/Жашылшым.png').convert_alpha(), (362 // 2, 688 // 2.1))
kokshim_big = pygame.transform.scale(pygame.image.load('Шым/Кокшым.png').convert_alpha(), (364 // 1.94, 686 // 1.9))

akshim_big = pygame.transform.scale(pygame.image.load('Шым/Акшым.png').convert_alpha(), (430 // 1.5, 580 // 1.7))
bozshim_big = pygame.transform.scale(pygame.image.load('Шым/Бозшым.png').convert_alpha(), (402 // 1.7, 620 // 1.8))
jinsi_big = pygame.transform.scale(pygame.image.load('Шым/Джинсы1.png').convert_alpha(), (432 // 1.8, 576 // 1.8))
klesh_big = pygame.transform.scale(pygame.image.load('Шым/Шорта2.png').convert_alpha(), (548 // 3.95, 456 // 3.9))

karayubka_big = pygame.transform.scale(pygame.image.load('Юбка/Караюбка.png').convert_alpha(), (460 // 2.72, 542 // 2.72))
sariyubka_big = pygame.transform.scale(pygame.image.load('Юбка/Сарыюбка.png').convert_alpha(), (70 * 3.3, 102 * 2))
yubka_big = pygame.transform.scale(pygame.image.load('Юбка/Акюбка.png').convert_alpha(), (370 // 1.5, 481 // 1.5))
yubka1_big = pygame.transform.scale(pygame.image.load('Юбка/Жашылюбка.png').convert_alpha(), (445 // 2.9, 561 // 2.9))
yubka2_big = pygame.transform.scale(pygame.image.load('Юбка/Кызылюбка.png').convert_alpha(), (370 // 1.32, 480 // 1.32))
yubka3_big = pygame.transform.scale(pygame.image.load('Юбка/Кызылюбка1.png').convert_alpha(), (348 // 1.2, 367 // 1))

# 4. БУТ КИЙИМДЕР:
bozsapog_big = pygame.transform.scale(pygame.image.load('Ботинке/Бозсапог.png').convert_alpha(), (283 // 2.73, 309 // 2.85))
sapog_big = pygame.transform.scale(pygame.image.load('Ботинке/Сапог.png').convert_alpha(), (297 // 2.8, 211 // 2.8))

karabuts_big = pygame.transform.scale(pygame.image.load('Ботинке/Карабутс.png').convert_alpha(), (297 // 2.9, 156 // 2.4))

kokbuts_big = pygame.transform.scale(pygame.image.load('Ботинке/Кокбутс.png').convert_alpha(), (280 // 2.9, 181 // 2.4))

kizilbuts_big = pygame.transform.scale(pygame.image.load('Ботинке/Кызылбутс.png').convert_alpha(), (269 // 2.7, 169 // 2.3))



# 5. АКСЕССУАРЛАР:
ochka_big = pygame.transform.scale(pygame.image.load('Очки/Очка.png').convert_alpha(), (348 // 3, 196 // 3))
ochka1_big = pygame.transform.scale(pygame.image.load('Очки/Очка1.png').convert_alpha(), (191 // 1.46, 102 // 1.46))
ochka2_big = pygame.transform.scale(pygame.image.load('Очки/Очка2.png').convert_alpha(), (354 // 3.1, 236 // 3.1))


sumka_big = pygame.transform.scale(pygame.image.load('Сумка/Сумка.png').convert_alpha(), (337 // 4, 277 // 4))
sumka1_big = pygame.transform.scale(pygame.image.load('Сумка/Колсумка.png').convert_alpha(), (198 // 2, 163 // 2))
sumka2_big = pygame.transform.scale(pygame.image.load('Сумка/Кызылсумка.png').convert_alpha(), (264 // 3, 187 // 3))
sumka3_big = pygame.transform.scale(pygame.image.load('Сумка/Кошелек.png').convert_alpha(), (430 // 5, 280 // 5))

jashilbantik_big = pygame.transform.scale(pygame.image.load('Бантик/Жашылбантик.png').convert_alpha(), (246 // 2,  223 // 2))
kizilbantik_big = pygame.transform.scale(pygame.image.load('Бантик/Кызылбантик.png').convert_alpha(), (30 * 3, 25 * 3))
bantik_big = pygame.transform.scale(pygame.image.load('Бантик/Бантик.png').convert_alpha(), (164 // 2, 119 // 2))
bantik1_big = pygame.transform.scale(pygame.image.load('Бантик/Бантик1.png').convert_alpha(), (163 // 2, 124 // 2))
bantik2_big = pygame.transform.scale(pygame.image.load('Бантик/Бантик2.png').convert_alpha(), (146 // 2, 104 // 2))
bantik3_big = pygame.transform.scale(pygame.image.load('Бантик/Бантик3.png').convert_alpha(), (159 // 2, 104 // 2))
bantik4_big  = pygame.transform.scale(pygame.image.load('Бантик/Бантик4.png').convert_alpha(), (178 // 2, 148 // 2))
bantik5_big = pygame.transform.scale(pygame.image.load('Бантик/Бантик5.png').convert_alpha(), (146 // 2, 96 // 2))

# Начальные позиции маленьких иконок
doll_rect = doll_small.get_rect(topleft=(128, 140))
# 1. БАШ КИЙИМ:
jashilkepka_rect = jashilkepka_small.get_rect(topleft=(1, 18))
kizilshlyapa_rect = kizilshlyapa_small.get_rect(topleft=(100, 12))
shapka_rect = shapka_small.get_rect(topleft=(184, 19))
shlyapa_rect = shlyapa_small.get_rect(topleft=(261, 22))
tumak_rect = tumak_small.get_rect(topleft=(392, 22))
tumak1_rect = tumak1_small.get_rect(topleft=(472, 22))
tumak2_rect = tumak2_small.get_rect(topleft=(551, 22))
tumak3_rect = tumak3_small.get_rect(topleft=(634, 22))

# 2. КӨЙНӨКТӨР:
akoinok_rect = akoinok_small.get_rect(topleft=(9, 127))

zebrakoinok_rect = zebrakoinok_small.get_rect(topleft=(114, 913))

kemsel_rect = kemsel_small.get_rect(topleft=(0, 385))
jashiljemper_rect = jashiljemper_small.get_rect(topleft=(6, 870))
sarijemper_rect = sarijemper_small.get_rect(topleft=(0, 1000))

kokoinok_rect = kokoinok_small.get_rect(topleft=(7, 260))

kizilkoinok_rect = kizilkoinok_small.get_rect(topleft=(75, 530))

purpurkoinok_rect = purpurkoinok_small.get_rect(topleft=(98, 342))

karakoinok_rect = karakoinok_small.get_rect(topleft=(110, 710))

sarikoinok_rect = sarikoinok_small.get_rect(topleft=(0, 545))

kizillyamka_rect = kizillyamka_small.get_rect(topleft=(8, 690))

# 3. ШЫМДАР:
jashilshim_rect = jashilshim_small.get_rect(topleft=(507, 157))
kokshim_rect = kokshim_small.get_rect(topleft=(605, 154))
akshim_rect = akshim_small.get_rect(topleft=(490, 330))
bozshim_rect = bozshim_small.get_rect(topleft=(595, 334))
jinsi_rect = jinsi_small.get_rect(topleft=(489, 515))
klesh_rect = klesh_small.get_rect(topleft=(602, 520))
karayubka_rect = karayubka_small.get_rect(topleft=(609, 690))
sariyubka_rect = sariyubka_small.get_rect(topleft=(507, 687))
yubka_rect = yubka_small.get_rect(topleft=(500, 830))
yubka1_rect = yubka1_small.get_rect(topleft=(611, 835))
yubka2_rect = yubka2_small.get_rect(topleft=(499, 945))
yubka3_rect = yubka3_small.get_rect(topleft=(602, 947))

# 4. БУТ КИЙИМДЕР:
bozsapog_rect = bozsapog_small.get_rect(topleft=(480, 1192))

sapog_rect = sapog_small.get_rect(topleft=(590, 1225))

karabuts_rect = karabuts_small.get_rect(topleft=(625, 1130))

kokbuts_rect = kokbuts_small.get_rect(topleft=(540, 1123))

kizilbuts_rect = kizilbuts_small.get_rect(topleft=(460, 1123))



# 5. АКСЕССУАРЛАР:
ochka_rect = ochka_small.get_rect(topleft=(270, 451))
ochka1_rect = ochka1_small.get_rect(topleft=(326, 449))
ochka2_rect = ochka2_small.get_rect(topleft=(390, 447))
sumka_rect = sumka_small.get_rect(topleft=(280, 494))
sumka1_rect = sumka1_small.get_rect(topleft=(365, 491))
sumka2_rect = sumka2_small.get_rect(topleft=(280, 565))
sumka3_rect = sumka3_small.get_rect(topleft=(370, 577))

jashilbantik_rect = jashilbantik_small.get_rect(topleft=(282, 105))

kizilbantik_rect = kizilbantik_small.get_rect(topleft=(352, 112))
bantik_rect = bantik_small.get_rect(topleft=(254, 170))
bantik1_rect = bantik1_small.get_rect(topleft=(245, 231))
bantik2_rect = bantik2_small.get_rect(topleft=(242, 300))
bantik3_rect = bantik3_small.get_rect(topleft=(378, 176))
bantik4_rect = bantik4_small.get_rect(topleft=(385, 230))
bantik5_rect = bantik5_small.get_rect(topleft=(392, 300))

# Позиции на кукле
doll_target = pygame.Rect(239, 645, 200, 300)
# 1. БАШ КИЙИМ:
jashilkepka_target = pygame.Rect(179, 650, 200, 200)
kizilshlyapa_target = pygame.Rect(258, 620, 200, 200)
shapka_target = pygame.Rect(250, 625, 200, 200)
shlyapa_target = pygame.Rect(252, 655, 200, 200)
tumak_target = pygame.Rect(268, 641, 200, 200)
tumak1_target = pygame.Rect(262, 640, 200, 200)
tumak2_target = pygame.Rect(260, 650, 200, 200)
tumak3_target = pygame.Rect(237, 635, 200, 200)
# 2. КӨЙНӨКТӨР:
akoinok_target = pygame.Rect(276, 855, 200, 300)
zebrakoinok_target = pygame.Rect(265, 856, 200, 300)
kemsel_target = pygame.Rect(262, 846, 200, 300)
jashiljemper_target = pygame.Rect(256, 853, 200, 300)
sarijemper_target = pygame.Rect(245, 837, 200, 300)
kokoinok_target = pygame.Rect(284, 854, 200, 300)
kizilkoinok_target = pygame.Rect(175, 854, 200, 300)
purpurkoinok_target = pygame.Rect(240, 847, 200, 300)
karakoinok_target = pygame.Rect(265, 873, 200, 300)
sarikoinok_target = pygame.Rect(253, 853, 200, 300)
kizillyamka_target = pygame.Rect(259, 860, 200, 300)

# 3. ШЫМДАР:
jashilshim_target = pygame.Rect(263, 1029, 200, 300)
akshim_target = pygame.Rect(210, 1020, 200, 300)
karayubka_target = pygame.Rect(270, 1015, 200, 300)
sariyubka_target = pygame.Rect(238, 1003, 200, 300)
kokshim_target = pygame.Rect(263, 1015, 200, 300)
bozshim_target = pygame.Rect(236, 1015, 200, 300)
klesh_target = pygame.Rect(284, 1020, 200, 300)
jinsi_target = pygame.Rect(234, 1000, 200, 300)
yubka_target = pygame.Rect(232, 990, 200, 300)
yubka1_target = pygame.Rect(279, 1010, 200, 300)
yubka2_target = pygame.Rect(219, 930, 200, 300)
yubka3_target = pygame.Rect(210, 942, 200, 300)
# 4. БУТ КИЙИМДЕР:
bozsapog_target = pygame.Rect(303, 1286, 200, 200)
sapog_target = pygame.Rect(302, 1318, 200, 200)
karabuts_target = pygame.Rect(303, 1334, 200, 200)
kokbuts_target = pygame.Rect(305, 1322, 200, 200)
kizilbuts_target = pygame.Rect(305, 1321, 200, 200)


# 5. АКСЕССУАРЛАР:
ochka_target = pygame.Rect(294, 753, 200, 200)
ochka1_target = pygame.Rect(289, 751, 200, 200)
ochka2_target = pygame.Rect(297, 747, 200, 200)

sumka_target = pygame.Rect(240, 1070, 200, 200)
sumka1_target = pygame.Rect(235, 1075, 200, 200)
sumka2_target = pygame.Rect(240, 1075, 200, 200)
sumka3_target = pygame.Rect(240, 1075, 200, 200)

jashilbantik_target = pygame.Rect(300, 620, 200, 200)
kizilbantik_target = pygame.Rect(300, 660, 200, 200)
bantik_target = pygame.Rect(300, 680, 200, 200)
bantik1_target = pygame.Rect(300, 680, 200, 200)
bantik2_target = pygame.Rect(300, 680, 200, 200)
bantik3_target = pygame.Rect(300, 680, 200, 200)
bantik4_target = pygame.Rect(300, 680, 200, 200)
bantik5_target = pygame.Rect(300, 680, 200, 200)

# Флаги
selected_item = None
offset_x, offset_y = 0, 0
is_dressed = {'akoinok': False, 'bozsapog': False, 'jashilbantik': False, 'jashilshim': False, 'zebrakoinok': False, 'karabuts': False, 'karayubka': False, 'kemsel': False, 'kokbuts': False, 'kokoinok': False, 'kokshim': False, 'kizilbuts': False, 'kizilkoinok': False, 'ochka': False, 'purpurkoinok': False, 'karakoinok': False, 'sarikoinok': False, 'kizillyamka': False, 'jashiljemper': False, 'sarijemper': False, 'doll': False, 'jashilkepka': False, 'kizilshlyapa': False, 'shapka': False, 'shlyapa': False, 'akshim': False, 'bozshim': False, 'jinsi': False, 'klesh': False, 'sariyubka': False, 'sapog': False, 'kizilbantik': False, 'sumka': False, 'bantik': False,'bantik1': False,'bantik2': False, 'bantik3': False, 'bantik4': False,'bantik5': False, 'sumka1': False,'sumka2': False, 'sumka3': False,'ochka1': False, 'ochka2': False, 'tumak': False, 'tumak1': False, 'tumak2': False, 'tumak3': False, 'yubka': False, 'yubka1': False, 'yubka2': False, 'yubka3': False}

def namesto(selected_item, rect):
                    if selected_item == "doll":
                        doll_rect.topleft = (128, 140)
                    elif selected_item == "akoinok":
                        akoinok_rect.topleft = (9, 127)
                    elif selected_item == "zebrakoinok":
                        zebrakoinok_rect.topleft = (114, 913)
                    elif selected_item == "kokoinok":
                        kokoinok_rect.topleft = (7, 260)
                    elif selected_item == "kizilkoinok":
                        kizilkoinok_rect.topleft = (75, 530)
                    elif selected_item == "purpurkoinok":
                        purpurkoinok_rect.topleft = (98, 342)
                    elif selected_item == "karakoinok":
                        karakoinok_rect.topleft = (110, 710)
                    elif selected_item == "sarikoinok":
                        sarikoinok_rect.topleft = (0, 545)
                    elif selected_item == "kizillyamka":
                        kizillyamka_rect.topleft = (8, 690)
                    elif selected_item == "kemsel":
                        kemsel_rect.topleft = (0, 385)
                    elif selected_item == "jashiljemper":
                        jashiljemper_rect.topleft = (6, 870)
                    elif selected_item == "sarijemper":
                        sarijemper_rect.topleft = (0, 1000)
                    elif selected_item == "bozshim":
                        kokshim2_rect.topleft = (595, 334)
                    elif selected_item == "akshim":
                        akshim_rect.topleft = (490, 330)
                    elif selected_item == "kokshim":
                        kokshim_rect.topleft = (605, 154)
                    elif selected_item == "jashilshim":
                        jashilshim_rect.topleft = (507, 157)
                    elif selected_item == "jinsi":
                        jinsi_rect.topleft = (489, 515)
                    elif selected_item == "klesh":
                        klesh_rect.topleft = (602, 520)
                    elif selected_item == "karayubka":
                        karayubka_rect.topleft = (609, 690)
                    elif selected_item == "sariyubka":
                        sariyubka_rect.topleft = (507, 687)
                    elif selected_item == "yubka":
                        yubka_rect.topleft = (500, 830)
                    elif selected_item == "yubka1":
                        yubka1_rect.topleft = (611, 835)
                    elif selected_item == "yubka2":
                        yubka2_rect.topleft = (499, 945)
                    elif selected_item == "yubka3":
                        yubka3_rect.topleft = (602, 947)
                    elif selected_item == "karabuts":
                        karabuts_rect.topleft = (625, 1130)
                    elif selected_item == "kokbuts":
                        kokbuts_rect.topleft = (540, 1123)
                    elif selected_item == "kizilbuts":
                        kizilbuts_rect.topleft = (460, 1123)
                    elif selected_item == "bozsapog":
                        bozsapog_rect.topleft = (480, 1192)
                    elif selected_item == "sapog":
                        sapog_rect.topleft = (590, 1225)
                    elif selected_item == "jashilbantik":
                        jashilbantik_rect.topleft = (282, 105)
                    elif selected_item == "kizilbantik":
                        kizilbantik_rect.topleft = (352, 112)
                    elif selected_item == "bantik":
                        bantik_rect.topleft = (254, 170)
                    elif selected_item == "bantik1":
                        bantik1_rect.topleft = (245, 231)
                    elif selected_item == "bantik2":
                        bantik2_rect.topleft = (242, 300)
                    elif selected_item == "bantik3":
                        bantik3_rect.topleft = (378, 176)
                    elif selected_item == "bantik4":
                        bantik4_rect.topleft = (385, 230)
                    elif selected_item == "bantik5":
                        bantik5_rect.topleft = (392, 300)
                    elif selected_item == "kizilshlyapa":
                        kizilshlyapa_rect.topleft = (100, 12)
                    elif selected_item == "jashilkepka":
                        jashilkepka_rect.topleft = (1, 18)
                    elif selected_item == "shapka":
                        shapka_rect.topleft = (184, 19)
                    elif selected_item == "shlyapa":
                        shlyapa_rect.topleft = (261, 22)
                    elif selected_item == "tumak":
                        tumak_rect.topleft = (392, 22)
                    elif selected_item == "tumak1":
                        tumak1_rect.topleft = (472, 22)
                    elif selected_item == "tumak2":
                        tumak2_rect.topleft = (551, 22)
                    elif selected_item == "tumak3":
                        tumak3_rect.topleft = (634, 22)
                    elif selected_item == "sumka":
                        sumka_rect.topleft = (280, 494)
                    elif selected_item == "sumka1":
                        sumka1_rect.topleft = (365, 491)
                    elif selected_item == "sumka2":
                        sumka2_rect.topleft = (280, 565)
                    elif selected_item == "sumka3":
                        sumka3_rect.topleft = (370, 577)
                    elif selected_item == "ochka":
                        ochka_rect.topleft = (270, 451)
                    elif selected_item == "ochka1":
                        ochka1_rect.topleft = (326, 449)
                    elif selected_item == "ochka2":
                        ochka2_rect.topleft = (390, 447)
running = True
while running:
    # Отрисовка
    screen.blit(background, (0, 0))
    screen.blit(polka, (470, 1160))
    screen.blit(polka4, (250, 430))
    screen.blit(polka4, (250, 500))
    screen.blit(polka4, (250, 570))
    
    if is_dressed["sumka"]:
        screen.blit(sumka_big, sumka_rect)
    else:
        screen.blit(sumka_small, sumka_rect)
    if is_dressed["sumka1"]:
        screen.blit(sumka1_big, sumka1_rect)
    else:
        screen.blit(sumka1_small, sumka1_rect)
    if is_dressed["sumka2"]:
        screen.blit(sumka2_big, sumka2_rect)
    else:
        screen.blit(sumka2_small, sumka2_rect)
    if is_dressed["sumka3"]:
        screen.blit(sumka3_big, sumka3_rect)
    else:
        screen.blit(sumka3_small, sumka3_rect)
    screen.blit(doll, (239, 645))
    screen.blit(logo, (306, 70))
    
    
    screen.blit(veshalka1, (10, 100))
    screen.blit(veshalka1, (120, 100))
    screen.blit(veshalka1, (120, 880))
    screen.blit(veshalka1, (10, 230))
    screen.blit(veshalka1, (10, 357))
    screen.blit(veshalka1, (110, 310))
    screen.blit(veshalka1, (118, 500))
    screen.blit(veshalka1, (115, 670))
    screen.blit(veshalka1, (17, 510))
    screen.blit(veshalka1, (17, 655))
    screen.blit(veshalka1, (10, 840))
    screen.blit(veshalka1, (10, 984))
    
    screen.blit(veshalka3, (20, 0))
    screen.blit(veshalka3, (100, 0))
    screen.blit(veshalka3, (180, 0))
    screen.blit(veshalka3, (260, 0))
    screen.blit(veshalka3, (390, 0))
    screen.blit(veshalka3, (470, 0))
    screen.blit(veshalka3, (550, 0))
    screen.blit(veshalka3, (630, 0))
    
    screen.blit(veshalka2, (500, 100))
    screen.blit(veshalka2, (600, 100))
    screen.blit(veshalka2, (500, 275))
    screen.blit(veshalka2, (600, 275))
    screen.blit(veshalka2, (500, 460))
    screen.blit(veshalka2, (600, 460))
    screen.blit(veshalka2, (500, 635))
    screen.blit(veshalka2, (600, 635))
    screen.blit(veshalka2, (500, 775))
    screen.blit(veshalka2, (600, 775))
    screen.blit(veshalka2, (500, 910))
    screen.blit(veshalka2, (600, 910))
    
    screen.blit(veshalka4, (295, 115))
    screen.blit(veshalka4, (370, 115))
    screen.blit(veshalka4, (270, 175))
    screen.blit(veshalka4, (393, 175))
    screen.blit(veshalka4, (260, 235))
    screen.blit(veshalka4, (403, 235))
    screen.blit(veshalka4, (255, 295))
    screen.blit(veshalka4, (408, 295))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
        elif event.type == MOUSEBUTTONDOWN:
            mx, my = event.pos
            for name, rect in [('doll', doll_rect), ('akoinok', akoinok_rect), ('bozsapog', bozsapog_rect),
                               ('jashilbantik', jashilbantik_rect), ('jashilshim', jashilshim_rect), ('zebrakoinok', zebrakoinok_rect), ('karabuts', karabuts_rect), ('karayubka', karayubka_rect), ('kemsel', kemsel_rect), ('kokbuts', kokbuts_rect), ('kokoinok', kokoinok_rect), ('kokshim', kokshim_rect), ('kizilbuts', kizilbuts_rect), ('kizilkoinok', kizilkoinok_rect), ('ochka', ochka_rect), ('purpurkoinok', purpurkoinok_rect), ('karakoinok', karakoinok_rect), ('sarikoinok', sarikoinok_rect), ('kizillyamka', kizillyamka_rect), ('jashiljemper', jashiljemper_rect), ('sarijemper', sarijemper_rect),  ('jashilkepka', jashilkepka_rect), ('kizilshlyapa', kizilshlyapa_rect), ('shapka', shapka_rect), ('shlyapa', shlyapa_rect), ('akshim', akshim_rect), ('bozshim', bozshim_rect), ('jinsi', jinsi_rect), ('klesh', klesh_rect), ('sariyubka', sariyubka_rect), ('sapog', sapog_rect), ('kizilbantik', kizilbantik_rect), ('sumka', sumka_rect), ('bantik', bantik_rect), ('bantik1', bantik1_rect), ('bantik2', bantik2_rect), ('bantik3', bantik3_rect), ('bantik4', bantik4_rect), ('bantik5', bantik5_rect), ('sumka1', sumka1_rect), ('sumka2', sumka2_rect),  ('sumka3', sumka3_rect), ('ochka1', ochka1_rect), ('ochka2', ochka2_rect), ('tumak', tumak_rect),('tumak1', tumak1_rect),('tumak2', tumak2_rect), ('tumak3', tumak3_rect), ('yubka', yubka_rect), ('yubka1', yubka1_rect), ('yubka2', yubka2_rect), ('yubka3', yubka3_rect)]:
                if rect.collidepoint(mx, my) and not is_dressed[name]:  
                    selected_item = name
                    offset_x, offset_y = mx - rect.x, my - rect.y
                    break
                    
        elif event.type == MOUSEBUTTONUP:
            if selected_item:
                Dressound.play(loops=0)
                if selected_item == "doll" and doll_target.colliderect(doll_rect):
                        doll_rect.topleft = doll_target.topleft
                        is_dressed["doll"] = True
                        
                        is_dressed["akoinok"] = False
                        is_dressed["kokoinok"] = False 
                        is_dressed["zebrakoinok"] = False
                        is_dressed["kizilkoinok"] = False
                        is_dressed["purpurkoinok"] = False
                        is_dressed["karakoinok"] = False
                        is_dressed["sarikoinok"] = False
                        is_dressed["kizillyamka"] = False
                        
                        is_dressed["kemsel"] = False
                        is_dressed["jashiljemper"] = False
                        is_dressed["sarijemper"] = False
                        
                        is_dressed["jashilshim"] = False
                        is_dressed["kokshim"] = False
                        is_dressed["akshim"] = False
                        is_dressed["bozshim"] = False
                        is_dressed["klesh"] = False
                        is_dressed["jinsi"] = False
                        
                        is_dressed["karayubka"] = False
                        is_dressed["sariyubka"] = False
                        is_dressed["yubka"] = False
                        is_dressed["yubka1"] = False
                        is_dressed["yubka2"] = False
                        is_dressed["yubka3"] = False
                        
                        is_dressed["kokbuts"] = False
                        is_dressed["karabuts"] = False
                        is_dressed["bozsapog"] = False
                        is_dressed["sapog"] = False
                        is_dressed["kizilbuts"] = False
                        
                        is_dressed["jashilbantik"] = False
                        is_dressed["kizilbantik"] = False
                        is_dressed["bantik"] = False
                        is_dressed["bantik1"] = False
                        is_dressed["bantik2"] = False
                        is_dressed["bantik3"] = False
                        is_dressed["bantik4"] = False
                        is_dressed["bantik5"] = False
                        
                        is_dressed["jashilkepka"] = False
                        is_dressed["kizilshlyapa"] = False
                        is_dressed["shapka"] = False
                        is_dressed["shlyapa"] = False
                        is_dressed["tumak"] = False
                        is_dressed["tumak1"] = False
                        is_dressed["tumak2"] = False
                        is_dressed["tumak3"] = False
                        
                        is_dressed["sumka"] = False
                        is_dressed["sumka1"] = False
                        is_dressed["sumka2"] = False
                        is_dressed["sumka3"] = False
                        
                        
                        is_dressed["ochka"] = False
                        is_dressed["ochka1"] = False
                        is_dressed["ochka2"] = False
                    
                        akoinok_rect.topleft = (9, 127)
                        zebrakoinok_rect.topleft = (114, 913)
                        kokoinok_rect.topleft = (7, 260)
                        kizilkoinok_rect.topleft = (75, 530)  
                        purpurkoinok_rect.topleft = (98, 342) 
                        karakoinok_rect.topleft = (110, 710)
                        sarikoinok_rect.topleft = (0, 545)      
                        kizillyamka_rect.topleft = (8, 690)
                        
                        kemsel_rect.topleft = (0, 385)      
                        jashiljemper_rect.topleft = (6, 870)
                        sarijemper_rect.topleft = (0, 1000)  
                         
                        bozshim_rect.topleft = (595, 334)
                        akshim_rect.topleft = (490, 330)
                        kokshim_rect.topleft = (605, 154)
                        jashilshim_rect.topleft = (507, 157)  
                        jinsi_rect.topleft = (489, 515)
                        klesh_rect.topleft = (602, 520)
                          
                        karayubka_rect.topleft = (609, 690)
                        sariyubka_rect.topleft = (507, 687) 
                        yubka_rect.topleft = (500, 830)
                        yubka1_rect.topleft = (611, 835) 
                        yubka2_rect.topleft = (499, 945)
                        yubka3_rect.topleft = (602, 947) 
                         
                        karabuts_rect.topleft = (625, 1130) 
                        kokbuts_rect.topleft = (540, 1123) 
                        kizilbuts_rect.topleft = (460, 1123)
                        bozsapog_rect.topleft = (480, 1192)
                        sapog_rect.topleft = (590, 1225)
                        
                        jashilbantik_rect.topleft = (282, 105)
                        kizilbantik_rect.topleft = (352, 112)
                        bantik_rect.topleft = (254, 170)
                        bantik1_rect.topleft = (245, 231)
                        bantik2_rect.topleft = (242, 300) 
                        bantik3_rect.topleft = (378, 176)
                        bantik4_rect.topleft = (385, 230)
                        bantik5_rect.topleft = (392, 300)
                        
                        kizilshlyapa_rect.topleft = (100, 12)
                        jashilkepka_rect.topleft = (1, 18)
                        shapka_rect.topleft = (184, 19)
                        shlyapa_rect.topleft = (261, 22)
                        tumak_rect.topleft = (392, 22)
                        tumak1_rect.topleft = (472, 22)
                        tumak2_rect.topleft = (551, 22)
                        tumak3_rect.topleft = (634, 22)
                        
                        sumka_rect.topleft = (280, 494)
                        sumka1_rect.topleft = (365, 491)
                        sumka2_rect.topleft = (280, 565)
                        sumka3_rect.topleft = (370, 577)
                        
                        ochka_rect.topleft = (270, 451)
                        ochka1_rect.topleft = (326, 449)
                        ochka2_rect.topleft = (390, 447)
                    
                elif selected_item == "akoinok" and akoinok_target.colliderect(akoinok_rect):
                    akoinok_rect.topleft = akoinok_target.topleft
                    is_dressed["akoinok"] = True
                    is_dressed["kokoinok"] = False 
                    is_dressed["zebrakoinok"] = False
                    is_dressed["kizilkoinok"] = False
                    is_dressed["purpurkoinok"] = False
                    is_dressed["karakoinok"] = False
                    is_dressed["sarikoinok"] = False
                    
                    is_dressed["doll"] = False 
                    is_dressed["kizillyamka"] = False
                    kizillyamka_rect.topleft = (8, 690)
                    doll_rect.topleft = (128, 140)
                    zebrakoinok_rect.topleft = (114, 913)
                    kokoinok_rect.topleft = (7, 260)
                    kizilkoinok_rect.topleft = (75, 530)  
                    purpurkoinok_rect.topleft = (98, 342) 
                    karakoinok_rect.topleft = (110, 710)
                    sarikoinok_rect.topleft = (0, 545)      
                    
                        
                elif selected_item == "zebrakoinok" and zebrakoinok_target.colliderect(zebrakoinok_rect):
                    zebrakoinok_rect.topleft = zebrakoinok_target.topleft
                    is_dressed["zebrakoinok"] = True  
                    is_dressed["akoinok"] = False
                    is_dressed["kokoinok"] = False 
                    is_dressed["sarikoinok"] = False
                    is_dressed["kizilkoinok"] = False
                    is_dressed["purpurkoinok"] = False
                    is_dressed["karakoinok"] = False
                    is_dressed["bozshim"] = False
                    is_dressed["kizillyamka"] = False
                    is_dressed["karayubka"] = False
                    is_dressed["sariyubka"] = False
                    is_dressed["yubka"] = False
                    is_dressed["yubka1"] = False
                    is_dressed["yubka2"] = False
                    is_dressed["yubka3"] = False
                    is_dressed["akshim"] = False
                    is_dressed["doll"] = False
                    is_dressed["jinsi"] = False
                    jinsi_rect.topleft = (489, 515)
                    akoinok_rect.topleft = (9, 127)
                    doll_rect.topleft = (128, 140)
                    kokoinok_rect.topleft = (7, 260)
                    kizilkoinok_rect.topleft = (75, 530)  
                    purpurkoinok_rect.topleft = (98, 342) 
                    karakoinok_rect.topleft = (110, 710)
                    sarikoinok_rect.topleft = (0, 545) 
                    kizillyamka_rect.topleft = (8, 690)
                    karayubka_rect.topleft = (609, 690)
                    sariyubka_rect.topleft = (507, 687) 
                    yubka_rect.topleft = (500, 830)
                    yubka1_rect.topleft = (611, 835) 
                    yubka2_rect.topleft = (499, 945)
                    yubka3_rect.topleft = (602, 947) 
                    akshim_rect.topleft = (490, 330)
                    bozshim_rect.topleft = (595, 334)
                    
                elif selected_item == "kokoinok" and kokoinok_target.colliderect(kokoinok_rect):
                    kokoinok_rect.topleft = kokoinok_target.topleft
                    is_dressed["kokoinok"] = True  
                    is_dressed["akoinok"] = False 
                    is_dressed["zebrakoinok"] = False
                    is_dressed["kizilkoinok"] = False
                    is_dressed["purpurkoinok"] = False
                    is_dressed["karakoinok"] = False
                    is_dressed["sarikoinok"] = False
                    is_dressed["kizillyamka"] = False
                    is_dressed["doll"] = False
                    akoinok_rect.topleft = (9, 127)
                    zebrakoinok_rect.topleft = (114, 913)
                    doll_rect.topleft = (128, 140)
                    kizilkoinok_rect.topleft = (75, 530)  
                    purpurkoinok_rect.topleft = (98, 342) 
                    karakoinok_rect.topleft = (110, 710)
                    sarikoinok_rect.topleft = (0, 545)      
                    kizillyamka_rect.topleft = (8, 690)
                    
                elif selected_item == "kizilkoinok" and kizilkoinok_target.colliderect(kizilkoinok_rect):
                    kizilkoinok_rect.topleft = kizilkoinok_target.topleft
                    is_dressed["kizilkoinok"] = True
                    is_dressed["akoinok"] = False
                    is_dressed["kokoinok"] = False 
                    is_dressed["zebrakoinok"] = False
                    is_dressed["purpurkoinok"] = False
                    is_dressed["karakoinok"] = False
                    is_dressed["sarikoinok"] = False
                    is_dressed["kizillyamka"] = False
                    is_dressed["sarijemper"] = False
                    is_dressed["jashiljemper"] = False
                    is_dressed["kemsel"] = False
                    is_dressed["karayubka"] = False
                    is_dressed["sariyubka"] = False
                    is_dressed["yubka"] = False
                    is_dressed["yubka1"] = False
                    is_dressed["yubka2"] = False
                    is_dressed["yubka3"] = False
                    is_dressed["doll"] = False
                    
                    akoinok_rect.topleft = (9, 127)
                    zebrakoinok_rect.topleft = (114, 913)
                    kokoinok_rect.topleft = (7, 260)
                    doll_rect.topleft = (128, 140)  
                    purpurkoinok_rect.topleft = (98, 342) 
                    karakoinok_rect.topleft = (110, 710)
                    sarikoinok_rect.topleft = (0, 545)      
                    kizillyamka_rect.topleft = (8, 690)
                    kemsel_rect.topleft = (0, 385)      
                    jashiljemper_rect.topleft = (6, 870)
                    sarijemper_rect.topleft = (0, 1000)
                    karayubka_rect.topleft = (609, 690)
                    sariyubka_rect.topleft = (507, 687) 
                    yubka_rect.topleft = (500, 830)
                    yubka1_rect.topleft = (611, 835) 
                    yubka2_rect.topleft = (499, 945)
                    yubka3_rect.topleft = (602, 947) 
                    
                elif selected_item == "purpurkoinok" and purpurkoinok_target.colliderect(purpurkoinok_rect):
                    purpurkoinok_rect.topleft = purpurkoinok_target.topleft
                    is_dressed["purpurkoinok"] = True
                    is_dressed["akoinok"] = False
                    is_dressed["kokoinok"] = False 
                    is_dressed["zebrakoinok"] = False
                    is_dressed["kizilkoinok"] = False
                    is_dressed["karakoinok"] = False
                    is_dressed["sarikoinok"] = False
                    is_dressed["kizillyamka"] = False
                    is_dressed["karayubka"] = False
                    is_dressed["sariyubka"] = False
                    is_dressed["yubka"] = False
                    is_dressed["yubka1"] = False
                    is_dressed["yubka2"] = False
                    is_dressed["yubka3"] = False
                    is_dressed["doll"] = False
                    
                    akoinok_rect.topleft = (9, 127)
                    zebrakoinok_rect.topleft = (114, 913)
                    kokoinok_rect.topleft = (7, 260)
                    kizilkoinok_rect.topleft = (75, 530)  
                    doll_rect.topleft = (128, 140)
                    karakoinok_rect.topleft = (110, 710)
                    sarikoinok_rect.topleft = (0, 545)      
                    kizillyamka_rect.topleft = (8, 690)
                    karayubka_rect.topleft = (609, 690)
                    sariyubka_rect.topleft = (507, 687) 
                    yubka_rect.topleft = (500, 830)
                    yubka1_rect.topleft = (611, 835) 
                    yubka2_rect.topleft = (499, 945)
                    yubka3_rect.topleft = (602, 947) 
                    
                elif selected_item == "karakoinok" and karakoinok_target.colliderect(karakoinok_rect):
                    karakoinok_rect.topleft = karakoinok_target.topleft
                    is_dressed["karakoinok"] = True
                    is_dressed["akoinok"] = False
                    is_dressed["kokoinok"] = False 
                    is_dressed["zebrakoinok"] = False
                    is_dressed["kizilkoinok"] = False
                    is_dressed["purpurkoinok"] = False
                    is_dressed["sarikoinok"] = False
                    is_dressed["kizillyamka"] = False
                    is_dressed["karayubka"] = False
                    is_dressed["sariyubka"] = False
                    is_dressed["yubka"] = False
                    is_dressed["yubka1"] = False
                    is_dressed["yubka2"] = False
                    is_dressed["yubka3"] = False
                    is_dressed["doll"] = False
                    
                    akoinok_rect.topleft = (9, 127)
                    zebrakoinok_rect.topleft = (114, 913)
                    kokoinok_rect.topleft = (7, 260)
                    kizilkoinok_rect.topleft = (75, 530)  
                    purpurkoinok_rect.topleft = (98, 342) 
                    doll_rect.topleft = (128, 140)
                    sarikoinok_rect.topleft = (0, 545)      
                    kizillyamka_rect.topleft = (8, 690)
                    karayubka_rect.topleft = (609, 690)
                    sariyubka_rect.topleft = (507, 687) 
                    yubka_rect.topleft = (500, 830)
                    yubka1_rect.topleft = (611, 835) 
                    yubka2_rect.topleft = (499, 945)
                    yubka3_rect.topleft = (602, 947) 
                    
                elif selected_item == "sarikoinok" and sarikoinok_target.colliderect(sarikoinok_rect):
                    sarikoinok_rect.topleft = sarikoinok_target.topleft
                    is_dressed["sarikoinok"] = True
                    is_dressed["akoinok"] = False
                    is_dressed["kokoinok"] = False 
                    is_dressed["zebrakoinok"] = False
                    is_dressed["kizilkoinok"] = False
                    is_dressed["purpurkoinok"] = False
                    is_dressed["karakoinok"] = False
                    is_dressed["kizillyamka"] = False
                    is_dressed["doll"] = False
                    akoinok_rect.topleft = (9, 127)
                    zebrakoinok_rect.topleft = (114, 913)
                    kokoinok_rect.topleft = (7, 260)
                    kizilkoinok_rect.topleft = (75, 530)  
                    purpurkoinok_rect.topleft = (98, 342) 
                    karakoinok_rect.topleft = (110, 710)
                    doll_rect.topleft = (128, 140)    
                    kizillyamka_rect.topleft = (8, 690)
                elif selected_item == "kizillyamka" and kizillyamka_target.colliderect(kizillyamka_rect):
                    kizillyamka_rect.topleft = kizillyamka_target.topleft
                    is_dressed["kizillyamka"] = True
                    is_dressed["akoinok"] = False
                    is_dressed["kokoinok"] = False 
                    is_dressed["zebrakoinok"] = False
                    is_dressed["kizilkoinok"] = False
                    is_dressed["purpurkoinok"] = False
                    is_dressed["karakoinok"] = False
                    is_dressed["sarikoinok"] = False
                    is_dressed["karayubka"] = False
                    is_dressed["sariyubka"] = False
                    is_dressed["yubka"] = False
                    is_dressed["yubka1"] = False
                    is_dressed["yubka2"] = False
                    is_dressed["yubka3"] = False
                    is_dressed["doll"] = False
                    is_dressed["sarijemper"] = False
                    sarijemper_rect.topleft = (0, 1000)
                    is_dressed["jashiljemper"] = False
                    jashiljemper_rect.topleft = (6, 870)
                    akoinok_rect.topleft = (9, 127)
                    zebrakoinok_rect.topleft = (114, 913)
                    kokoinok_rect.topleft = (7, 260)
                    kizilkoinok_rect.topleft = (75, 530)  
                    purpurkoinok_rect.topleft = (98, 342) 
                    karakoinok_rect.topleft = (110, 710)
                    sarikoinok_rect.topleft = (0, 545)   
                    karayubka_rect.topleft = (609, 690)
                    sariyubka_rect.topleft = (507, 687) 
                    yubka_rect.topleft = (500, 830)
                    yubka1_rect.topleft = (611, 835) 
                    yubka2_rect.topleft = (499, 945)
                    yubka3_rect.topleft = (602, 947) 
                    doll_rect.topleft = (128, 140)
                elif selected_item == "kemsel" and kemsel_target.colliderect(kemsel_rect):
                    kemsel_rect.topleft = kemsel_target.topleft
                    is_dressed["kemsel"] = True
                    is_dressed["kizilkoinok"] = False
                    is_dressed["jashiljemper"] = False
                    is_dressed["sarijemper"] = False
                    is_dressed["doll"] = False
                    doll_rect.topleft = (128, 140)      
                    jashiljemper_rect.topleft = (6, 870)
                    sarijemper_rect.topleft = (0, 1000)
                    kizilkoinok_rect.topleft = (75, 530)
                elif selected_item == "jashiljemper" and jashiljemper_target.colliderect(jashiljemper_rect):
                    jashiljemper_rect.topleft = jashiljemper_target.topleft
                    is_dressed["jashiljemper"] = True
                    is_dressed["kizilkoinok"] = False
                    is_dressed["kemsel"] = False
                    
                    is_dressed["doll"] = False
                    is_dressed["kizillyamka"] = False
                    is_dressed["sarijemper"] = False
                    sarijemper_rect.topleft = (0, 1000)
                    kizillyamka_rect.topleft = (8, 690)
                    kemsel_rect.topleft = (0, 385)      
                    doll_rect.topleft = (128, 140)
                    
                    kizilkoinok_rect.topleft = (75, 530)
                elif selected_item == "sarijemper" and sarijemper_target.colliderect(sarijemper_rect):
                    sarijemper_rect.topleft = sarijemper_target.topleft
                    is_dressed["sarijemper"] = True
                    is_dressed["jashiljemper"] = False
                    is_dressed["kizilkoinok"] = False
                    is_dressed["kemsel"] = False
                    is_dressed["doll"] = False
                    is_dressed["kizillyamka"] = False
                    kizillyamka_rect.topleft = (8, 690)
                    kemsel_rect.topleft = (0, 385)      
                    jashiljemper_rect.topleft = (6, 870)
                    doll_rect.topleft = (128, 140)
                    kizilkoinok_rect.topleft = (75, 530)
                    
                elif selected_item == "karayubka" and karayubka_target.colliderect(karayubka_rect):
                    karayubka_rect.topleft = karayubka_target.topleft
                    is_dressed["karayubka"] = True
                    is_dressed["sariyubka"] = False
                    is_dressed["jashilshim"] = False
                    is_dressed["kokshim"] = False
                    is_dressed["yubka"] = False
                    is_dressed["yubka1"] = False
                    is_dressed["yubka2"] = False
                    is_dressed["yubka3"] = False
                    is_dressed["akshim"] = False
                    is_dressed["bozshim"] = False
                    is_dressed["klesh"] = False
                    is_dressed["jinsi"] = False
                    is_dressed["kizilkoinok"] = False
                    is_dressed["purpurkoinok"] = False
                    is_dressed["karakoinok"] = False
                    is_dressed["zebrakoinok"] = False  
                    is_dressed["kizillyamka"] = False
                    is_dressed["doll"] = False
                    bozshim_rect.topleft = (595, 334)
                    akshim_rect.topleft = (490, 330)
                    kokshim_rect.topleft = (605, 154)
                    jashilshim_rect.topleft = (507, 157)  
                    jinsi_rect.topleft = (489, 515)
                    klesh_rect.topleft = (602, 520)
                    doll_rect.topleft = (128, 140)
                    sariyubka_rect.topleft = (507, 687) 
                    yubka_rect.topleft = (500, 830)
                    yubka1_rect.topleft = (611, 835) 
                    yubka2_rect.topleft = (499, 945)
                    yubka3_rect.topleft = (602, 947) 
                    kizilkoinok_rect.topleft = (75, 530)  
                    purpurkoinok_rect.topleft = (98, 342) 
                    karakoinok_rect.topleft = (110, 710)
                    zebrakoinok_rect.topleft = (114, 913)
                    kizillyamka_rect.topleft = (8, 690)
                    
                elif selected_item == "sariyubka" and sariyubka_target.colliderect(sariyubka_rect):
                    sariyubka_rect.topleft = sariyubka_target.topleft
                    is_dressed["sariyubka"] = True
                    is_dressed["jashilshim"] = False
                    is_dressed["kokshim"] = False
                    is_dressed["karayubka"] = False
                    is_dressed["yubka"] = False
                    is_dressed["yubka1"] = False
                    is_dressed["yubka2"] = False
                    is_dressed["yubka3"] = False
                    is_dressed["akshim"] = False
                    is_dressed["bozshim"] = False
                    is_dressed["klesh"] = False
                    is_dressed["kizilkoinok"] = False
                    is_dressed["purpurkoinok"] = False
                    is_dressed["karakoinok"] = False
                    is_dressed["zebrakoinok"] = False  
                    is_dressed["kizillyamka"] = False
                    is_dressed["doll"] = False
                    is_dressed["jinsi"] = False
                    jinsi_rect.topleft = (489, 515)
                    bozshim_rect.topleft = (595, 334)
                    akshim_rect.topleft = (490, 330)
                    kokshim_rect.topleft = (605, 154)
                    jashilshim_rect.topleft = (507, 157)  
                    
                    klesh_rect.topleft = (602, 520)
                    karayubka_rect.topleft = (609, 690)
                    doll_rect.topleft = (128, 140) 
                    yubka_rect.topleft = (500, 830)
                    yubka1_rect.topleft = (611, 835) 
                    yubka2_rect.topleft = (499, 945)
                    yubka3_rect.topleft = (602, 947) 
                    kizilkoinok_rect.topleft = (75, 530)  
                    purpurkoinok_rect.topleft = (98, 342) 
                    karakoinok_rect.topleft = (110, 710)
                    zebrakoinok_rect.topleft = (114, 913)
                    kizillyamka_rect.topleft = (8, 690)
                    
                elif selected_item == "yubka" and yubka_target.colliderect(yubka_rect):
                    yubka_rect.topleft = yubka_target.topleft
                    is_dressed["yubka"] = True
                    is_dressed["jashilshim"] = False
                    is_dressed["kokshim"] = False
                    is_dressed["karayubka"] = False
                    is_dressed["sariyubka"] = False
                    is_dressed["yubka1"] = False
                    is_dressed["yubka2"] = False
                    is_dressed["yubka3"] = False
                    is_dressed["akshim"] = False
                    is_dressed["bozshim"] = False
                    is_dressed["klesh"] = False
                    is_dressed["jinsi"] = False
                    is_dressed["kizilkoinok"] = False
                    is_dressed["purpurkoinok"] = False
                    is_dressed["karakoinok"] = False
                    is_dressed["zebrakoinok"] = False  
                    is_dressed["kizillyamka"] = False
                    is_dressed["doll"] = False
                    bozshim_rect.topleft = (595, 334)
                    akshim_rect.topleft = (490, 330)
                    kokshim_rect.topleft = (605, 154)
                    jashilshim_rect.topleft = (507, 157)  
                    jinsi_rect.topleft = (489, 515)
                    klesh_rect.topleft = (602, 520)
                    karayubka_rect.topleft = (609, 690)
                    sariyubka_rect.topleft = (507, 687) 
                    doll_rect.topleft = (128, 140)
                    yubka1_rect.topleft = (611, 835) 
                    yubka2_rect.topleft = (499, 945)
                    yubka3_rect.topleft = (602, 947) 
                    kizilkoinok_rect.topleft = (75, 530)  
                    purpurkoinok_rect.topleft = (98, 342) 
                    karakoinok_rect.topleft = (110, 710)
                    zebrakoinok_rect.topleft = (114, 913)
                    kizillyamka_rect.topleft = (8, 690)
                    
                elif selected_item == "yubka1" and yubka1_target.colliderect(yubka1_rect):
                    yubka1_rect.topleft = yubka1_target.topleft
                    is_dressed["yubka1"] = True
                    is_dressed["jashilshim"] = False
                    is_dressed["kokshim"] = False
                    is_dressed["karayubka"] = False
                    is_dressed["sariyubka"] = False
                    is_dressed["yubka"] = False
                    is_dressed["yubka2"] = False
                    is_dressed["yubka3"] = False
                    is_dressed["akshim"] = False
                    is_dressed["bozshim"] = False
                    is_dressed["klesh"] = False
                    is_dressed["jinsi"] = False
                    is_dressed["kizilkoinok"] = False
                    is_dressed["purpurkoinok"] = False
                    is_dressed["karakoinok"] = False
                    is_dressed["zebrakoinok"] = False  
                    is_dressed["kizillyamka"] = False
                    is_dressed["doll"] = False
                    bozshim_rect.topleft = (595, 334)
                    akshim_rect.topleft = (490, 330)
                    kokshim_rect.topleft = (605, 154)
                    jashilshim_rect.topleft = (507, 157)  
                    jinsi_rect.topleft = (489, 515)
                    klesh_rect.topleft = (602, 520)
                    karayubka_rect.topleft = (609, 690)
                    sariyubka_rect.topleft = (507, 687) 
                    yubka_rect.topleft = (500, 830)
                    doll_rect.topleft = (128, 140) 
                    yubka2_rect.topleft = (499, 945)
                    yubka3_rect.topleft = (602, 947) 
                    kizilkoinok_rect.topleft = (75, 530)  
                    purpurkoinok_rect.topleft = (98, 342) 
                    karakoinok_rect.topleft = (110, 710)
                    zebrakoinok_rect.topleft = (114, 913)
                    kizillyamka_rect.topleft = (8, 690)
                    
                elif selected_item == "yubka2" and yubka2_target.colliderect(yubka2_rect):
                    yubka2_rect.topleft = yubka2_target.topleft
                    is_dressed["yubka2"] = True
                    is_dressed["jashilshim"] = False
                    is_dressed["kokshim"] = False
                    is_dressed["karayubka"] = False
                    is_dressed["sariyubka"] = False
                    is_dressed["yubka1"] = False
                    is_dressed["yubka"] = False
                    is_dressed["yubka3"] = False
                    is_dressed["akshim"] = False
                    is_dressed["bozshim"] = False
                    is_dressed["klesh"] = False
                    is_dressed["jinsi"] = False
                    is_dressed["kizilkoinok"] = False
                    is_dressed["purpurkoinok"] = False
                    is_dressed["karakoinok"] = False
                    is_dressed["zebrakoinok"] = False  
                    is_dressed["kizillyamka"] = False
                    is_dressed["doll"] = False
                    bozshim_rect.topleft = (595, 334)
                    akshim_rect.topleft = (490, 330)
                    kokshim_rect.topleft = (605, 154)
                    jashilshim_rect.topleft = (507, 157)  
                    jinsi_rect.topleft = (489, 515)
                    klesh_rect.topleft = (602, 520)
                    karayubka_rect.topleft = (609, 690)
                    sariyubka_rect.topleft = (507, 687) 
                    yubka_rect.topleft = (500, 830)
                    yubka1_rect.topleft = (611, 835) 
                    doll_rect.topleft = (128, 140)
                    yubka3_rect.topleft = (602, 947) 
                    kizilkoinok_rect.topleft = (75, 530)  
                    purpurkoinok_rect.topleft = (98, 342) 
                    karakoinok_rect.topleft = (110, 710)
                    zebrakoinok_rect.topleft = (114, 913)
                    kizillyamka_rect.topleft = (8, 690)
                    
                elif selected_item == "yubka3" and yubka3_target.colliderect(yubka3_rect):
                    yubka3_rect.topleft = yubka3_target.topleft
                    is_dressed["yubka3"] = True
                    is_dressed["jashilshim"] = False
                    is_dressed["kokshim"] = False
                    is_dressed["karayubka"] = False
                    is_dressed["sariyubka"] = False
                    is_dressed["yubka1"] = False
                    is_dressed["yubka2"] = False
                    is_dressed["yubka"] = False
                    is_dressed["akshim"] = False
                    is_dressed["bozshim"] = False
                    is_dressed["klesh"] = False
                    is_dressed["jinsi"] = False
                    is_dressed["kizilkoinok"] = False
                    is_dressed["purpurkoinok"] = False
                    is_dressed["karakoinok"] = False
                    is_dressed["zebrakoinok"] = False  
                    is_dressed["kizillyamka"] = False
                    is_dressed["doll"] = False
                    bozshim_rect.topleft = (595, 334)
                    akshim_rect.topleft = (490, 330)
                    kokshim_rect.topleft = (605, 154)
                    jashilshim_rect.topleft = (507, 157)  
                    jinsi_rect.topleft = (489, 515)
                    klesh_rect.topleft = (602, 520)
                    karayubka_rect.topleft = (609, 690)
                    sariyubka_rect.topleft = (507, 687) 
                    yubka_rect.topleft = (500, 830)
                    yubka1_rect.topleft = (611, 835) 
                    yubka2_rect.topleft = (499, 945)
                    doll_rect.topleft = (128, 140)
                    kizilkoinok_rect.topleft = (75, 530)  
                    purpurkoinok_rect.topleft = (98, 342) 
                    karakoinok_rect.topleft = (110, 710)
                    zebrakoinok_rect.topleft = (114, 913)
                    kizillyamka_rect.topleft = (8, 690)
                    
                elif selected_item == "kokshim" and kokshim_target.colliderect(kokshim_rect):
                    kokshim_rect.topleft = kokshim_target.topleft
                    is_dressed["kokshim"] = True 
                    is_dressed["karayubka"] = False
                    is_dressed["sariyubka"] = False
                    is_dressed["jashilshim"] = False
                    is_dressed["yubka"] = False
                    is_dressed["yubka1"] = False
                    is_dressed["yubka2"] = False
                    is_dressed["yubka3"] = False
                    is_dressed["akshim"] = False
                    is_dressed["bozshim"] = False
                    is_dressed["klesh"] = False
                    is_dressed["jinsi"] = False
                    is_dressed["doll"] = False
                    bozshim_rect.topleft = (595, 334)
                    akshim_rect.topleft = (490, 330)
                    doll_rect.topleft = (128, 140)
                    jashilshim_rect.topleft = (507, 157)  
                    jinsi_rect.topleft = (489, 515)
                    klesh_rect.topleft = (602, 520)
                    karayubka_rect.topleft = (609, 690)
                    sariyubka_rect.topleft = (507, 687) 
                    yubka_rect.topleft = (500, 830)
                    yubka1_rect.topleft = (611, 835) 
                    yubka2_rect.topleft = (499, 945)
                    yubka3_rect.topleft = (602, 947) 
                    
                elif selected_item == "jashilshim" and jashilshim_target.colliderect(jashilshim_rect):
                    jashilshim_rect.topleft = jashilshim_target.topleft
                    is_dressed["jashilshim"] = True  
                    is_dressed["karayubka"] = False
                    is_dressed["sariyubka"] = False
                    is_dressed["kokshim"] = False
                    is_dressed["yubka"] = False
                    is_dressed["yubka1"] = False
                    is_dressed["yubka2"] = False
                    is_dressed["yubka3"] = False
                    is_dressed["akshim"] = False
                    is_dressed["bozshim"] = False
                    is_dressed["klesh"] = False
                    is_dressed["jinsi"] = False
                    is_dressed["doll"] = False
                    bozshim_rect.topleft = (595, 334)
                    akshim_rect.topleft = (490, 330)
                    kokshim_rect.topleft = (605, 154)
                    doll_rect.topleft = (128, 140)
                    jinsi_rect.topleft = (489, 515)
                    klesh_rect.topleft = (602, 520)
                    karayubka_rect.topleft = (609, 690)
                    sariyubka_rect.topleft = (507, 687) 
                    yubka_rect.topleft = (500, 830)
                    yubka1_rect.topleft = (611, 835) 
                    yubka2_rect.topleft = (499, 945)
                    yubka3_rect.topleft = (602, 947) 
                    
                elif selected_item == "akshim" and akshim_target.colliderect(akshim_rect):
                    akshim_rect.topleft = akshim_target.topleft
                    is_dressed["akshim"] = True
                    is_dressed["jashilshim"] = False
                    is_dressed["kokshim"] = False
                    is_dressed["karayubka"] = False
                    is_dressed["sariyubka"] = False
                    is_dressed["yubka"] = False
                    is_dressed["yubka1"] = False
                    is_dressed["yubka2"] = False
                    is_dressed["yubka3"] = False
                    is_dressed["bozshim"] = False
                    is_dressed["klesh"] = False
                    is_dressed["jinsi"] = False
                    is_dressed["zebrakoinok"] = False
                    is_dressed["doll"] = False
                    bozshim_rect.topleft = (595, 334)
                    doll_rect.topleft = (128, 140)
                    kokshim_rect.topleft = (605, 154)
                    jashilshim_rect.topleft = (507, 157)  
                    jinsi_rect.topleft = (489, 515)
                    klesh_rect.topleft = (602, 520)
                    karayubka_rect.topleft = (609, 690)
                    sariyubka_rect.topleft = (507, 687) 
                    yubka_rect.topleft = (500, 830)
                    yubka1_rect.topleft = (611, 835) 
                    yubka2_rect.topleft = (499, 945)
                    yubka3_rect.topleft = (602, 947) 
                    zebrakoinok_rect.topleft = (114, 913)
                elif selected_item == "bozshim" and bozshim_target.colliderect(bozshim_rect):
                    bozshim_rect.topleft = bozshim_target.topleft
                    is_dressed["bozshim"] = True
                    is_dressed["jashilshim"] = False
                    is_dressed["kokshim"] = False
                    is_dressed["karayubka"] = False
                    is_dressed["sariyubka"] = False
                    is_dressed["yubka"] = False
                    is_dressed["yubka1"] = False
                    is_dressed["yubka2"] = False
                    is_dressed["yubka3"] = False
                    is_dressed["akshim"] = False
                    is_dressed["klesh"] = False
                    is_dressed["jinsi"] = False
                    is_dressed["zebrakoinok"] = False
                    is_dressed["doll"] = False
                    doll_rect.topleft = (128, 140)
                    akshim_rect.topleft = (490, 330)
                    kokshim_rect.topleft = (605, 154)
                    jashilshim_rect.topleft = (507, 157)  
                    jinsi_rect.topleft = (489, 515)
                    klesh_rect.topleft = (602, 520)
                    karayubka_rect.topleft = (609, 690)
                    sariyubka_rect.topleft = (507, 687) 
                    yubka_rect.topleft = (500, 830)
                    yubka1_rect.topleft = (611, 835) 
                    yubka2_rect.topleft = (499, 945)
                    yubka3_rect.topleft = (602, 947) 
                    zebrakoinok_rect.topleft = (114, 913)
                    

                elif selected_item == "klesh" and klesh_target.colliderect(klesh_rect):
                    klesh_rect.topleft = klesh_target.topleft
                    is_dressed["klesh"] = True
                    is_dressed["jashilshim"] = False
                    is_dressed["kokshim"] = False
                    is_dressed["karayubka"] = False
                    is_dressed["sariyubka"] = False
                    is_dressed["yubka"] = False
                    is_dressed["yubka1"] = False
                    is_dressed["yubka2"] = False
                    is_dressed["yubka3"] = False
                    is_dressed["akshim"] = False
                    is_dressed["bozshim"] = False
                    is_dressed["jinsi"] = False
                    is_dressed["doll"] = False
                    bozshim_rect.topleft = (595, 334)
                    akshim_rect.topleft = (490, 330)
                    kokshim_rect.topleft = (605, 154)
                    jashilshim_rect.topleft = (507, 157)  
                    jinsi_rect.topleft = (489, 515)
                    doll_rect.topleft = (128, 140)
                    karayubka_rect.topleft = (609, 690)
                    sariyubka_rect.topleft = (507, 687) 
                    yubka_rect.topleft = (500, 830)
                    yubka1_rect.topleft = (611, 835) 
                    yubka2_rect.topleft = (499, 945)
                    yubka3_rect.topleft = (602, 947) 
                    
                elif selected_item == "jinsi" and jinsi_target.colliderect(jinsi_rect):
                    jinsi_rect.topleft = jinsi_target.topleft
                    is_dressed["jinsi"] = True
                    is_dressed["jashilshim"] = False
                    is_dressed["kokshim"] = False
                    is_dressed["karayubka"] = False
                    is_dressed["sariyubka"] = False
                    is_dressed["yubka"] = False
                    is_dressed["yubka1"] = False
                    is_dressed["yubka2"] = False
                    is_dressed["yubka3"] = False
                    is_dressed["akshim"] = False
                    is_dressed["bozshim"] = False
                    is_dressed["klesh"] = False
                    
                    is_dressed["zebrakoinok"] = False  
                    
                    is_dressed["doll"] = False
                    bozshim_rect.topleft = (595, 334)
                    akshim_rect.topleft = (490, 330)
                    kokshim_rect.topleft = (605, 154)
                    jashilshim_rect.topleft = (507, 157)  
                    doll_rect.topleft = (128, 140)
                    klesh_rect.topleft = (602, 520)
                    karayubka_rect.topleft = (609, 690)
                    sariyubka_rect.topleft = (507, 687) 
                    yubka_rect.topleft = (500, 830)
                    yubka1_rect.topleft = (611, 835) 
                    yubka2_rect.topleft = (499, 945)
                    yubka3_rect.topleft = (602, 947) 
                    
                    zebrakoinok_rect.topleft = (114, 913)
                    
                    
                
                elif selected_item == "kokbuts" and kokbuts_target.colliderect(kokbuts_rect):
                    kokbuts_rect.topleft = kokbuts_target.topleft
                    is_dressed["kokbuts"] = True
                    is_dressed["karabuts"] = False
                    is_dressed["bozsapog"] = False
                    is_dressed["kizilbuts"] = False
                    is_dressed["sapog"] = False
                    is_dressed["doll"] = False
                    karabuts_rect.topleft = (625, 1130) 
                    doll_rect.topleft = (128, 140)
                    kizilbuts_rect.topleft = (460, 1123)
                    bozsapog_rect.topleft = (480, 1192)
                    sapog_rect.topleft = (590, 1225)
                  
                elif selected_item == "kizilbuts" and kizilbuts_target.colliderect(kizilbuts_rect):
                    kizilbuts_rect.topleft = kizilbuts_target.topleft
                    is_dressed["kizilbuts"] = True 
                    is_dressed["kokbuts"] = False
                    is_dressed["karabuts"] = False
                    is_dressed["bozsapog"] = False
                    is_dressed["sapog"] = False
                    is_dressed["doll"] = False
                    karabuts_rect.topleft = (625, 1130) 
                    kokbuts_rect.topleft = (540, 1123) 
                    doll_rect.topleft = (128, 140)
                    bozsapog_rect.topleft = (480, 1192)
                    sapog_rect.topleft = (590, 1225)
                  
                    
                elif selected_item == "bozsapog" and bozsapog_target.colliderect(bozsapog_rect):
                    bozsapog_rect.topleft = bozsapog_target.topleft
                    is_dressed["bozsapog"] = True  
                    is_dressed["karabuts"] = False
                    is_dressed["kokbuts"] = False
                    is_dressed["kizilbuts"] = False
                    is_dressed["sapog"] = False
                    is_dressed["doll"] = False
                    karabuts_rect.topleft = (625, 1130) 
                    kokbuts_rect.topleft = (540, 1123) 
                    kizilbuts_rect.topleft = (460, 1123)
                    doll_rect.topleft = (128, 140)
                    sapog_rect.topleft = (590, 1225)
                  
                    
                elif selected_item == "karabuts" and karabuts_target.colliderect(karabuts_rect):
                    karabuts_rect.topleft = karabuts_target.topleft
                    is_dressed["karabuts"] = True
                    is_dressed["bozsapog"] = False
                    is_dressed["kokbuts"] = False
                    is_dressed["kizilbuts"] = False
                    is_dressed["sapog"] = False
                    is_dressed["doll"] = False
                    doll_rect.topleft = (128, 140)
                    kokbuts_rect.topleft = (540, 1123) 
                    kizilbuts_rect.topleft = (460, 1123)
                    bozsapog_rect.topleft = (480, 1192)
                    sapog_rect.topleft = (590, 1225)
                  
                elif selected_item == "sapog" and sapog_target.colliderect(sapog_rect):
                    sapog_rect.topleft = sapog_target.topleft
                    is_dressed["sapog"] = True
                    is_dressed["bozsapog"] = False
                    is_dressed["kokbuts"] = False
                    is_dressed["kizilbuts"] = False
                    is_dressed["karabuts"] = False
                    is_dressed["doll"] = False
                    karabuts_rect.topleft = (625, 1130) 
                    kokbuts_rect.topleft = (540, 1123) 
                    kizilbuts_rect.topleft = (460, 1123)
                    bozsapog_rect.topleft = (480, 1192)
                    doll_rect.topleft = (128, 140)
                  
                   
                
                elif selected_item == "jashilbantik" and jashilbantik_target.colliderect(jashilbantik_rect):
                    jashilbantik_rect.topleft = jashilbantik_target.topleft
                    is_dressed["jashilbantik"] = True  
                    is_dressed["jashilkepka"] = False
                    is_dressed["kizilshlyapa"] = False
                    is_dressed["shapka"] = False
                    is_dressed["shlyapa"] = False
                    is_dressed["tumak"] = False
                    is_dressed["tumak1"] = False
                    is_dressed["tumak2"] = False
                    is_dressed["tumak3"] = False
                    is_dressed["kizilbantik"] = False
                    is_dressed["bantik"] = False
                    is_dressed["bantik1"] = False
                    is_dressed["bantik2"] = False
                    is_dressed["bantik3"] = False
                    is_dressed["bantik4"] = False
                    is_dressed["bantik5"] = False
                    is_dressed["doll"] = False
                    doll_rect.topleft = (128, 140)
                    kizilbantik_rect.topleft = (352, 112)
                    bantik_rect.topleft = (254, 170)
                    bantik1_rect.topleft = (245, 231)
                    bantik2_rect.topleft = (242, 300) 
                    bantik3_rect.topleft = (378, 176)
                    bantik4_rect.topleft = (385, 230)
                    bantik5_rect.topleft = (392, 300)
                    kizilshlyapa_rect.topleft = (100, 12)
                    jashilkepka_rect.topleft = (1, 18)
                    shapka_rect.topleft = (184, 19)
                    shlyapa_rect.topleft = (261, 22)
                    tumak_rect.topleft = (392, 22)
                    tumak1_rect.topleft = (472, 22)
                    tumak2_rect.topleft = (551, 22)
                    tumak3_rect.topleft = (634, 22)
                        
                elif selected_item == "kizilbantik" and kizilbantik_target.colliderect(kizilbantik_rect):
                    kizilbantik_rect.topleft = kizilbantik_target.topleft
                    is_dressed["kizilbantik"] = True
                    is_dressed["jashilbantik"] = False
                    is_dressed["jashilkepka"] = False
                    is_dressed["shapka"] = False
                    is_dressed["kizilshlyapa"] = False
                    is_dressed["tumak"] = False
                    is_dressed["tumak1"] = False
                    is_dressed["tumak2"] = False
                    is_dressed["tumak3"] = False
                    is_dressed["shlyapa"] = False
                    is_dressed["bantik"] = False
                    is_dressed["bantik1"] = False
                    is_dressed["bantik2"] = False
                    is_dressed["bantik3"] = False
                    is_dressed["bantik4"] = False
                    is_dressed["bantik5"] = False
                    is_dressed["doll"] = False
                    jashilbantik_rect.topleft = (282, 105)
                    doll_rect.topleft = (128, 140)
                    bantik_rect.topleft = (254, 170)
                    bantik1_rect.topleft = (245, 231)
                    bantik2_rect.topleft = (242, 300) 
                    bantik3_rect.topleft = (378, 176)
                    bantik4_rect.topleft = (385, 230)
                    bantik5_rect.topleft = (392, 300)
                    kizilshlyapa_rect.topleft = (100, 12)
                    jashilkepka_rect.topleft = (1, 18)
                    shapka_rect.topleft = (184, 19)
                    shlyapa_rect.topleft = (261, 22)
                    tumak_rect.topleft = (392, 22)
                    tumak1_rect.topleft = (472, 22)
                    tumak2_rect.topleft = (551, 22)
                    tumak3_rect.topleft = (634, 22)
                        
                elif selected_item == "bantik" and bantik_target.colliderect(bantik_rect):
                    bantik_rect.topleft = bantik_target.topleft
                    is_dressed["bantik"] = True
                    is_dressed["jashilbantik"] = False
                    is_dressed["jashilkepka"] = False
                    is_dressed["shapka"] = False
                    is_dressed["kizilshlyapa"] = False
                    is_dressed["tumak"] = False
                    is_dressed["tumak1"] = False
                    is_dressed["tumak2"] = False
                    is_dressed["tumak3"] = False
                    is_dressed["shlyapa"] = False
                    is_dressed["kizilbantik"] = False
                    is_dressed["bantik1"] = False
                    is_dressed["bantik2"] = False
                    is_dressed["bantik3"] = False
                    is_dressed["bantik4"] = False
                    is_dressed["bantik5"] = False
                    is_dressed["doll"] = False
                    jashilbantik_rect.topleft = (282, 105)
                    kizilbantik_rect.topleft = (352, 112)
                    doll_rect.topleft = (128, 140)
                    bantik1_rect.topleft = (245, 231)
                    bantik2_rect.topleft = (242, 300) 
                    bantik3_rect.topleft = (378, 176)
                    bantik4_rect.topleft = (385, 230)
                    bantik5_rect.topleft = (392, 300)
                    kizilshlyapa_rect.topleft = (100, 12)
                    jashilkepka_rect.topleft = (1, 18)
                    shapka_rect.topleft = (184, 19)
                    shlyapa_rect.topleft = (261, 22)
                    tumak_rect.topleft = (392, 22)
                    tumak1_rect.topleft = (472, 22)
                    tumak2_rect.topleft = (551, 22)
                    tumak3_rect.topleft = (634, 22)
                        
                elif selected_item == "bantik1" and bantik1_target.colliderect(bantik1_rect):
                    bantik1_rect.topleft = bantik1_target.topleft
                    is_dressed["bantik1"] = True
                    is_dressed["jashilbantik"] = False
                    is_dressed["jashilkepka"] = False
                    is_dressed["shapka"] = False
                    is_dressed["kizilshlyapa"] = False
                    is_dressed["tumak"] = False
                    is_dressed["tumak1"] = False
                    is_dressed["tumak2"] = False
                    is_dressed["tumak3"] = False
                    is_dressed["shlyapa"] = False
                    is_dressed["kizilbantik"] = False
                    is_dressed["bantik"] = False
                    is_dressed["bantik2"] = False
                    is_dressed["bantik3"] = False
                    is_dressed["bantik4"] = False
                    is_dressed["bantik5"] = False
                    is_dressed["doll"] = False
                    jashilbantik_rect.topleft = (282, 105)
                    kizilbantik_rect.topleft = (352, 112)
                    bantik_rect.topleft = (254, 170)
                    doll_rect.topleft = (128, 140)
                    bantik2_rect.topleft = (242, 300) 
                    bantik3_rect.topleft = (378, 176)
                    bantik4_rect.topleft = (385, 230)
                    bantik5_rect.topleft = (392, 300)
                    kizilshlyapa_rect.topleft = (100, 12)
                    jashilkepka_rect.topleft = (1, 18)
                    shapka_rect.topleft = (184, 19)
                    shlyapa_rect.topleft = (261, 22)
                    tumak_rect.topleft = (392, 22)
                    tumak1_rect.topleft = (472, 22)
                    tumak2_rect.topleft = (551, 22)
                    tumak3_rect.topleft = (634, 22)
                        
                elif selected_item == "bantik2" and bantik2_target.colliderect(bantik2_rect):
                    bantik2_rect.topleft = bantik2_target.topleft
                    is_dressed["bantik2"] = True
                    is_dressed["jashilbantik"] = False
                    is_dressed["jashilkepka"] = False
                    is_dressed["shapka"] = False
                    is_dressed["kizilshlyapa"] = False
                    is_dressed["tumak"] = False
                    is_dressed["tumak1"] = False
                    is_dressed["tumak2"] = False
                    is_dressed["tumak3"] = False
                    is_dressed["shlyapa"] = False
                    is_dressed["kizilbantik"] = False
                    is_dressed["bantik1"] = False
                    is_dressed["bantik"] = False
                    is_dressed["bantik3"] = False
                    is_dressed["bantik4"] = False
                    is_dressed["bantik5"] = False
                    is_dressed["doll"] = False
                    jashilbantik_rect.topleft = (282, 105)
                    kizilbantik_rect.topleft = (352, 112)
                    bantik_rect.topleft = (254, 170)
                    bantik1_rect.topleft = (245, 231)
                    doll_rect.topleft = (128, 140)
                    bantik3_rect.topleft = (378, 176)
                    bantik4_rect.topleft = (385, 230)
                    bantik5_rect.topleft = (392, 300)
                    kizilshlyapa_rect.topleft = (100, 12)
                    jashilkepka_rect.topleft = (1, 18)
                    shapka_rect.topleft = (184, 19)
                    shlyapa_rect.topleft = (261, 22)
                    tumak_rect.topleft = (392, 22)
                    tumak1_rect.topleft = (472, 22)
                    tumak2_rect.topleft = (551, 22)
                    tumak3_rect.topleft = (634, 22)
                        
                elif selected_item == "bantik3" and bantik3_target.colliderect(bantik3_rect):
                    bantik3_rect.topleft = bantik3_target.topleft
                    is_dressed["bantik3"] = True
                    is_dressed["jashilbantik"] = False
                    is_dressed["jashilkepka"] = False
                    is_dressed["shapka"] = False
                    is_dressed["kizilshlyapa"] = False
                    is_dressed["tumak"] = False
                    is_dressed["tumak1"] = False
                    is_dressed["tumak2"] = False
                    is_dressed["tumak3"] = False
                    is_dressed["shlyapa"] = False
                    is_dressed["kizilbantik"] = False
                    is_dressed["bantik1"] = False
                    is_dressed["bantik2"] = False
                    is_dressed["bantik"] = False
                    is_dressed["bantik4"] = False
                    is_dressed["bantik5"] = False
                    is_dressed["doll"] = False
                    jashilbantik_rect.topleft = (282, 105)
                    kizilbantik_rect.topleft = (352, 112)
                    bantik_rect.topleft = (254, 170)
                    bantik1_rect.topleft = (245, 231)
                    bantik2_rect.topleft = (242, 300) 
                    doll_rect.topleft = (128, 140)
                    bantik4_rect.topleft = (385, 230)
                    bantik5_rect.topleft = (392, 300)
                    kizilshlyapa_rect.topleft = (100, 12)
                    jashilkepka_rect.topleft = (1, 18)
                    shapka_rect.topleft = (184, 19)
                    shlyapa_rect.topleft = (261, 22)
                    tumak_rect.topleft = (392, 22)
                    tumak1_rect.topleft = (472, 22)
                    tumak2_rect.topleft = (551, 22)
                    tumak3_rect.topleft = (634, 22)
                        
                elif selected_item == "bantik4" and bantik4_target.colliderect(bantik4_rect):
                    bantik4_rect.topleft = bantik4_target.topleft
                    is_dressed["bantik4"] = True
                    is_dressed["jashilbantik"] = False
                    is_dressed["jashilkepka"] = False
                    is_dressed["shapka"] = False
                    is_dressed["kizilshlyapa"] = False
                    is_dressed["tumak"] = False
                    is_dressed["tumak1"] = False
                    is_dressed["tumak2"] = False
                    is_dressed["tumak3"] = False
                    is_dressed["shlyapa"] = False
                    is_dressed["kizilbantik"] = False
                    is_dressed["bantik1"] = False
                    is_dressed["bantik2"] = False
                    is_dressed["bantik3"] = False
                    is_dressed["bantik"] = False
                    is_dressed["bantik5"] = False
                    is_dressed["doll"] = False
                    jashilbantik_rect.topleft = (282, 105)
                    kizilbantik_rect.topleft = (352, 112)
                    bantik_rect.topleft = (254, 170)
                    bantik1_rect.topleft = (245, 231)
                    bantik2_rect.topleft = (242, 300) 
                    bantik3_rect.topleft = (378, 176)
                    doll_rect.topleft = (128, 140)
                    bantik5_rect.topleft = (392, 300)
                    kizilshlyapa_rect.topleft = (100, 12)
                    jashilkepka_rect.topleft = (1, 18)
                    shapka_rect.topleft = (184, 19)
                    shlyapa_rect.topleft = (261, 22)
                    tumak_rect.topleft = (392, 22)
                    tumak1_rect.topleft = (472, 22)
                    tumak2_rect.topleft = (551, 22)
                    tumak3_rect.topleft = (634, 22)
                        
                elif selected_item == "bantik5" and bantik5_target.colliderect(bantik5_rect):
                    bantik5_rect.topleft = bantik5_target.topleft
                    is_dressed["bantik5"] = True
                    is_dressed["jashilbantik"] = False
                    is_dressed["jashilkepka"] = False
                    is_dressed["shapka"] = False
                    is_dressed["kizilshlyapa"] = False
                    is_dressed["tumak"] = False
                    is_dressed["tumak1"] = False
                    is_dressed["tumak2"] = False
                    is_dressed["tumak3"] = False
                    is_dressed["shlyapa"] = False
                    is_dressed["kizilbantik"] = False
                    is_dressed["bantik1"] = False
                    is_dressed["bantik2"] = False
                    is_dressed["bantik3"] = False
                    is_dressed["bantik4"] = False
                    is_dressed["bantik"] = False
                    is_dressed["doll"] = False
                    jashilbantik_rect.topleft = (282, 105)
                    kizilbantik_rect.topleft = (352, 112)
                    bantik_rect.topleft = (254, 170)
                    bantik1_rect.topleft = (245, 231)
                    bantik2_rect.topleft = (242, 300) 
                    bantik3_rect.topleft = (378, 176)
                    bantik4_rect.topleft = (385, 230)
                    doll_rect.topleft = (128, 140)
                    kizilshlyapa_rect.topleft = (100, 12)
                    jashilkepka_rect.topleft = (1, 18)
                    shapka_rect.topleft = (184, 19)
                    shlyapa_rect.topleft = (261, 22)
                    tumak_rect.topleft = (392, 22)
                    tumak1_rect.topleft = (472, 22)
                    tumak2_rect.topleft = (551, 22)
                    tumak3_rect.topleft = (634, 22)
                        
                
                elif selected_item == "jashilkepka" and jashilkepka_target.colliderect(jashilkepka_rect):
                    jashilkepka_rect.topleft = jashilkepka_target.topleft
                    is_dressed["jashilkepka"] = True
                    is_dressed["jashilbantik"] = False
                    is_dressed["kizilshlyapa"] = False
                    is_dressed["shapka"] = False
                    is_dressed["shlyapa"] = False
                    is_dressed["tumak"] = False
                    is_dressed["tumak1"] = False
                    is_dressed["tumak2"] = False
                    is_dressed["tumak3"] = False
                    is_dressed["kizilbantik"] = False
                    is_dressed["bantik"] = False
                    is_dressed["bantik1"] = False
                    is_dressed["bantik2"] = False
                    is_dressed["bantik3"] = False
                    is_dressed["bantik4"] = False
                    is_dressed["bantik5"] = False
                    is_dressed["doll"] = False
                    jashilbantik_rect.topleft = (282, 105)
                    kizilbantik_rect.topleft = (352, 112)
                    bantik_rect.topleft = (254, 170)
                    bantik1_rect.topleft = (245, 231)
                    bantik2_rect.topleft = (242, 300) 
                    bantik3_rect.topleft = (378, 176)
                    bantik4_rect.topleft = (385, 230)
                    bantik5_rect.topleft = (392, 300)
                    kizilshlyapa_rect.topleft = (100, 12)
                    doll_rect.topleft = (128, 140)
                    shapka_rect.topleft = (184, 19)
                    shlyapa_rect.topleft = (261, 22)
                    tumak_rect.topleft = (392, 22)
                    tumak1_rect.topleft = (472, 22)
                    tumak2_rect.topleft = (551, 22)
                    tumak3_rect.topleft = (634, 22)
                        
                elif selected_item == "kizilshlyapa" and kizilshlyapa_target.colliderect(kizilshlyapa_rect):
                    kizilshlyapa_rect.topleft = kizilshlyapa_target.topleft
                    is_dressed["kizilshlyapa"] = True
                    is_dressed["jashilbantik"] = False
                    is_dressed["jashilkepka"] = False
                    is_dressed["shapka"] = False
                    is_dressed["shlyapa"] = False
                    is_dressed["tumak"] = False
                    is_dressed["tumak1"] = False
                    is_dressed["tumak2"] = False
                    is_dressed["tumak3"] = False
                    is_dressed["kizilbantik"] = False
                    is_dressed["bantik"] = False
                    is_dressed["bantik1"] = False
                    is_dressed["bantik2"] = False
                    is_dressed["bantik3"] = False
                    is_dressed["bantik4"] = False
                    is_dressed["bantik5"] = False
                    is_dressed["doll"] = False
                    jashilbantik_rect.topleft = (282, 105)
                    kizilbantik_rect.topleft = (352, 112)
                    bantik_rect.topleft = (254, 170)
                    bantik1_rect.topleft = (245, 231)
                    bantik2_rect.topleft = (242, 300) 
                    bantik3_rect.topleft = (378, 176)
                    bantik4_rect.topleft = (385, 230)
                    bantik5_rect.topleft = (392, 300)
                    doll_rect.topleft = (128, 140)
                    jashilkepka_rect.topleft = (1, 18)
                    shapka_rect.topleft = (184, 19)
                    shlyapa_rect.topleft = (261, 22)
                    tumak_rect.topleft = (392, 22)
                    tumak1_rect.topleft = (472, 22)
                    tumak2_rect.topleft = (551, 22)
                    tumak3_rect.topleft = (634, 22)
                        
                elif selected_item == "shapka" and shapka_target.colliderect(shapka_rect):
                    shapka_rect.topleft = shapka_target.topleft
                    is_dressed["shapka"] = True
                    is_dressed["jashilbantik"] = False
                    is_dressed["jashilkepka"] = False
                    is_dressed["tumak"] = False
                    is_dressed["tumak1"] = False
                    is_dressed["tumak2"] = False
                    is_dressed["tumak3"] = False
                    is_dressed["kizilshlyapa"] = False
                    is_dressed["shlyapa"] = False
                    is_dressed["kizilbantik"] = False
                    is_dressed["bantik"] = False
                    is_dressed["bantik1"] = False
                    is_dressed["bantik2"] = False
                    is_dressed["bantik3"] = False
                    is_dressed["bantik4"] = False
                    is_dressed["bantik5"] = False
                    is_dressed["doll"] = False
                    jashilbantik_rect.topleft = (282, 105)
                    kizilbantik_rect.topleft = (352, 112)
                    bantik_rect.topleft = (254, 170)
                    bantik1_rect.topleft = (245, 231)
                    bantik2_rect.topleft = (242, 300) 
                    bantik3_rect.topleft = (378, 176)
                    bantik4_rect.topleft = (385, 230)
                    bantik5_rect.topleft = (392, 300)
                    kizilshlyapa_rect.topleft = (100, 12)
                    jashilkepka_rect.topleft = (1, 18)
                    doll_rect.topleft = (128, 140)
                    shlyapa_rect.topleft = (261, 22)
                    tumak_rect.topleft = (392, 22)
                    tumak1_rect.topleft = (472, 22)
                    tumak2_rect.topleft = (551, 22)
                    tumak3_rect.topleft = (634, 22)
                        
                elif selected_item == "shlyapa" and shlyapa_target.colliderect(shlyapa_rect):
                    shlyapa_rect.topleft = shlyapa_target.topleft
                    is_dressed["shlyapa"] = True
                    is_dressed["jashilbantik"] = False
                    is_dressed["jashilkepka"] = False
                    is_dressed["shapka"] = False
                    is_dressed["kizilshlyapa"] = False
                    is_dressed["tumak"] = False
                    is_dressed["tumak1"] = False
                    is_dressed["tumak2"] = False
                    is_dressed["tumak3"] = False
                    is_dressed["kizilbantik"] = False
                    is_dressed["bantik"] = False
                    is_dressed["bantik1"] = False
                    is_dressed["bantik2"] = False
                    is_dressed["bantik3"] = False
                    is_dressed["bantik4"] = False
                    is_dressed["bantik5"] = False
                    is_dressed["doll"] = False
                    jashilbantik_rect.topleft = (282, 105)
                    kizilbantik_rect.topleft = (352, 112)
                    bantik_rect.topleft = (254, 170)
                    bantik1_rect.topleft = (245, 231)
                    bantik2_rect.topleft = (242, 300) 
                    bantik3_rect.topleft = (378, 176)
                    bantik4_rect.topleft = (385, 230)
                    bantik5_rect.topleft = (392, 300)
                    kizilshlyapa_rect.topleft = (100, 12)
                    jashilkepka_rect.topleft = (1, 18)
                    shapka_rect.topleft = (184, 19)
                    doll_rect.topleft = (128, 140)
                    tumak_rect.topleft = (392, 22)
                    tumak1_rect.topleft = (472, 22)
                    tumak2_rect.topleft = (551, 22)
                    tumak3_rect.topleft = (634, 22)
                        
                elif selected_item == "tumak" and tumak_target.colliderect(tumak_rect):
                    tumak_rect.topleft = tumak_target.topleft
                    is_dressed["tumak"] = True
                    is_dressed["jashilbantik"] = False
                    is_dressed["jashilkepka"] = False
                    is_dressed["shapka"] = False
                    is_dressed["kizilshlyapa"] = False
                    is_dressed["bantik5"] = False
                    is_dressed["tumak1"] = False
                    is_dressed["tumak2"] = False
                    is_dressed["tumak3"] = False
                    is_dressed["shlyapa"] = False
                    is_dressed["kizilbantik"] = False
                    is_dressed["bantik1"] = False
                    is_dressed["bantik2"] = False
                    is_dressed["bantik3"] = False
                    is_dressed["bantik4"] = False
                    is_dressed["bantik"] = False
                    is_dressed["doll"] = False
                    jashilbantik_rect.topleft = (282, 105)
                    kizilbantik_rect.topleft = (352, 112)
                    bantik_rect.topleft = (254, 170)
                    bantik1_rect.topleft = (245, 231)
                    bantik2_rect.topleft = (242, 300) 
                    bantik3_rect.topleft = (378, 176)
                    bantik4_rect.topleft = (385, 230)
                    bantik5_rect.topleft = (392, 300)
                    kizilshlyapa_rect.topleft = (100, 12)
                    jashilkepka_rect.topleft = (1, 18)
                    shapka_rect.topleft = (184, 19)
                    shlyapa_rect.topleft = (261, 22)
                    doll_rect.topleft = (128, 140)
                    tumak1_rect.topleft = (472, 22)
                    tumak2_rect.topleft = (551, 22)
                    tumak3_rect.topleft = (634, 22)
                        
                elif selected_item == "tumak1" and tumak1_target.colliderect(tumak1_rect):
                    tumak1_rect.topleft = tumak1_target.topleft
                    is_dressed["tumak1"] = True
                    is_dressed["jashilbantik"] = False
                    is_dressed["jashilkepka"] = False
                    is_dressed["shapka"] = False
                    is_dressed["kizilshlyapa"] = False
                    is_dressed["bantik5"] = False
                    is_dressed["tumak"] = False
                    is_dressed["tumak2"] = False
                    is_dressed["tumak3"] = False
                    is_dressed["shlyapa"] = False
                    is_dressed["kizilbantik"] = False
                    is_dressed["bantik1"] = False
                    is_dressed["bantik2"] = False
                    is_dressed["bantik3"] = False
                    is_dressed["bantik4"] = False
                    is_dressed["bantik"] = False
                    is_dressed["doll"] = False
                    jashilbantik_rect.topleft = (282, 105)
                    kizilbantik_rect.topleft = (352, 112)
                    bantik_rect.topleft = (254, 170)
                    bantik1_rect.topleft = (245, 231)
                    bantik2_rect.topleft = (242, 300) 
                    bantik3_rect.topleft = (378, 176)
                    bantik4_rect.topleft = (385, 230)
                    bantik5_rect.topleft = (392, 300)
                    kizilshlyapa_rect.topleft = (100, 12)
                    jashilkepka_rect.topleft = (1, 18)
                    shapka_rect.topleft = (184, 19)
                    shlyapa_rect.topleft = (261, 22)
                    tumak_rect.topleft = (392, 22)
                    doll_rect.topleft = (128, 140)
                    tumak2_rect.topleft = (551, 22)
                    tumak3_rect.topleft = (634, 22)
                        
                elif selected_item == "tumak2" and tumak2_target.colliderect(tumak2_rect):
                    tumak2_rect.topleft = tumak2_target.topleft
                    is_dressed["tumak2"] = True
                    is_dressed["jashilbantik"] = False
                    is_dressed["jashilkepka"] = False
                    is_dressed["shapka"] = False
                    is_dressed["kizilshlyapa"] = False
                    is_dressed["bantik5"] = False
                    is_dressed["tumak1"] = False
                    is_dressed["tumak"] = False
                    is_dressed["tumak3"] = False
                    is_dressed["shlyapa"] = False
                    is_dressed["kizilbantik"] = False
                    is_dressed["bantik1"] = False
                    is_dressed["bantik2"] = False
                    is_dressed["bantik3"] = False
                    is_dressed["bantik4"] = False
                    is_dressed["bantik"] = False
                    is_dressed["doll"] = False
                    jashilbantik_rect.topleft = (282, 105)
                    kizilbantik_rect.topleft = (352, 112)
                    bantik_rect.topleft = (254, 170)
                    bantik1_rect.topleft = (245, 231)
                    bantik2_rect.topleft = (242, 300) 
                    bantik3_rect.topleft = (378, 176)
                    bantik4_rect.topleft = (385, 230)
                    bantik5_rect.topleft = (392, 300)
                    kizilshlyapa_rect.topleft = (100, 12)
                    jashilkepka_rect.topleft = (1, 18)
                    shapka_rect.topleft = (184, 19)
                    shlyapa_rect.topleft = (261, 22)
                    tumak_rect.topleft = (392, 22)
                    tumak1_rect.topleft = (472, 22)
                    doll_rect.topleft = (128, 140)
                    tumak3_rect.topleft = (634, 22)
                        
                elif selected_item == "tumak3" and tumak3_target.colliderect(tumak3_rect):
                    tumak3_rect.topleft = tumak3_target.topleft
                    is_dressed["tumak3"] = True
                    is_dressed["jashilbantik"] = False
                    is_dressed["jashilkepka"] = False
                    is_dressed["shapka"] = False
                    is_dressed["kizilshlyapa"] = False
                    is_dressed["bantik5"] = False
                    is_dressed["tumak1"] = False
                    is_dressed["tumak2"] = False
                    is_dressed["tumak"] = False
                    is_dressed["shlyapa"] = False
                    is_dressed["kizilbantik"] = False
                    is_dressed["bantik1"] = False
                    is_dressed["bantik2"] = False
                    is_dressed["bantik3"] = False
                    is_dressed["bantik4"] = False
                    is_dressed["bantik"] = False
                    is_dressed["doll"] = False
                    jashilbantik_rect.topleft = (282, 105)
                    kizilbantik_rect.topleft = (352, 112)
                    bantik_rect.topleft = (254, 170)
                    bantik1_rect.topleft = (245, 231)
                    bantik2_rect.topleft = (242, 300) 
                    bantik3_rect.topleft = (378, 176)
                    bantik4_rect.topleft = (385, 230)
                    bantik5_rect.topleft = (392, 300)
                    kizilshlyapa_rect.topleft = (100, 12)
                    jashilkepka_rect.topleft = (1, 18)
                    shapka_rect.topleft = (184, 19)
                    shlyapa_rect.topleft = (261, 22)
                    tumak_rect.topleft = (392, 22)
                    tumak1_rect.topleft = (472, 22)
                    tumak2_rect.topleft = (551, 22)
                    doll_rect.topleft = (128, 140)
                        
                    
                    
                elif selected_item == "ochka" and ochka_target.colliderect(ochka_rect):
                    ochka_rect.topleft = ochka_target.topleft
                    is_dressed["ochka"] = True
                    is_dressed["ochka1"] = False
                    is_dressed["ochka2"] = False
                    is_dressed["doll"] = False
                    doll_rect.topleft = (128, 140)
                    ochka1_rect.topleft = (326, 449)
                    ochka2_rect.topleft = (390, 447)
                        
                elif selected_item == "ochka1" and ochka1_target.colliderect(ochka1_rect):
                    ochka1_rect.topleft = ochka1_target.topleft
                    is_dressed["ochka1"] = True
                    is_dressed["ochka"] = False
                    is_dressed["ochka2"] = False
                    is_dressed["doll"] = False
                    ochka_rect.topleft = (270, 451)
                    doll_rect.topleft = (128, 140)
                    ochka2_rect.topleft = (390, 447)
                        
                elif selected_item == "ochka2" and ochka2_target.colliderect(ochka2_rect):
                    ochka2_rect.topleft = ochka2_target.topleft
                    is_dressed["ochka2"] = True
                    is_dressed["ochka1"] = False
                    is_dressed["ochka"] = False
                    is_dressed["doll"] = False
                    ochka_rect.topleft = (270, 451)
                    ochka1_rect.topleft = (326, 449)
                    doll_rect.topleft = (128, 140)
                        
                elif selected_item == "sumka" and sumka_target.colliderect(sumka_rect):
                    sumka_rect.topleft = sumka_target.topleft
                    is_dressed["sumka"] = True
                    is_dressed["sumka1"] = False
                    is_dressed["sumka2"] = False
                    is_dressed["sumka3"] = False
                    is_dressed["doll"] = False
                    doll_rect.topleft = (128, 140)
                    sumka1_rect.topleft = (365, 491)
                    sumka2_rect.topleft = (280, 565)
                    sumka3_rect.topleft = (370, 577)
                        
                elif selected_item == "sumka1" and sumka1_target.colliderect(sumka1_rect):
                    sumka1_rect.topleft = sumka1_target.topleft
                    is_dressed["sumka1"] = True
                    is_dressed["sumka"] = False
                    is_dressed["sumka2"] = False
                    is_dressed["sumka3"] = False
                    is_dressed["doll"] = False
                    sumka_rect.topleft = (280, 494)
                    doll_rect.topleft = (128, 140)
                    sumka2_rect.topleft = (280, 565)
                    sumka3_rect.topleft = (370, 577)
                        
                elif selected_item == "sumka2" and sumka2_target.colliderect(sumka2_rect):
                    sumka2_rect.topleft = sumka2_target.topleft
                    is_dressed["sumka2"] = True
                    is_dressed["sumka1"] = False
                    is_dressed["sumka"] = False
                    is_dressed["sumka3"] = False
                    is_dressed["doll"] = False
                    sumka_rect.topleft = (280, 494)
                    sumka1_rect.topleft = (365, 491)
                    doll_rect.topleft = (128, 140)
                    sumka3_rect.topleft = (370, 577)
                        
                elif selected_item == "sumka3" and sumka3_target.colliderect(sumka3_rect):
                    sumka3_rect.topleft = sumka3_target.topleft
                    is_dressed["sumka3"] = True
                    is_dressed["sumka1"] = False
                    is_dressed["sumka2"] = False
                    is_dressed["sumka"] = False
                    is_dressed["doll"] = False
                    sumka_rect.topleft = (280, 494)
                    sumka1_rect.topleft = (365, 491)
                    sumka2_rect.topleft = (280, 565)
                    doll_rect.topleft = (128, 140)
                       
                else:
                    namesto(selected_item, rect)
                    # Вернуть иконку на место
            selected_item = None

        elif event.type == MOUSEMOTION and selected_item:
            mx, my = event.pos
            if selected_item == "akoinok":
                akoinok_rect.topleft = (mx - offset_x, my - offset_y)
            elif selected_item == "bozsapog":
                bozsapog_rect.topleft = (mx - offset_x, my - offset_y)
            elif selected_item == "sapog":
                sapog_rect.topleft = (mx - offset_x, my - offset_y)
            elif selected_item == "jashilbantik":
                jashilbantik_rect.topleft = (mx - offset_x, my - offset_y)
            elif selected_item == "kizilbantik":
                kizilbantik_rect.topleft = (mx - offset_x, my - offset_y)
            elif selected_item == "bantik":
                bantik_rect.topleft = (mx - offset_x, my - offset_y)
            elif selected_item == "bantik1":
                bantik1_rect.topleft = (mx - offset_x, my - offset_y)
            elif selected_item == "bantik2":
                bantik2_rect.topleft = (mx - offset_x, my - offset_y)
            elif selected_item == "bantik3":
                bantik3_rect.topleft = (mx - offset_x, my - offset_y)
            elif selected_item == "bantik4":
                bantik4_rect.topleft = (mx - offset_x, my - offset_y)
            elif selected_item == "bantik5":
                bantik5_rect.topleft = (mx - offset_x, my - offset_y)
            
                
            elif selected_item == "jashilshim":
                jashilshim_rect.topleft = (mx - offset_x, my - offset_y)
            elif selected_item == "zebrakoinok":
                zebrakoinok_rect.topleft = (mx - offset_x, my - offset_y)
            elif selected_item == "karabuts":
                karabuts_rect.topleft = (mx - offset_x, my - offset_y)
            elif selected_item == "karayubka":
                karayubka_rect.topleft = (mx - offset_x, my - offset_y)
            elif selected_item == "sariyubka":
                sariyubka_rect.topleft = (mx - offset_x, my - offset_y)
            elif selected_item == "kemsel":
                kemsel_rect.topleft = (mx - offset_x, my - offset_y)
            elif selected_item == "jashiljemper":
                jashiljemper_rect.topleft = (mx - offset_x, my - offset_y)
            elif selected_item == "sarijemper":
                sarijemper_rect.topleft = (mx - offset_x, my - offset_y)
            elif selected_item == "kokbuts":
                kokbuts_rect.topleft = (mx - offset_x, my - offset_y)
            elif selected_item == "kokoinok":
                kokoinok_rect.topleft = (mx - offset_x, my - offset_y)
                
            elif selected_item == "kokshim":
                kokshim_rect.topleft = (mx - offset_x, my - offset_y)
            elif selected_item == "kizilbuts":
                kizilbuts_rect.topleft = (mx - offset_x, my - offset_y)  
            elif selected_item == "kizilkoinok":
                kizilkoinok_rect.topleft = (mx - offset_x, my - offset_y) 
            elif selected_item == "ochka":
                ochka_rect.topleft = (mx - offset_x, my - offset_y) 
            elif selected_item == "ochka1":
                ochka1_rect.topleft = (mx - offset_x, my - offset_y) 
            elif selected_item == "ochka2":
                ochka2_rect.topleft = (mx - offset_x, my - offset_y) 
            elif selected_item == "sumka":
                sumka_rect.topleft = (mx - offset_x, my - offset_y) 
            elif selected_item == "sumka1":
                sumka1_rect.topleft = (mx - offset_x, my - offset_y) 
            elif selected_item == "sumka2":
                sumka2_rect.topleft = (mx - offset_x, my - offset_y) 
            elif selected_item == "sumka3":
                sumka3_rect.topleft = (mx - offset_x, my - offset_y) 
            elif selected_item == "purpurkoinok":
                purpurkoinok_rect.topleft = (mx - offset_x, my - offset_y) 
            elif selected_item == "yubka":
                yubka_rect.topleft = (mx - offset_x, my - offset_y) 
            elif selected_item == "yubka1":
                yubka1_rect.topleft = (mx - offset_x, my - offset_y) 
            elif selected_item == "yubka2":
                yubka2_rect.topleft = (mx - offset_x, my - offset_y) 
            elif selected_item == "yubka3":
                yubka3_rect.topleft = (mx - offset_x, my - offset_y) 
            elif selected_item == "karakoinok":
                karakoinok_rect.topleft = (mx - offset_x, my - offset_y) 
            elif selected_item == "sarikoinok":
                sarikoinok_rect.topleft = (mx - offset_x, my - offset_y) 
            elif selected_item == "kizillyamka":
                kizillyamka_rect.topleft = (mx - offset_x, my - offset_y) 
            elif selected_item == "doll":
                doll_rect.topleft = (mx - offset_x, my - offset_y) 
            elif selected_item == "jashilkepka":
                jashilkepka_rect.topleft = (mx - offset_x, my - offset_y)
            elif selected_item == "kizilshlyapa":
                kizilshlyapa_rect.topleft = (mx - offset_x, my - offset_y)
            elif selected_item == "shapka":
                shapka_rect.topleft = (mx - offset_x, my - offset_y)
            elif selected_item == "shlyapa":
                shlyapa_rect.topleft = (mx - offset_x, my - offset_y)
            elif selected_item == "akshim":
                akshim_rect.topleft = (mx - offset_x, my - offset_y)
            elif selected_item == "bozshim":
                bozshim_rect.topleft = (mx - offset_x, my - offset_y)
            elif selected_item == "klesh":
                klesh_rect.topleft = (mx - offset_x, my - offset_y)
            elif selected_item == "jinsi":
                jinsi_rect.topleft = (mx - offset_x, my - offset_y)
            elif selected_item == "tumak":
                tumak_rect.topleft = (mx - offset_x, my - offset_y)
            elif selected_item == "tumak1":
                tumak1_rect.topleft = (mx - offset_x, my - offset_y)
            elif selected_item == "tumak2":
                tumak2_rect.topleft = (mx - offset_x, my - offset_y)
            elif selected_item == "tumak3":
                tumak3_rect.topleft = (mx - offset_x, my - offset_y)
                
    # Отрисовываем одежду: маленькую или большую
    
    if is_dressed["doll"]:
        screen.blit(doll_big, doll_rect)
    else:
        screen.blit(doll_small, doll_rect)
        
    if is_dressed["karabuts"]:
        screen.blit(karabuts_big, karabuts_rect)
    else:
        screen.blit(karabuts_small, karabuts_rect)
    if is_dressed["kokbuts"]:
        screen.blit(kokbuts_big, kokbuts_rect)
    else:
        screen.blit(kokbuts_small, kokbuts_rect)
    if is_dressed["kizilbuts"]:
        screen.blit(kizilbuts_big, kizilbuts_rect)
    else:
        screen.blit(kizilbuts_small, kizilbuts_rect)
    if is_dressed["ochka"]:
        screen.blit(ochka_big, ochka_rect)
    else:
        screen.blit(ochka_small, ochka_rect)
    if is_dressed["ochka1"]:
        screen.blit(ochka1_big, ochka1_rect)
    else:
        screen.blit(ochka1_small, ochka1_rect)
    if is_dressed["ochka2"]:
        screen.blit(ochka2_big, ochka2_rect)
    else:
        screen.blit(ochka2_small, ochka2_rect)
        
    

    if is_dressed["jashilbantik"]:
        screen.blit(jashilbantik_big, jashilbantik_rect)
    else:
        screen.blit(jashilbantik_small, jashilbantik_rect)
    if is_dressed["kizilbantik"]:
        screen.blit(kizilbantik_big, kizilbantik_rect)
    else:
        screen.blit(kizilbantik_small, kizilbantik_rect)
    if is_dressed["bantik"]:
        screen.blit(bantik_big, bantik_rect)
    else:
        screen.blit(bantik_small, bantik_rect)
        
    if is_dressed["bantik1"]:
        screen.blit(bantik1_big, bantik1_rect)
    else:
        screen.blit(bantik1_small, bantik1_rect)
        
    if is_dressed["bantik2"]:
        screen.blit(bantik2_big, bantik2_rect)
    else:
        screen.blit(bantik2_small, bantik2_rect)
    if is_dressed["bantik3"]:
        screen.blit(bantik3_big, bantik3_rect)
    else:
        screen.blit(bantik3_small, bantik3_rect)
    if is_dressed["bantik4"]:
        screen.blit(bantik4_big, bantik4_rect)
    else:
        screen.blit(bantik4_small, bantik4_rect)
    if is_dressed["bantik5"]:
        screen.blit(bantik5_big, bantik5_rect)
    else:
        screen.blit(bantik5_small, bantik5_rect)
        
    if is_dressed["jashilkepka"]:
        screen.blit(jashilkepka_big, jashilkepka_rect)
    else:
        screen.blit(jashilkepka_small, jashilkepka_rect)
    if is_dressed["kizilshlyapa"]:
        screen.blit(kizilshlyapa_big, kizilshlyapa_rect)
    else:
        screen.blit(kizilshlyapa_small, kizilshlyapa_rect)
    if is_dressed["shapka"]:
        screen.blit(shapka_big, shapka_rect)
    else:
        screen.blit(shapka_small, shapka_rect)
    if is_dressed["shlyapa"]:
        screen.blit(shlyapa_big, shlyapa_rect)
    else:
        screen.blit(shlyapa_small, shlyapa_rect)
    if is_dressed["tumak"]:
        screen.blit(tumak_big, tumak_rect)
    else:
        screen.blit(tumak_small, tumak_rect)
    if is_dressed["tumak1"]:
        screen.blit(tumak1_big, tumak1_rect)
    else:
        screen.blit(tumak1_small, tumak1_rect)
    if is_dressed["tumak2"]:
        screen.blit(tumak2_big, tumak2_rect)
    else:
        screen.blit(tumak2_small, tumak2_rect)
    if is_dressed["tumak3"]:
        screen.blit(tumak3_big, tumak3_rect)
    else:
        screen.blit(tumak3_small, tumak3_rect)
        
   
    if is_dressed["bozsapog"]:
        screen.blit(bozsapog_big, bozsapog_rect)
    else:
        screen.blit(bozsapog_small, bozsapog_rect)
    if is_dressed["jashilshim"]:
        screen.blit(jashilshim_big, jashilshim_rect)
    else:
        screen.blit(jashilshim_small, jashilshim_rect)
        
    
    if is_dressed["sapog"]:
        screen.blit(sapog_big, sapog_rect)
    else:
        screen.blit(sapog_small, sapog_rect)
   
    if is_dressed["kokshim"]:
        screen.blit(kokshim_big, kokshim_rect)
    else:
        screen.blit(kokshim_small, kokshim_rect)
    if is_dressed["bozshim"]:
        screen.blit(bozshim_big, bozshim_rect)
    else:
        screen.blit(bozshim_small, bozshim_rect)
        
    if is_dressed["klesh"]:
        screen.blit(klesh_big, klesh_rect)
    else:
        screen.blit(klesh_small, klesh_rect)
        
    
    
    if is_dressed["akshim"]:
        screen.blit(akshim_big, akshim_rect)
    else:
        screen.blit(akshim_small, akshim_rect)
        
    if is_dressed["yubka"]:
        screen.blit(yubka_big, yubka_rect)
    else:
        screen.blit(yubka_small, yubka_rect)
    if is_dressed["yubka1"]:
        screen.blit(yubka1_big, yubka1_rect)
    else:
        screen.blit(yubka1_small, yubka1_rect)
    if is_dressed["yubka2"]:
        screen.blit(yubka2_big, yubka2_rect)
    else:
        screen.blit(yubka2_small, yubka2_rect)
    
    
    if is_dressed["akoinok"]:
        screen.blit(akoinok_big, akoinok_rect)
    else:
        screen.blit(akoinok_small, akoinok_rect)
    if is_dressed["kokoinok"]:
        screen.blit(kokoinok_big, kokoinok_rect)
    else:
        screen.blit(kokoinok_small, kokoinok_rect)
    if is_dressed["sarikoinok"]:
        screen.blit(sarikoinok_big, sarikoinok_rect)
    else:
        screen.blit(sarikoinok_small, sarikoinok_rect)
    if is_dressed["jinsi"]:
        screen.blit(jinsi_big, jinsi_rect)
    else:
        screen.blit(jinsi_small, jinsi_rect)
    if is_dressed["karayubka"]:
        screen.blit(karayubka_big, karayubka_rect)
    else:
        screen.blit(karayubka_small, karayubka_rect)
    if is_dressed["sariyubka"]:
        screen.blit(sariyubka_big, sariyubka_rect)
    else:
        screen.blit(sariyubka_small, sariyubka_rect)
        
    if is_dressed["purpurkoinok"]:
        screen.blit(purpurkoinok_big, purpurkoinok_rect)
    else:
        screen.blit(purpurkoinok_small, purpurkoinok_rect)
    if is_dressed["zebrakoinok"]:
        screen.blit(zebrakoinok_big, zebrakoinok_rect)
    else:
        screen.blit(zebrakoinok_small, zebrakoinok_rect)
    if is_dressed["karakoinok"]:
        screen.blit(karakoinok_big, karakoinok_rect)
    else:
        screen.blit(karakoinok_small, karakoinok_rect)
    if is_dressed["kizillyamka"]:
        screen.blit(kizillyamka_big, kizillyamka_rect)
    else:
        screen.blit(kizillyamka_small, kizillyamka_rect)
    if is_dressed["kizilkoinok"]:
        screen.blit(kizilkoinok_big, kizilkoinok_rect)
    else:
        screen.blit(kizilkoinok_small, kizilkoinok_rect)
        
    
    if is_dressed["jashiljemper"]:
        screen.blit(jashiljemper_big, jashiljemper_rect)
    else:
        screen.blit(jashiljemper_small, jashiljemper_rect)
    if is_dressed["sarijemper"]:
        screen.blit(sarijemper_big, sarijemper_rect)
    else:
        screen.blit(sarijemper_small, sarijemper_rect)
    if is_dressed["yubka3"]:
        screen.blit(yubka3_big, yubka3_rect)
    else:
        screen.blit(yubka3_small, yubka3_rect)
    if is_dressed["kemsel"]:
        screen.blit(kemsel_big, kemsel_rect)
    else:
        screen.blit(kemsel_small, kemsel_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
