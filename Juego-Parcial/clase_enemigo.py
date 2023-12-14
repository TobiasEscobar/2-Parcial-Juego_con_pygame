from sprites import reescalar_imagenes, obtener_rectangulos

class Enemigo():
    def __init__(self, tamaño, animaciones, posicion_inicial, velocidad, vida, que_lado):
        #TAMAÑO ENEMIGO
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        #ANIMACIONES
        self.contador_pasos = 0
        self.que_hace = "quieto"
        self.direccion = "derecha"
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
        self.borde_izquierdo = False
        self.borde_derecho = False
        self.lado_I = que_lado[0]
        self.lado_R = que_lado[1]
        #ATRIBUTOS
        self.vida = vida
        self.colisiona = False
        self.hizo_daño = False

    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave], (self.ancho, self.alto))

    def animar_enemigo(self, pantalla, que_animacion):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)

        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        
        pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
        self.contador_pasos += 1

    def mover(self, velocidad):
        lado_izquierdo = self.lado_I
        lado_derecho = self.lado_R

        #Aplica la velocidad a todos los lados del rectangulo
        for lado in self.lados:
            self.lados[lado].x += velocidad

        if self.direccion == "derecha":
            if self.lados["main"].right >= lado_derecho:
                self.borde_derecho = True
            if self.borde_derecho:
                self.borde_izquierdo = False

        elif self.direccion == "izquierda":
            if self.lados["main"].left <= lado_izquierdo:
                self.borde_izquierdo = True
            if self.borde_izquierdo:
                self.borde_derecho = False

    def update(self, pantalla, piso, tamaño_pantalla):
        match self.direccion:
            case "derecha":
                self.animar_enemigo(pantalla, "camina_derecha")
                self.mover(self.velocidad)
            case "izquierda":
                self.animar_enemigo(pantalla, "camina_izquierda")
                self.mover(self.velocidad *-1)

        if self.borde_derecho:
            self.direccion = "izquierda"
        if self.borde_izquierdo:
            self.direccion = "derecha"

    def daño_a_personaje(self, rect_personaje):
        if self.lados["right"].colliderect(rect_personaje) or self.lados["left"].colliderect(rect_personaje):
            self.colisiona = True
            return True