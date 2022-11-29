import pygame, sys
from constantes import *
from settings import *
from level import Level
from gui_form import Form, FormMenu

pygame.init()

# VENTANA
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# TIMER
clock = pygame.time.Clock()

# NIVEL
level_1 = Level(level_map,screen)

# form_menu = FormMenu(name="form_menu_A",master_surface = screen, x=100,y=100,w=400,h=400,color_background=(255,255,255),color_border=(255,255,255),active=True)

while True:
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    

    delta_ms = clock.tick(FPS)

    # if form_menu.active:
    #     form_menu.update(delta_ms,event_list)
    #     form_menu.draw()
    level_1.run(delta_ms)
    pygame.display.update() # REEMPLAZA .FLIP()
