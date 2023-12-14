import pygame
import sys
import os
from clase_juego import *
from sprites  import *
from constantes import * 

class EmpezarJuego():
    def __init__(self):
        self.juego = Juego()

    def empezar(self):
        if "bd_ranking.db" not in os.listdir("."):  
            crear_tabla()

        pygame.init()

        RELOJ = pygame.time.Clock()
        while self.juego.jugar:
            RELOJ.tick(FPS)

            pantalla_menu(PANTALLA)

            if self.juego.menu == True:
                if self.juego.juego_pausado == True:
                    pygame.mixer.music.load(ruta_musica)
                    pygame.mixer.music.play(-1)
                    pygame.mixer.music.set_volume(0.1)
                    if self.juego.estado_menu == "inicio":
                        if empezar_boton.dibujar_y_verificar(PANTALLA):
                            self.juego.iniciar_juego = True
                            self.juego.menu = False
                        elif tabla_boton.dibujar_y_verificar(PANTALLA):
                            self.juego.estado_menu = "tabla"
                        elif salir_boton.dibujar_y_verificar(PANTALLA):
                            self.juego.jugar = False
                            pygame.mixer.music.stop()
                    if self.juego.estado_menu == "tabla":
                        self.juego.ver_ranking()
                        if volver_boton.dibujar_y_verificar(PANTALLA):
                            self.juego.estado_menu = "inicio"
                else:
                    dibujar_texto("ESCRIBA SU NOMBRE PARA CONTINUAR", self.juego.fuente_texto, COLOR_NEGRO, 390, 450, PANTALLA)
                    self.juego.escribir_nombre()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_TAB:
                        cambiar_modo()
                    if evento.key == pygame.K_BACKSPACE:
                        self.juego.ingreso = self.juego.ingreso[0:-1]
                    elif evento.key == pygame.K_RETURN:
                        if 3 <= len(self.juego.ingreso) <= 10 and self.juego.ingreso.strip() != "":
                            self.juego.juego_pausado = True
                    else:
                        self.juego.ingreso += evento.unicode

                if evento.type == self.juego.timer_segundos:
                    if self.juego.fin_tiempo == False:
                        self.juego.segundos = int(self.juego.segundos) - 1
                        if int(self.juego.segundos) == 0:
                            self.juego.fin_tiempo = True

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                mi_personaje.que_hace = "derecha"
            elif keys[pygame.K_LEFT]:
                mi_personaje.que_hace = "izquierda"
            elif keys[pygame.K_UP]:
                mi_personaje.que_hace = "salta"
            else:
                mi_personaje.que_hace = "quieto"

            self.juego.iniciar_niveles(lista_grande_de_enemigos, lista_grande_de_plataformas, lista_grande_de_vidas)


            pygame.display.flip()

juego_parcial = EmpezarJuego()
juego_parcial.empezar()