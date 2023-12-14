from sprites import obtener_rectangulos
import pygame

class Plataforma():
    def __init__(self, ubicacion, lista_plataformas):
        self.ancho = ubicacion[0]
        self.alto = ubicacion[1]
        self.imagen_plataforma = lista_plataformas
        self.rectangulo = pygame.Rect(self.imagen_plataforma.get_rect())
        self.rectangulo.x = ubicacion[0]
        self.rectangulo.y = ubicacion[1]
        self.lados = obtener_rectangulos(self.rectangulo)
        self.devolver = False

    def ubicar_plataforma(self, pantalla):
        pantalla.blit(self.imagen_plataforma, (self.rectangulo))

    def dibujar_rectangulo(self, pantalla):
        for lado in self.lados:
            pygame.draw.rect(pantalla, "Orange", self.lados[lado], 2)
