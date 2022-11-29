import pygame

class Tramp(pygame.sprite.Sprite):
    def __init__(self,pos,size,path):
        super().__init__()
        self.image = pygame.image.load(path).convert_alpha()
        self.image = pygame.transform.scale(self.image,(size,size))
        self.rect = self.image.get_rect(topleft = pos)
        self.collition_rect = pygame.Rect(self.rect.x, self.rect.y + (self.rect.h / 2),self.rect.width,40)

    def show_debug(self,screen):
        pygame.draw.rect(screen, (255,255,255), self.collition_rect)

    def update(self,speed_camera_x):
        self.collition_rect = pygame.Rect(self.rect.x, self.rect.y + (self.rect.h / 2),self.rect.width,40)
        self.rect.x += speed_camera_x