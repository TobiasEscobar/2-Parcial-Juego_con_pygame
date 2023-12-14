import pygame
from constantes import *
from funciones_manejo_de_pantallas import *
from funciones import * 
from funciones_colision import * 
from lista_enemigos import *
from lista_vidas import *
from personaje import *
from botones_menu import *
from modo_programador import *

class Juego():
    def __init__(self):
        pygame.init()

        #Entrada del nombre del jugador
        self.fuente_texto = pygame.font.SysFont("arialblack", 30)
        self.fuente = pygame.font.SysFont("Arial", 20)
        self.ingreso = ""
        self.ingreso_rect = pygame.Rect(600, 320, 200, 30)

        #Timer de tiempo de juego
        self.segundos = "60"
        self.fin_tiempo = False
        self.timer_segundos = pygame.USEREVENT
        pygame.time.set_timer(self.timer_segundos, 1000)

        #Menu
        self.jugar = True
        self.estado_menu = "inicio"
        self.juego_pausado = False
        self.menu = True
        self.pantalla = PANTALLA
        
        #JUEGO
        self.iniciar_juego = False
        self.termino_juego = False
        self.volver_al_menu = False

        #Personaje
        self.murio_personaje = True
        self.personaje = mi_personaje

        #Datos del usuario
        self.fin_tiempo = False
        self.score = 0
        self.mostrar_menu_nombre = True
        self.ingreso_nombre = False

        #Niveles
        self.nivel_actual = 3

    #Datos para el usuario en pantalla

    def tiempo_y_score(self, mostrar_datos):
        if mostrar_datos:
            vista_score = self.fuente.render("Score: " + str(self.score), True, COLOR_BLANCO)
            segundos_texto = self.fuente.render("Tiempo: " + str(self.segundos), True, COLOR_BLANCO)
            self.pantalla.blit(vista_score, (1280,0))
            self.pantalla.blit(segundos_texto, (0,0))

    #daño del personaje a enemigos 

    def personaje_daño(self, lista_enemigos, nivel_actual):
        valor = False
        if nivel_actual == 1:
            for enemigo in lista_enemigos[0]:
                daño = enemigo.daño_a_personaje(self.personaje.lados["main"])
                if daño:
                    vidas = self.personaje.vidas(daño)
                    if vidas:
                        valor = True
        if nivel_actual == 2:
            for enemigo in lista_enemigos[1]:
                daño = enemigo.daño_a_personaje(self.personaje.lados["main"])
                if daño:
                    vidas = self.personaje.vidas(daño)
                    if vidas:
                        valor = True
        if nivel_actual == 3:
            for enemigo in lista_enemigos[2]:
                daño = enemigo.daño_a_personaje(self.personaje.lados["main"])
                if daño:
                    vidas = self.personaje.vidas(daño)
                    if vidas:
                        valor = True
        return valor

    def personaje_recupera_vida(self, lista_vidas, nivel_actual):
        if nivel_actual == 1:
            for vida in lista_vidas[0]:
                recupera_vida = self.personaje.agarrar_vidas(vida.lados["main"])
                if recupera_vida:
                    self.personaje.sumar_vida()
                    print(self.personaje.vida)
        if nivel_actual == 2:
            for vida in lista_vidas[1]:
                recupera_vida = self.personaje.agarrar_vidas(vida.lados["main"])
                if recupera_vida:
                    self.personaje.sumar_vida()
                    print(self.personaje.vida)
        if nivel_actual == 3:
            for vida in lista_vidas[2]:
                recupera_vida = self.personaje.agarrar_vidas(vida.lados["main"])
                if recupera_vida:
                    self.personaje.sumar_vida()
                    print(self.personaje.vida)

    #Dibujar los lados de los objetos que esten en pantalla

    def dibujar_rectangulos(self, lista_plataformas, lista_enemigos, lista_vidas):
        if get_modo():
            for lado in lados_piso:
                pygame.draw.rect(self.pantalla, "Black", lados_piso[lado], 2)
            for lado in self.personaje.lados:
                pygame.draw.rect(self.pantalla, "Orange", self.personaje.lados[lado], 2)
            for enemigo in lista_enemigos:
                for lado in enemigo.lados:
                    pygame.draw.rect(self.pantalla, "Black", enemigo.lados[lado], 2)
            dibujar_rectangulos_plataformas(lista_plataformas, self.pantalla)
            dibujar_rectangulos_vidas(lista_vidas, self.pantalla)

    #Actualizar en pantalla a un personaje o enemigo 
    def actualizar_pantalla(self, un_personaje, lados_piso, tamaño_pantalla):
        un_personaje.update(self.pantalla, lados_piso, tamaño_pantalla)

        if un_personaje.vida > 2 and un_personaje.vida <= 3:
            mostrar_vida_personaje(self.pantalla,0)
        elif un_personaje.vida > 1 and un_personaje.vida <= 2:
            mostrar_vida_personaje(self.pantalla,1)
        elif un_personaje.vida > 0 and un_personaje.vida <= 1:
            mostrar_vida_personaje(self.pantalla,2)

    #logica de niveles

    def niveles(self, lista_plataformas, lista_enemigos, lista_vidas):
        self.pantalla.blit(fondo, (0,0))
        self.pantalla.blit(lista_piso[0], (0,750))
        self.pantalla.blit(lista_piso[1], (480,750))
        self.pantalla.blit(lista_piso[2], (950,750))
        posicionar_plataformas(lista_plataformas, self.pantalla)
        posicionar_vidas(lista_vidas, self.pantalla)

        for enemigo in lista_enemigos:
            self.actualizar_pantalla(enemigo, lados_piso, TAMAÑO_PANTALLA)
        self.actualizar_pantalla(self.personaje, lados_piso, TAMAÑO_PANTALLA)
        
        self.dibujar_rectangulos(lista_plataformas, lista_enemigos, lista_vidas)

    def ubicar_niveles(self, lista_plataformas, lista_enemigos, lista_vidas, nivel_actual):
        if nivel_actual == 1:
            self.niveles(lista_plataformas[0], lista_enemigos[0], lista_vidas[0])
            manejar_colision_plataformas(self.personaje, lista_plataformas[0], lados_piso)
            valor = 1
        elif nivel_actual == 2:
            self.niveles(lista_plataformas[1], lista_enemigos[1], lista_vidas[1])
            manejar_colision_plataformas(self.personaje, lista_plataformas[1], lados_piso)
            valor = 2
        elif nivel_actual == 3:
            self.niveles(lista_plataformas[2], lista_enemigos[2], lista_vidas[2])
            manejar_colision_plataformas(self.personaje, lista_plataformas[2], lados_piso)
            valor = 3
        return valor

    def pasar_nivel(self, lista_enemigos):
        for enemigo in lista_enemigos:
            hacer_daño = self.personaje.dañar_con_salto(enemigo.lados["top"])

            if hacer_daño:
                print("Enemigo muerto")
                enemigo.vida = 0
                self.score += 10

            for enemigo in lista_enemigos:
                if enemigo.vida == 0:
                    lista_enemigos.remove(enemigo)
                    if len(lista_enemigos) == 0:
                        return True


    def que_nivel(self, nivel, lista_enemigos, lista_plataformas, lista_vidas):
        pasar_al_2 = False
        pasar_al_3 = False
        if nivel == 1:
            self.ubicar_niveles(lista_plataformas, lista_enemigos, lista_vidas, 1)
            self.tiempo_y_score(True)
            if self.pasar_nivel(lista_enemigos[0]):
                pantalla_final(self.pantalla)
                pygame.display.flip()
                while pasar_al_2 == False:
                    que_opcion = seleccionar_opcion()
                    match que_opcion:
                        case 1:
                            pass
                        case 2:
                            pass
                        case 3:
                            self.personaje.actualizar_posicion((H/2 - 350, 670))
                            pasar_al_2 = True
                            return 1
        elif nivel == 2:
            self.ubicar_niveles(lista_plataformas, lista_enemigos, lista_vidas, 2)
            self.tiempo_y_score(True)
            if self.pasar_nivel(lista_enemigos[1]):
                pantalla_final(self.pantalla)
                pygame.display.flip()
                while pasar_al_3 == False:
                    que_opcion = seleccionar_opcion()
                    match que_opcion:
                        case 1:
                            pass
                        case 2:
                            pass
                        case 3:
                            self.personaje.actualizar_posicion((H/2 - 350, 670))
                            pasar_al_3 = True
                            return 2
        elif nivel == 3:
            self.ubicar_niveles(lista_plataformas, lista_enemigos, lista_vidas, 3)
            self.tiempo_y_score(True)
            if self.pasar_nivel(lista_enemigos[2]):
                return 3

    #Manejo de menu y fin de juego

    def escribir_nombre(self):
        pygame.draw.rect(self.pantalla,  COLOR_NEGRO, self.ingreso_rect, 2)
        font_input_surface = self.fuente.render(self.ingreso, True, COLOR_NEGRO)
        self.pantalla.blit(font_input_surface, (self.ingreso_rect.x+15, self.ingreso_rect.y+5))
        pygame.display.flip()
    
    def ver_ranking(self):
        pantalla_ranking(self.pantalla)
        mostrar_tabla(self.pantalla)

    def juego_terminado(self):
        if not self.termino_juego:
            self.tiempo_y_score(False)
            pantalla_termino_juego(self.pantalla)
            actualizar_puntaje(self.ingreso, self.score)
            pygame.display.flip()

            while not self.volver_al_menu:
                if volver_menu():
                    self.volver_al_menu = True
                    self.termino_juego = True
                    self.iniciar_juego = False

    def jugador_perdio(self):
        if self.murio_personaje:
            pantalla_game_over(self.pantalla)
            pygame.display.flip()

            while not self.volver_al_menu:
                if volver_menu():
                    self.volver_al_menu = True
                    self.termino_juego = True


    def iniciar_niveles(self, lista_enemigos, lista_plataformas, lista_vidas):
        if self.iniciar_juego:
            if not self.personaje_daño(lista_enemigos, self.nivel_actual) or self.fin_tiempo == True:
                termino_nivel = self.que_nivel(self.nivel_actual, lista_enemigos, lista_plataformas, lista_vidas)
                self.personaje_recupera_vida(lista_vidas, self.nivel_actual)
                if termino_nivel == 1:
                    self.nivel_actual += 1
                    mi_personaje.vida = 3
                    self.segundos = "60"
                if termino_nivel == 2:
                    self.nivel_actual += 1
                    self.segundos = "60"
                if termino_nivel == 3:
                    self.juego_terminado()
                    self.termino_juego = True
                    self.empezar_de_nuevo(lista_enemigos, lista_plataformas, lista_vidas)
            else:
                self.jugador_perdio()
                self.murio_personaje = True
                self.termino_juego = True
                self.empezar_de_nuevo(lista_enemigos, lista_plataformas, lista_vidas)

    def empezar_de_nuevo(self, lista_enemigos, lista_plataformas, lista_vidas):
        if self.termino_juego:
            self.reiniciar_juego(lista_plataformas, lista_enemigos, lista_vidas)
            self.jugar = True
            self.estado_menu = "inicio"
            self.juego_pausado = True
            self.menu = True

    def reiniciar_juego(self, lista_plataformas, lista_enemigos, lista_vidas):
        self.iniciar_juego = False
        self.segundos = "60"
        self.score = 0
        mi_personaje.vida = 3
        self.personaje.actualizar_posicion((H/2 - 350, 670))
        self.nivel_actual = 1
        self.ubicar_niveles(lista_plataformas, lista_enemigos, lista_vidas, self.nivel_actual)

