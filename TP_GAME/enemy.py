import pygame
from constantes import *
from auxiliar import Auxiliar

class Enemy(pygame.sprite.Sprite):
    def __init__(self,pos,speed,gravity,frames_animations,size_w_stay,size_h_stay,size_w_run,size_h_run,size_w_dead,size_h_dead,path_stay,path_run,path_dead,scale,quantity_stay,quantity_run,quantity_dead,health) -> None:
        super().__init__()
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles(path_stay,quantity_stay,False,1,scale,size_w_stay,size_h_stay,1)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles(path_stay,quantity_stay,True,1,scale,size_w_stay,size_h_stay,1)
        self.run_r = Auxiliar.getSurfaceFromSeparateFiles(path_run,quantity_run,False,1,scale,size_w_run,size_h_run,1)
        self.run_l = Auxiliar.getSurfaceFromSeparateFiles(path_run,quantity_run,True,1,scale,size_w_run,size_h_run,1)
        self.dead_r = Auxiliar.getSurfaceFromSeparateFiles(path_dead,quantity_dead,False,1,scale,size_w_dead,size_h_dead,1)
        self.dead_l = Auxiliar.getSurfaceFromSeparateFiles(path_dead,quantity_dead,True,1,scale,size_w_dead,size_h_dead,1)
        self.quantity_dead = quantity_dead
        self.animation = self.stay_r
        self.frame = 0
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2(0,0)
        self.gravity = gravity
        self.direction_looking = DIRECTION_R
        self.speed = speed
        self.time_animations = 0
        self.time_movements = 0
        self.frames_animations = frames_animations
        self.hitbox = (self.rect.x + 12,self.rect.y + 12,45,60)
        self.health = health

    def stay(self):
        self.direction.x = 0
        if self.direction_looking == DIRECTION_R:
            self.animation = self.stay_r
        else:
            self.animation = self.stay_l

    def run(self,direction):
        self.direction.x = direction * self.speed
        if direction == DIRECTION_R:
            self.direction_looking = direction
            self.animation = self.run_r
        else:
            self.direction_looking = direction
            self.animation = self.run_l

    def movement_x(self,delta_ms):
        self.time_movements += delta_ms
        self.rect.x += self.direction.x
        if self.time_movements >= 500 and self.time_movements <= 1500:
            self.run(DIRECTION_L)
        elif self.time_movements > 1500 and self.time_movements <= 2500:
            self.stay()
        elif self.time_movements > 2500 and self.time_movements <= 3500:
            self.run(DIRECTION_R)
        elif self.time_movements > 3500 and self.time_movements <= 5500:
            self.stay()
        elif self.time_movements > 5500:
            self.time_movements = 0

    def dead(self):
        if self.health <= 0:
            if self.direction_looking == DIRECTION_R:
                self.animation = self.dead_r
            elif self.direction_looking == DIRECTION_L:
                self.animation = self.dead_l

    def movement_y(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def animations(self,delta_ms):
        self.time_animations += delta_ms
        if self.time_animations >= self.frames_animations:
            self.time_animations = 0
            if self.frame < len(self.animation) - 1:
                self.frame += 1
            else:
                self.frame = 0
            
            self.image = self.animation[self.frame]
            

    def update(self,delta_ms,speed_camera_x):
        self.rect.x += speed_camera_x
        self.animations(delta_ms)
        self.hitbox = (self.rect.x + 12,self.rect.y + 12,45,60)
        
        # self.movement()

