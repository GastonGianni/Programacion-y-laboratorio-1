import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,size,path):
        super().__init__()
        self.image = pygame.image.load(path).convert()
        self.image = pygame.transform.scale(self.image,(size,size))
        self.rect = self.image.get_rect(topleft = pos)

    def update(self,speed_camera_x):
        self.rect.x += speed_camera_x
