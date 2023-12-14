from clase_enemigo import Enemigo
from sprites import *
from constantes import *

diccionario_animaciones_enemigas = {}
diccionario_animaciones_enemigas["quieto_derecha"] = enemigo_quieto
diccionario_animaciones_enemigas["quieto_izquierda"] = enemigo_quieto_izquierda
diccionario_animaciones_enemigas["camina_derecha"] = enemigo_camina
diccionario_animaciones_enemigas["camina_izquierda"] = enemigo_camina_izquierda

tamaño_enemigo = (75,85)

#Enemigos lvl1
posiciones_lvl1 = [(100, 340), (400 ,670), (750 ,500), (1000, 340), (600, 150)]
limites_lvl1 = [(0, 400), (300, 500), (730, 1150), (960, 1400), (600, 1100)]

enemigo_basico = Enemigo(tamaño_enemigo, diccionario_animaciones_enemigas, posiciones_lvl1[0], 5, 3, limites_lvl1[0])
enemigo_basico_dos = Enemigo(tamaño_enemigo, diccionario_animaciones_enemigas, posiciones_lvl1[1], 5, 3, limites_lvl1[1])
enemigo_basico_tres = Enemigo(tamaño_enemigo, diccionario_animaciones_enemigas, posiciones_lvl1[2], 5, 3, limites_lvl1[2])
enemigo_basico_cuatro = Enemigo(tamaño_enemigo, diccionario_animaciones_enemigas, posiciones_lvl1[3], 5, 3, limites_lvl1[3])
enemigo_basico_cinco = Enemigo(tamaño_enemigo, diccionario_animaciones_enemigas, posiciones_lvl1[4], 5, 3, limites_lvl1[4])

#Enemigos lvl2

posiciones_lvl2 = [(430,610), (20 ,280), (290 ,120), (820,120), (730 ,320), (750 ,500), (800,670), (900 ,670)]
limites_lvl2 = [(430, 800), (0, 472), (270, 700), (800,1205), (700 ,1170), (730 ,1280), (800,1100), (850 ,1390)]

enemigo_basico_lvl2 = Enemigo(tamaño_enemigo, diccionario_animaciones_enemigas, posiciones_lvl2[0], 10, 3, limites_lvl2[0])
enemigo_basico_dos_lvl2 = Enemigo(tamaño_enemigo, diccionario_animaciones_enemigas, posiciones_lvl2[1], 10, 3, limites_lvl2[1])
enemigo_basico_tres_lvl2 = Enemigo(tamaño_enemigo, diccionario_animaciones_enemigas, posiciones_lvl2[2], 10, 3, limites_lvl2[2])
enemigo_basico_cuatro_lvl2 = Enemigo(tamaño_enemigo, diccionario_animaciones_enemigas, posiciones_lvl2[3], 10, 3, limites_lvl2[3])
enemigo_basico_cinco_lvl2 = Enemigo(tamaño_enemigo, diccionario_animaciones_enemigas, posiciones_lvl2[4], 10, 3, limites_lvl2[4])
enemigo_basico_seis_lvl2 = Enemigo(tamaño_enemigo, diccionario_animaciones_enemigas, posiciones_lvl2[5], 10, 3, limites_lvl2[5])
enemigo_basico_siete_lvl2 = Enemigo(tamaño_enemigo, diccionario_animaciones_enemigas, posiciones_lvl2[6], 10, 3, limites_lvl2[6])
enemigo_basico_ocho_lvl2 = Enemigo(tamaño_enemigo, diccionario_animaciones_enemigas, posiciones_lvl2[7], 10, 3, limites_lvl2[7])

#Enemigos lvl3

posiciones_lvl3 = [(20,420), (20,270), (20,120), (720,430), (970,80), (730,230)]
limites_lvl3 = [(0,440), (0,440), (0,440), (700,1150), (940,1390), (700,1150)]

enemigo_basico_lvl3 = Enemigo(tamaño_enemigo, diccionario_animaciones_enemigas, posiciones_lvl3[0], 15, 3, limites_lvl3[0])
enemigo_basico_dos_lvl3 = Enemigo(tamaño_enemigo, diccionario_animaciones_enemigas, posiciones_lvl3[1], 15, 3, limites_lvl3[1])
enemigo_basico_tres_lvl3 = Enemigo(tamaño_enemigo, diccionario_animaciones_enemigas, posiciones_lvl3[2], 15, 3, limites_lvl3[2])
enemigo_basico_cuatro_lvl3 = Enemigo(tamaño_enemigo, diccionario_animaciones_enemigas, posiciones_lvl3[3], 15, 3, limites_lvl3[3])
enemigo_basico_cinco_lvl3 = Enemigo(tamaño_enemigo, diccionario_animaciones_enemigas, posiciones_lvl3[4], 15, 3, limites_lvl3[4])
enemigo_basico_seis_lvl3 = Enemigo(tamaño_enemigo, diccionario_animaciones_enemigas, posiciones_lvl3[5], 15, 3, limites_lvl3[5])
enemigo_basico_siete_lvl3 = Enemigo(tamaño_enemigo, diccionario_animaciones_enemigas, posiciones_lvl3[5], 15, 3, limites_lvl3[5])
enemigo_basico_ocho_lvl3 = Enemigo(tamaño_enemigo, diccionario_animaciones_enemigas, posiciones_lvl3[5], 15, 3, limites_lvl3[5])

lista_enemigos = [enemigo_basico, enemigo_basico_dos, enemigo_basico_tres, enemigo_basico_cuatro, enemigo_basico_cinco]

lista_enemigos_2 = [enemigo_basico_lvl2, enemigo_basico_dos_lvl2, enemigo_basico_tres_lvl2, enemigo_basico_cuatro_lvl2, 
                    enemigo_basico_cinco_lvl2, enemigo_basico_seis_lvl2, enemigo_basico_siete_lvl2, enemigo_basico_ocho_lvl2]

lista_enemigos_3 = [enemigo_basico_lvl3, enemigo_basico_dos_lvl3, enemigo_basico_tres_lvl3, enemigo_basico_cuatro_lvl3,
                    enemigo_basico_cinco_lvl3, enemigo_basico_seis_lvl3, enemigo_basico_siete_lvl3, enemigo_basico_ocho_lvl3]

lista_grande_de_enemigos = [lista_enemigos, lista_enemigos_2, lista_enemigos_3]