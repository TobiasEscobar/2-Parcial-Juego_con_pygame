from lista_plataformas import * 
from lista_vidas import *
from constantes import *

def posicionar_plataformas(lista_plataformas, pantalla):
    for plataforma in lista_plataformas:
        plataforma.ubicar_plataforma(pantalla)

def dibujar_rectangulos_plataformas(lista_plataformas, pantalla):
    for plataforma in lista_plataformas:
        plataforma.dibujar_rectangulo(pantalla)

def posicionar_vidas(lista_vidas, pantalla):
    for vida in lista_vidas:
        vida.blitear_vidas(pantalla)

def dibujar_rectangulos_vidas(lista_vidas, pantalla):
    for vida in lista_vidas:
        vida.dibujar_rectangulo(pantalla)

def dibujar_texto(texto, fuente, color_texto, x, y, pantalla):
    imagen = fuente.render(texto, True, color_texto)
    pantalla.blit(imagen, (x, y))

def mostrar_vida_personaje(pantalla,indice):
    lista_vida = ["2-Parcial/Juego-Parcial/Sprites/Vida/vida_imagen_3.png", "2-Parcial/Juego-Parcial/Sprites/Vida/vida_imagen_2.png", "2-Parcial/Juego-Parcial/Sprites/Vida/vida_imagen_1.png"]
    imagen_vida = pygame.image.load(lista_vida[indice])
    imagen_vida_reescalada = pygame.transform.scale(imagen_vida,(70,50))
    pantalla.blit(imagen_vida_reescalada,(500,10))