from sprites import reescalar_imagenes, obtener_rectangulos
import pygame

class Personaje:
    def __init__(self, tamaño, animaciones, posicion_inicial, velocidad, vida):
        #TAMAÑO PERSONAJE
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        #GRAVEDAD
        self.gravedad = 1
        self.potencia_salto = -15
        self.limite_velocidad_caida = 15
        self.esta_saltando = False
        self.esta_en_suelo = True
        #ANIMACIONES
        self.contador_pasos = 0
        self.que_hace = "quieto"
        self.ultimo_movimiento = "derecha"
        self.animaciones = animaciones
        self.reescalar_animaciones()
        #RECTANGULOS
        rectangulo = self.animaciones["camina_derecha"][0].get_rect()
        rectangulo.x = posicion_inicial[0]
        rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulos(rectangulo)
        #MOVIMIENTO
        self.velocidad = velocidad
        self.desplazamiento_y = 0
        #ATRIBUTOS
        self.vida = vida
        self.recupero_vida = False
        self.colisiona = False
        self.hizo_daño = False
        self.invencible = False
        self.tiempo_invencible = 2  
        self.tiempo_inicio_invencible = 0  

    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave], (self.ancho, self.alto))

    def animar(self, pantalla, que_animacion:str):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)

        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        
        pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
        self.contador_pasos += 1

    def mover(self, velocidad, tamaño_pantalla):

        limite_derecho = tamaño_pantalla[0]
        limite_izquierdo = 0

        #Verifica que no se vaya del limite derecho
        if self.lados["main"].right + velocidad > limite_derecho:
            diferencia = limite_derecho - self.lados["main"].right
            if diferencia > 0:
                velocidad = diferencia
            else:
                velocidad = 0

        #Verifica que no se vaya del limite izquierdo
        if self.lados["main"].left + velocidad < limite_izquierdo:
            diferencia = limite_izquierdo - self.lados["main"].left
            if diferencia > 0:
                velocidad = diferencia
            else:
                velocidad = 0

        #Aplica la velocidad a todos los lados del rectangulo
        for lado in self.lados:
            self.lados[lado].x += velocidad

    def aplicar_gravedad(self, pantalla,piso):
        if self.esta_saltando:
            if self.ultimo_movimiento == "derecha":
                self.animar(pantalla, "salta")
            if self.ultimo_movimiento == "izquierda":
                self.animar(pantalla, "salta_izquierda")
                
            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad

            if self.lados["bottom"].colliderect(piso["top"]):
                self.desplazamiento_y = 0
                self.esta_saltando = False
                self.esta_en_suelo = True
                self.lados["main"].bottom = piso["main"].top 
            else:
                self.esta_saltando = True
                self.esta_en_suelo = False

    def update(self, pantalla, piso, tamaño_pantalla):
        match self.que_hace:
            case "derecha":
                self.ultimo_movimiento = "derecha"
                if not self.esta_saltando:
                    self.animar(pantalla, "camina_derecha")
                self.mover(self.velocidad, tamaño_pantalla)
            case "izquierda":
                self.ultimo_movimiento = "izquierda"
                if not self.esta_saltando:
                    self.animar(pantalla, "camina_izquierda")
                self.mover(self.velocidad * - 1, tamaño_pantalla)
            case "salta":
                if not self.esta_saltando:
                    self.esta_saltando = True
                    self.desplazamiento_y = self.potencia_salto
                    if self.ultimo_movimiento == "derecha":
                        self.mover(self.velocidad, tamaño_pantalla)
                    else:
                        self.mover(self.velocidad * - 1, tamaño_pantalla)
            case "quieto":
                if not self.esta_saltando:
                    if self.ultimo_movimiento == "derecha":
                        self.animar(pantalla, "quieto_derecha")
                    if self.ultimo_movimiento == "izquierda":
                        self.animar(pantalla, "quieto_izquierda")

        self.aplicar_gravedad(pantalla, piso)

    def dañar_con_salto(self, rect_enemigo):
        if self.lados["bottom"].colliderect(rect_enemigo):
            self.hizo_daño = True
            return self.hizo_daño

    def agarrar_vidas(self, rect_vida):
        if self.lados["main"].colliderect(rect_vida):
            self.recupero_vida = True
            return self.recupero_vida

    def sumar_vida(self):
        if self.vida < 3:
            self.vida += 1

    def vidas(self, recibio_daño):
        tiempo_actual = pygame.time.get_ticks() / 1000 # Tiempo actual en segundos

        if self.invencible:
            if tiempo_actual - self.tiempo_inicio_invencible >= self.tiempo_invencible:
                self.invencible = False  # Restablecer la invencibilidad despues del tiempo establecido
        else:
            if recibio_daño:
                self.vida -= 1
                self.invencible = True
                self.tiempo_inicio_invencible = tiempo_actual  # Registrar el inicio de la invencibilidad
                if self.vida <= 0:
                    self.invencible = False
                    return True

    def actualizar_posicion(self, nueva_posicion):
        #Actualizar la posición principal 
        self.lados["main"].x = nueva_posicion[0]
        self.lados["main"].y = nueva_posicion[1]

        self.lados["bottom"] = pygame.Rect(self.lados["main"].left, self.lados["main"].bottom - 8, self.lados["main"].width, 8)
        self.lados["right"] = pygame.Rect(self.lados["main"].right - 10, self.lados["main"].top, 10, self.lados["main"].height)
        self.lados["left"] = pygame.Rect(self.lados["main"].left, self.lados["main"].top, 10, self.lados["main"].height)
        self.lados["top"] = pygame.Rect(self.lados["main"].left, self.lados["main"].top, self.lados["main"].width, 10)