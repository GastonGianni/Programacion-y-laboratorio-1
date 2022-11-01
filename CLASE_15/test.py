
import pygame
import colores
import dona
import personaje
import random

#VENTANA
ANCHO_VENTANA = 800
ALTO_VENTANA = 800

pygame.init()
ventana_ppal = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.display.set_caption("PYGAME HOMERO COME DONAS")

# TIMER
timer = pygame.USEREVENT + 0
pygame.time.set_timer(timer,10)

#PLAYER
player = personaje.crear(ANCHO_VENTANA/2, ALTO_VENTANA - 200, 200,200)
lista_donas = dona.crear_lista_donas(10)


# CREAR UN TEXTO
fuente = pygame.font.SysFont("Tahoma",30)
texto = fuente.render("Puntos",True, colores.ROJO)

#WHILE JUEGO
flag_run = True
while flag_run:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_run = False

        if evento.type == pygame.USEREVENT:
            if evento.type == timer:
                dona.update(lista_donas)

    lista_teclas = pygame.key.get_pressed()

    if lista_teclas[pygame.K_LEFT]:
        personaje.update(player,-5)
    if lista_teclas[pygame.K_RIGHT]:
        personaje.update(player,5)

    ventana_ppal.fill(colores.NEGRO)
    personaje.actualizar_pantalla(player,ventana_ppal)
    dona.actualizar_pantalla(lista_donas,player,ventana_ppal)



    pygame.display.flip()

pygame.quit()