import pygame
from constantes import *
from settings import *

class Bullet():
    def __init__(self,path,rotation,size,pos_x,pos_y,direction) -> None:
        self.image = pygame.image.load(path).convert_alpha()
        self.image = pygame.transform.scale(self.image,(size)) # 27,15
        self.image_r = pygame.transform.rotate(self.image,-rotation)
        self.image_l = pygame.transform.rotate(self.image,rotation) 
        self.rect = self.image.get_rect(topleft = (pos_x,pos_y))
        self.direction = direction
    
    def move(self):
        if self.direction == DIRECTION_R:
            self.image = self.image_r
            self.rect.x += 15
        if self.direction == DIRECTION_L:
            self.image = self.image_l
            self.rect.x -= 15
        
    def off_screen(self):
        return not (self.rect.x >= 0 and self.rect.x <= SCREEN_WIDTH)

    def show_debug(self,screen):
        pygame.draw.rect(screen, (255,255,255), self.rect)

    def draw(self,screen):
        screen.blit(self.image,self.rect)
