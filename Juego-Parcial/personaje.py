import pygame
from clase_personaje import Personaje
from sprites  import *
from constantes import * 

#PERSONAJE
posicion_inicial = (H/2 - 350, 670)
tamaño = (75,85)
acumular_daño = 0
hizo_daño = False

#Animaciones del personaje
diccionario_animaciones = {}
diccionario_animaciones["quieto_derecha"] = personaje_quieto_derecho
diccionario_animaciones["quieto_izquierda"] = personaje_quieto_izquierda
diccionario_animaciones["salta"] = personaje_salta
diccionario_animaciones["salta_izquierda"] = personaje_salta_izquierda
diccionario_animaciones["camina_derecha"] = personaje_camina
diccionario_animaciones["camina_izquierda"] = personaje_camina_izquierda


mi_personaje = Personaje(tamaño, diccionario_animaciones, posicion_inicial, 10, 3)

#PISO
piso = pygame.Rect(0,0,W,10)
piso.top = mi_personaje.lados["bottom"].bottom
lados_piso = obtener_rectangulos(piso)


