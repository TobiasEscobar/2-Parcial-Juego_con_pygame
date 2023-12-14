import pygame
from clase_boton_menu import Boton

empezar_img = pygame.image.load("2-Parcial/Juego-Parcial/images/boton_jugar.png").convert_alpha()
tabla_img = pygame.image.load("2-Parcial/Juego-Parcial/images/boton_tabla.png").convert_alpha()
back_img = pygame.image.load('2-Parcial/Juego-Parcial/images/boton_volver.png').convert_alpha()
quit_img = pygame.image.load("2-Parcial/Juego-Parcial/images/boton_salir.png").convert_alpha()


empezar_boton = Boton(555, 325, empezar_img, 1)
tabla_boton = Boton(550, 450, tabla_img, 1)
salir_boton = Boton(590, 575, quit_img, 1)
volver_boton = Boton(200, 650, back_img, 1)
