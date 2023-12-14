def colisiones_laterales_plataformas(personaje, plataforma, encima_plataforma):
    colisiona_derecha = False
    colisiona_izquierda = False

    if encima_plataforma == True and (personaje.lados["right"].colliderect(plataforma.lados["left"]) or personaje.lados["left"].colliderect(plataforma.lados["right"])):
        personaje.velocidad = 10
    else:
        if personaje.lados["right"].colliderect(plataforma.lados["left"]):
            colisiona_derecha = True

        elif personaje.lados["left"].colliderect(plataforma.lados["right"]):
            colisiona_izquierda = True

    if not personaje.esta_saltando:
        if colisiona_derecha:
            if personaje.ultimo_movimiento == "izquierda":
                personaje.velocidad = 10
            else:
                personaje.velocidad = 0
        
        elif colisiona_izquierda:
            if personaje.ultimo_movimiento == "derecha":
                personaje.velocidad = 10
            else:
                personaje.velocidad = 0

def manejar_colision_plataformas(personaje, plataformas, piso):
    en_plataforma = False
    for plataforma in plataformas:
        if personaje.lados["bottom"].colliderect(plataforma.lados["top"]) and personaje.desplazamiento_y >= 0:
            personaje.desplazamiento_y = 0
            personaje.esta_saltando = False
            personaje.esta_en_suelo = True
            personaje.lados["main"].bottom = plataforma.lados["top"].top
            en_plataforma = True
        
        colisiones_laterales_plataformas(personaje, plataforma, en_plataforma)

        if not en_plataforma and not personaje.lados["bottom"].colliderect(piso["top"]):
            personaje.esta_saltando = True
            personaje.esta_en_suelo = False
            en_plataforma = False

def colisionar_corazon_con_personaje(lista_vidas,personaje,rectangulo_main):
    for vidas in lista_vidas:
        verificar_colision_corazon = vidas.verificar_colision_vidas(rectangulo_main,personaje.vida)
        if verificar_colision_corazon:
            personaje.vida = vidas.curar(personaje.vida)
            lista_vidas.remove(vidas)