import pygame
from constantes import *
from auxiliar import Auxiliar

class Reward(pygame.sprite.Sprite):
    def __init__(self,pos,size,path):
        super().__init__()
        self.frame = 0
        self.animation = Auxiliar.getSurfaceFromSeparateFiles(path,30,False,1,1,size,size,1)
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect(topleft = pos)
        self.time_animations = 0
        
    def animations(self,delta_ms):
        self.time_animations += delta_ms
        if self.time_animations >= 60:
            self.time_animations = 0
            if self.frame < len(self.animation) - 1:
                    self.frame += 1
            else:
                self.frame = 0
        
        self.image = self.animation[self.frame]

    def update(self,delta_ms,speed_camera_x):
        self.rect.x += speed_camera_x
        self.animations(delta_ms)