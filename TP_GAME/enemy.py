import pygame
from constantes import *
from auxiliar import Auxiliar

class Enemy(pygame.sprite.Sprite):
    def __init__(self,pos,speed,gravity,frames_animations) -> None:
        super().__init__()
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("Resources\enemy_1\png\Idle ({0}).png",9,False,1,1,75,100,1)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("Resources\enemy_1\png\Idle ({0}).png",9,True,1,1,75,100,1)
        self.run_r = Auxiliar.getSurfaceFromSeparateFiles("Resources\enemy_1\png\Run ({0}).png",7,False,1,1,80,100,1)
        self.run_l = Auxiliar.getSurfaceFromSeparateFiles("Resources\enemy_1\png\Run ({0}).png",7,True,1,1,80,100,1)
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
        elif self.time_movements > 1500 and self.time_movements <= 4500:
            self.stay()
        elif self.time_movements > 4500 and self.time_movements <= 5500:
            self.run(DIRECTION_R)
        elif self.time_movements > 5500 and self.time_movements <= 8500:
            self.stay()
        elif self.time_movements > 8500:
            self.time_movements = 0


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
        
        # self.movement()

