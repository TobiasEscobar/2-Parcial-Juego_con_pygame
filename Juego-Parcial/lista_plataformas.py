import pygame
from clase_plataformas import Plataforma

plataforma_1 = pygame.image.load("2-Parcial/Juego-Parcial/Sprites/Plataformas/bloque 1.png")
plataforma_1 = pygame.transform.scale(plataforma_1, (64,64))

plataforma_2 = pygame.image.load("2-Parcial/Juego-Parcial/Sprites/Plataformas/piso largo.png")
plataforma_2 = pygame.transform.scale(plataforma_2, (510,32))

plataforma_3 = pygame.image.load("2-Parcial/Juego-Parcial/Sprites/Plataformas/plataforma larga.png")
plataforma_3 = pygame.transform.scale(plataforma_3, (415,45))

lista_imagenes_plataformas_lvl_1 = [plataforma_1, plataforma_2, plataforma_3]

objeto_1 = Plataforma((270, 690), lista_imagenes_plataformas_lvl_1[0])
objeto_2 = Plataforma((360, 590), lista_imagenes_plataformas_lvl_1[0])
objeto_3 = Plataforma((510, 520), lista_imagenes_plataformas_lvl_1[0])
objeto_4 = Plataforma((560, 360), lista_imagenes_plataformas_lvl_1[0])
objeto_5 = Plataforma((1250, 290), lista_imagenes_plataformas_lvl_1[0])
objeto_6 = Plataforma((600, 223), lista_imagenes_plataformas_lvl_1[1])
objeto_7 = Plataforma((0, 410), lista_imagenes_plataformas_lvl_1[2])
objeto_8 = Plataforma((1000, 410), lista_imagenes_plataformas_lvl_1[2])
objeto_9 = Plataforma((730, 570), lista_imagenes_plataformas_lvl_1[2])
objeto_10 = Plataforma((800, 410), lista_imagenes_plataformas_lvl_1[0])


lista_de_plataformas_lvl1 = [objeto_1, objeto_2, objeto_3, objeto_4, objeto_5, objeto_6, objeto_7, objeto_8, objeto_9, objeto_10]

#NIVEL 2

lista_imagenes_plataformas_lvl_2 = [plataforma_1, plataforma_2, plataforma_3]

objeto_1 = Plataforma((400, 600), lista_imagenes_plataformas_lvl_2[0])
objeto_2 = Plataforma((400, 510), lista_imagenes_plataformas_lvl_2[0])
objeto_3 = Plataforma((400, 420), lista_imagenes_plataformas_lvl_2[0])
objeto_4 = Plataforma((100, 240), lista_imagenes_plataformas_lvl_2[0])
objeto_5 = Plataforma((1280, 360), lista_imagenes_plataformas_lvl_2[0])
objeto_6 = Plataforma((260, 690), lista_imagenes_plataformas_lvl_2[1])
objeto_7 = Plataforma((0, 360), lista_imagenes_plataformas_lvl_2[2])
objeto_8 = Plataforma((270, 200), lista_imagenes_plataformas_lvl_2[2])
objeto_9 = Plataforma((800, 200), lista_imagenes_plataformas_lvl_2[2])
objeto_10 = Plataforma((710, 400), lista_imagenes_plataformas_lvl_2[2])
objeto_11 = Plataforma((790, 560), lista_imagenes_plataformas_lvl_2[1])


lista_de_plataformas_lvl2 = [objeto_1, objeto_2, objeto_3, objeto_4, objeto_5, objeto_6, objeto_7, objeto_8, objeto_9, objeto_10, objeto_11]

#NIVEL 3

lista_imagenes_plataformas_lvl_3 = [plataforma_1, plataforma_2, plataforma_3]

objeto_1 = Plataforma((1200, 650), lista_imagenes_plataformas_lvl_3[0])
objeto_2 = Plataforma((1000, 570), lista_imagenes_plataformas_lvl_3[0])
objeto_3 = Plataforma((520, 440), lista_imagenes_plataformas_lvl_3[0])
objeto_4 = Plataforma((0, 500), lista_imagenes_plataformas_lvl_3[2])
objeto_5 = Plataforma((0, 350), lista_imagenes_plataformas_lvl_3[2])
objeto_6 = Plataforma((0, 200), lista_imagenes_plataformas_lvl_3[2])
objeto_7 = Plataforma((700, 500), lista_imagenes_plataformas_lvl_3[2])
objeto_8 = Plataforma((700, 300), lista_imagenes_plataformas_lvl_3[2])
objeto_9 = Plataforma((990, 150), lista_imagenes_plataformas_lvl_3[2])
objeto_10 = Plataforma((520, 290), lista_imagenes_plataformas_lvl_3[0])
objeto_11 = Plataforma((470, 690), lista_imagenes_plataformas_lvl_3[0])
objeto_12 = Plataforma((770, 160), lista_imagenes_plataformas_lvl_3[0])

lista_de_plataformas_lvl3 = [objeto_1, objeto_2, objeto_3, objeto_4, objeto_5, objeto_6, objeto_7, objeto_8, objeto_9, objeto_10, objeto_11, objeto_12]

lista_grande_de_plataformas = [lista_de_plataformas_lvl1, lista_de_plataformas_lvl2, lista_de_plataformas_lvl3]