import pygame
from sprites import obtener_rectangulos

class Vidas():
    def __init__(self, posicion_x, posicion_y):
        self.imagen_vida = pygame.image.load("2-Parcial/Juego-Parcial/Sprites/Vida/vida.png")
        self.imagen_vida = self.reescalar(self.imagen_vida, (50,40))
        self.rectangulo_vida = pygame.Rect(self.imagen_vida.get_rect())
        self.rectangulo_vida.x = posicion_x
        self.rectangulo_vida.y = posicion_y
        self.lados = obtener_rectangulos(self.rectangulo_vida)

    def blitear_vidas(self, pantalla):
        pantalla.blit(self.imagen_vida, self.rectangulo_vida)

    def reescalar(self, imagen,tamaño):
        return pygame.transform.scale(imagen, (tamaño))

    def dibujar_rectangulo(self, pantalla):
        for lado in self.lados:
            pygame.draw.rect(pantalla, "Orange", self.lados[lado], 2)

    def verificar_colision_vidas(self, rectangulo_personaje, vida_personaje):
        colisiono = False
        if self.rectangulo_vida.colliderect(rectangulo_personaje) and vida_personaje < 3:
            colisiono = True
        return colisiono

