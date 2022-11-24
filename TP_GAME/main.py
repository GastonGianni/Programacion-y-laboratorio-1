import pygame, sys
from constantes import *
from settings import *
from level import Level

pygame.init()

# VENTANA
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# TIMER
clock = pygame.time.Clock()

# NIVEL
level_1 = Level(level_map,screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    

    delta_ms = clock.tick(FPS)
    level_1.run(delta_ms)
    
    pygame.display.update() # REEMPLAZA .FLIP()
