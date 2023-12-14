import pygame
from constantes import *
from funciones_BD import * 

menu = pygame.image.load("2-Parcial/Juego-Parcial/Sprites/botones menu/foto_menu.jpg")
menu = pygame.transform.scale(menu, TAMAÑO_PANTALLA)

fondo = pygame.image.load("2-Parcial/Juego-Parcial/Sprites/fondo_casa3_copia.png")
fondo = pygame.transform.scale(fondo, TAMAÑO_PANTALLA)

termino_nivel = pygame.image.load("2-Parcial/Juego-Parcial/Sprites/botones menu/menu paso de nivel.png")
termino_nivel = pygame.transform.scale(termino_nivel, TAMAÑO_PANTALLA)

game_over = pygame.image.load("2-Parcial/Juego-Parcial/Sprites/botones menu/game over.png")
game_over = pygame.transform.scale(game_over, TAMAÑO_PANTALLA)

ranking = pygame.image.load("2-Parcial/Juego-Parcial/Sprites/botones menu/foto_menu.jpg")
ranking = pygame.transform.scale(ranking, TAMAÑO_PANTALLA)

termino_juego = pygame.image.load("2-Parcial/Juego-Parcial/Sprites/botones menu/termino juego.png")
termino_juego = pygame.transform.scale(termino_juego, TAMAÑO_PANTALLA)

pygame.init()

def seleccionar_opcion():
    valor = 0
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_click = list(evento.pos)
            if 240 <= posicion_click[0] <= 470 and 290 <= posicion_click[1] <= 450:
                valor = 1
            if 585 <= posicion_click[0] <= 820 and 290 <= posicion_click[1] <= 470:
                valor = 2
            if 940 <= posicion_click[0] <= 1160 and 290 <= posicion_click[1] <= 470:
                print("PASE DE NIVEL")
                valor = 3
            return valor

def volver_menu():
    valor = False
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_click = list(evento.pos)
            if 95 <= posicion_click[0] <= 660 and 190 <= posicion_click[1] <= 765:
                valor = True
            return valor

def pantalla_menu(pantalla):
    pantalla.blit(menu, (0,0))

def pantalla_final(pantalla):
    pantalla.blit(termino_nivel, (0,0))

def pantalla_game_over(pantalla):
    pantalla.blit(game_over, (0,0))

def pantalla_ranking(pantalla):
    pantalla.blit(ranking, (0,0))

def pantalla_termino_juego(pantalla):
    pantalla.blit(termino_juego, (0,0))