import sqlite3
import pygame
from constantes import *

def crear_tabla():
    try:
        with sqlite3.connect("2-Parcial/Juego-Parcial/bd_ranking.db") as conexion:
            cursor = conexion.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS ranking (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nombre TEXT,
                                puntaje INTEGER
                            )''')
    except sqlite3.Error as error:
        print("Error al crear la tabla:", error)

def mostrar_tabla(pantalla):
    with sqlite3.connect("2-Parcial/Juego-Parcial/bd_ranking.db") as conexion:
        cursor = conexion.execute("SELECT * FROM ranking order by puntaje DESC LIMIT 5")
        registros = cursor.fetchall()

    fuente = pygame.font.SysFont("Malgun Gothic", 25)
    columnas = [440, 650, 920]  
    header = ["ID", "Nombre", "Puntaje"]

    # Renderizar la cabecera de las columnas
    for i, titulo in enumerate(header):
        encabezado = fuente.render(titulo, True, COLOR_NEGRO)
        pantalla.blit(encabezado, (columnas[i], 300))

    filas = 545  # Posición inicial en el eje Y para los datos
    for registro in registros:
        id_str = str(registro[0]).ljust(25)
        nombre_str = registro[1].ljust(25)
        puntaje_str = str(registro[2]).ljust(25)

        # Renderizar cada campo en su respectiva columna
        id_texto = fuente.render(id_str, True, COLOR_NEGRO)
        nombre_texto= fuente.render(nombre_str, True, COLOR_NEGRO)
        puntaje_texto = fuente.render(puntaje_str, True, COLOR_NEGRO)

        pantalla.blit(id_texto, (columnas[0], filas))
        pantalla.blit(nombre_texto, (columnas[1], filas))
        pantalla.blit(puntaje_texto, (columnas[2], filas))

        filas += 35  # Ajusta este valor para la separación entre líneas

    pygame.display.flip()  # Actualiza la pantalla


def agregar_nombre(nombre):
    try:
        with sqlite3.connect("2-Parcial/Juego-Parcial/bd_ranking.db") as conexion:
            cursor = conexion.cursor()
            # Verificar si el nombre ya está en la base de datos
            cursor.execute("SELECT nombre FROM ranking WHERE nombre = ?", (nombre,))
            resultado = cursor.fetchone()  # Obtener el primer resultado

            # Si no se encuentra el nombre, lo insertamos
            if resultado is None:
                conexion.execute("INSERT INTO ranking (nombre) VALUES (?)", (nombre,))
                conexion.commit()
                print("Nombre agregado correctamente")
            else:
                print("El nombre ya existe en la base de datos")
    except sqlite3.Error as e:
        print("Error al agregar el nombre:", e)

def actualizar_puntaje(nombre, nuevo_puntaje):
    try:
        with sqlite3.connect("2-Parcial/Juego-Parcial/bd_ranking.db") as conexion:
            cursor = conexion.cursor()
            sentencia = "UPDATE ranking SET puntaje = ? WHERE nombre = ?"
            cursor.execute(sentencia, (nuevo_puntaje, nombre))
            conexion.commit()
            print("Se actualizó el puntaje para", nombre)
    except sqlite3.Error as error:
        print("Error al actualizar el puntaje:", error)


