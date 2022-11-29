import pygame
from pygame.locals import *
from constantes import *
from auxiliar import Auxiliar

class Widget:
    def __init__(self,master_form,x,y,w,h,color_background,color_border) -> None:
        self.master_form = master_form
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color_background = color_background
        self.color_border = color_border

    def render(self):
        pass

    def update(self):
        pass

    def draw(self):
        self.master_form.surface.blit(self.child_surface,self.child_rect)