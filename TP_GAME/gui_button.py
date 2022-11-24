import pygame
from constantes import *
from auxiliar import Auxiliar

class Button:
    def __init__(self,x,y,image) -> None:
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self,screen):
        screen.blit(self.image, self.rect)