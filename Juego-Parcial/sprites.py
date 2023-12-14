import pygame

def reescalar_imagenes(lista_imagenes, tamaño):
    for i in range(len(lista_imagenes)):
        lista_imagenes[i] = pygame.transform.scale(lista_imagenes[i], tamaño)

def girar_imagenes(lista, flip_x, flip_y):
    lista_girada = []
    for imagen in lista:
        lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))
    return lista_girada

def obtener_rectangulos(principal)->dict:
    diccionario = {}

    diccionario["main"] = principal
    diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom -10, principal.width, 10)
    diccionario["right"] = pygame.Rect(principal.right -10, principal.top, 10, principal.height)
    diccionario["left"] = pygame.Rect(principal.left, principal.top, 10, principal.height)
    diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 10)

    return diccionario

#PERSONAJE PRINCIPAL:
personaje_quieto_derecho = [pygame.image.load("2-Parcial/Juego-Parcial/Sprites/Quieto/Quieto.png")]

personaje_quieto_izquierda =  girar_imagenes(personaje_quieto_derecho, True, False)

personaje_camina = [pygame.image.load("2-Parcial/Juego-Parcial/Sprites/Caminar/caminar-m (2).png"), 
                    pygame.image.load("2-Parcial/Juego-Parcial/Sprites/Caminar/caminar-m (3).png"), 
                    pygame.image.load("2-Parcial/Juego-Parcial/Sprites/Caminar/caminar-m (4).png"), 
                    pygame.image.load("2-Parcial/Juego-Parcial/Sprites/Caminar/caminar-m (5).png")
                    ]

personaje_camina_izquierda = girar_imagenes(personaje_camina, True, False)

personaje_salta = [pygame.image.load("2-Parcial/Juego-Parcial/Sprites/Saltar/Salta (1).png")]

personaje_salta_izquierda = girar_imagenes(personaje_salta, True, False)

#ENEMIGO BASICO:
enemigo_camina_izquierda = [pygame.image.load("2-Parcial/Juego-Parcial/Sprites/Enemigos/Camina(1).png"), 
                            pygame.image.load("2-Parcial/Juego-Parcial/Sprites/Enemigos/Camina(2).png")]

enemigo_camina = girar_imagenes(enemigo_camina_izquierda, True, False)

enemigo_quieto = [pygame.image.load("2-Parcial/Juego-Parcial/Sprites/Enemigos/Quieto.png")]

enemigo_quieto_izquierda = girar_imagenes(enemigo_quieto, True, False)

#Piso
piso_1 = pygame.image.load("2-Parcial/Juego-Parcial/Sprites/Plataformas/piso largo.png")
piso_2 = pygame.image.load("2-Parcial/Juego-Parcial/Sprites/Plataformas/piso largo.png")
piso_3 = pygame.image.load("2-Parcial/Juego-Parcial/Sprites/Plataformas/piso largo.png")
lista_piso = [piso_1, piso_2, piso_3]



