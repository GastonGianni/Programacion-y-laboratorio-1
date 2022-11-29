import pygame
from pygame.locals import *
from gui_widget import Widget
from gui_button import Button
from constantes import *
from settings import *

class Form():
    forms_dict = {}
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active) -> None:
        self.forms_dict[name] = self
        self.master_surface = master_surface
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color_background = color_background
        self.color_border = color_border


        self.child_surface = pygame.surface.Surface((w,h))
        self.child_rect = self.child_surface.get_rect()
        self.child_rect.x = x
        self.child_rect.y = y
        self.active = active
        self.x = x
        self.y = y
        
        if(self.color_background != None):
            self.child_surface.fill(self.color_background)


    def render(self):
        pass


    def update(self,delta_ms,event_list):
        pass


class FormMenu(Form):
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,active)

        self.button_1 = Button(master = self,x=SCREEN_WIDTH/2,y= SCREEN_HEIGHT/2,w=200,h=200,color_background=(255,255,0),color_border=(255,255,255),on_click=self.on_click_button_1 ,on_click_param="a",text="Boton",font="Verdana",font_size=30,font_color=(0,0,0))
        self.button_2 = Button(master = self,x=SCREEN_WIDTH/3,y= SCREEN_HEIGHT/3,w=200,h=200,color_background=(255,255,0),color_border=(255,255,255),on_click=self.on_click_button_1 ,on_click_param="a",text="Boton",font="Verdana",font_size=30,font_color=(0,0,0))
        self.button_list = [self.button_1,self.button_2]

    def on_click_button_1(parametro):
        print("CLICK",parametro)

    def update(self,event_list, delta_ms):
        for button in self.button_list:
            button.update(event_list,delta_ms)

    def draw(self):
        for button in self.button_list:
            button.draw()