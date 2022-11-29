import pygame
from pygame.locals import *
from constantes import *
from auxiliar import Auxiliar
from gui_widget import Widget

class Button(Widget):
    def __init__(self,master,x,y,w,h,color_background,color_border,on_click,on_click_param,text,font,font_size,font_color) -> None:
        super().__init__(master,x,y,w,h,color_background,color_border)
        pygame.font.init()
        self.on_click = on_click
        self.on_click_param = on_click_param
        self.text = text
        self.font = pygame.font.SysFont(font,font_size)
        self.font_color = font_color


    def render(self):
        image_text = self.font.render(self.text,True,self.font_color,self.color_background)
        self.child_surface = pygame.surface.Surface((self.w,self.h))
        self.child_rect = self.child_surface.get_rect()
        self.child_rect.x = self.x
        self.child_rect.y = self.y
        self.child_rect_collide = pygame.rect.Rect(self.child_rect)

        self.child_rect_collide.x += self.master_form.x
        self.child_rect_collide.y += self.master_form.y
        self.child_surface.fill(self.color_background)
        self.child_surface.blit(image_text,(10,10))


    def update(self,delta_ms,event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (self.child_rect_collide.collidepoint(event.pos)):
                    self.on_click(self.on_click_param)
        self.render()

    