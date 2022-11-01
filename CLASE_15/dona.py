from cmath import rect
import pygame
import colores

def crear(x,y,ancho,alto):
    #Leer una img
    dona_img = pygame.image.load(r"CLASE_15\CLASE_PYGAME_INTRO\00.png")
    dona_img = pygame.transform.scale(dona_img,(ancho,alto))
    rect_dona = dona_img.get_rect()
    rect_dona.x = x
    rect_dona.y = y
    dict_dona = {}
    dict_dona["surface"] = dona_img
    dict_dona["rect"] = rect_dona
    dict_dona["visible"] = True
    return dict_dona

def update(lista_donas):
    for dona in lista_donas:
        rect_dona = dona["rect"]
        rect_dona.y = rect_dona.y + 1


def actualizar_pantalla(lista_donas,personaje, ventana_ppal):
    for dona in lista_donas:
        if dona["visible"] and personaje["rect"].colliderect(dona["rect"]):
            dona["visible"] = False
            personaje["score"] = personaje["score"] + 100
        if dona["visible"]:   
            pygame.draw.rect(ventana_ppal,colores.AZUL,dona["rect"])
            ventana_ppal.blit(dona["surface"],dona["rect"])

    font = pygame.font.SysFont("Arial Narrow", 50)
    text = font.render("SCORE: {0}".format(personaje["score"]), True, (255,0,0))
    ventana_ppal.blit(text,(0,0))
def crear_lista_donas(cantidad):
    lista_donas = []
    for i in range(cantidad):
        lista_donas.append(crear(0+(i*80),0,60,60))
    return lista_donas
    