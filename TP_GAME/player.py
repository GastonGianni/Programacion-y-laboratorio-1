import pygame
from constantes import *
from auxiliar import Auxiliar

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,speed,gravity,jump_speed,jump_limit,frames_animations):
        super().__init__()
        self.stay_r = Auxiliar.getSurfaceFromSeparateFiles("Resources\player_ninja\png\Idle__00{0}.png",9,False,1,1,50,80,1)
        self.stay_l = Auxiliar.getSurfaceFromSeparateFiles("Resources\player_ninja\png\Idle__00{0}.png",9,True,1,1,50,80,1)
        self.run_r = Auxiliar.getSurfaceFromSeparateFiles("Resources\player_ninja\png\Run__00{0}.png",9,False,1,1,70,80,1)
        self.run_l = Auxiliar.getSurfaceFromSeparateFiles("Resources\player_ninja\png\Run__00{0}.png",9,True,1,1,70,80,1)
        self.jump_r = Auxiliar.getSurfaceFromSeparateFiles("Resources\player_ninja\png\Jump__002.png",1,False,1,1,70,80,1)
        self.jump_l = Auxiliar.getSurfaceFromSeparateFiles("Resources\player_ninja\png\Jump__002.png",1,True,1,1,70,80,1)
        self.fall_r = Auxiliar.getSurfaceFromSeparateFiles("Resources\player_ninja\png\Glide_000.png",1,False,1,1,70,80,1)
        self.fall_l = Auxiliar.getSurfaceFromSeparateFiles("Resources\player_ninja\png\Glide_000.png",1,True,1,1,70,80,1)
        self.attack_r = Auxiliar.getSurfaceFromSeparateFiles("Resources\player_ninja\png\Attack__00{0}.png",9,False,1,1,100,90,1)
        self.attack_l = Auxiliar.getSurfaceFromSeparateFiles("Resources\player_ninja\png\Attack__00{0}.png",9,True,1,1,100,90,1)
        self.hurt_r = Auxiliar.getSurfaceFromSeparateFiles("Resources\player_ninja\png\Dead__000.png",1,False,1,1,70,80,1)
        self.hurt_l = Auxiliar.getSurfaceFromSeparateFiles("Resources\player_ninja\png\Dead__000.png",1,True,1,1,70,80,1)
        self.dead_r = Auxiliar.getSurfaceFromSeparateFiles("Resources\player_ninja\png\Dead__00{}.png",9,False,1,1,80,90,1)
        self.dead_l = Auxiliar.getSurfaceFromSeparateFiles("Resources\player_ninja\png\Dead__00{}.png",9,True,1,1,80,90,1)
        self.animation = self.stay_r
        self.frame = 0
        self.score = 0
        self.lives = 5
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2(0,0)
        self.direction_looking = DIRECTION_R
        self.speed = speed
        self.gravity = gravity
        self.jump_speed = jump_speed
        self.jump_limit = jump_limit
        self.position_start_jump = 0
        self.time_animations = 0
        self.frames_animations = frames_animations
        self.is_grounding = False
        self.is_attacking = False
        self.is_contact_enemy = False
        

    def get_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.run(DIRECTION_R)
        elif keys[pygame.K_LEFT]:
            self.run(DIRECTION_L)
        else:
            self.stay()
        if keys[pygame.K_UP]:
            self.jump()
        if keys[pygame.K_SPACE]:
            self.mele_attack()
        
    def run(self,direction):
        if not self.is_attacking and not self.animation == self.attack_r and not self.animation == self.attack_l:
            self.direction.x = direction
            if direction == DIRECTION_R:
                self.direction_looking = direction
                self.animation = self.run_r
            else:
                self.direction_looking = direction
                self.animation = self.run_l
    
    def stay(self):
        self.is_attacking = False
        self.direction.x = 0
        if self.direction_looking == DIRECTION_R:
            self.animation = self.stay_r
        else:
            self.animation = self.stay_l

    def jump(self):
        if self.is_grounding:
            self.direction.y = self.jump_speed
        if self.direction.y < 0:
            if self.direction_looking == DIRECTION_R:
                self.animation = self.jump_r
            else:
                self.animation = self.jump_l
    
    def mele_attack(self):
        self.is_attacking = True
        if self.is_attacking:
            if self.direction_looking == DIRECTION_R:
                self.animation = self.attack_r
            else:
                self.animation = self.attack_l

    def movement_x(self):
        self.rect.x += self.direction.x * self.speed

    def movement_y(self):
        if abs(self.position_start_jump - self.rect.bottom) > self.jump_limit:
            self.is_grounding = False
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def hurt(self,direction):
        if self.is_contact_enemy and self.lives > 0:
            if direction == DIRECTION_R:
                self.animation = self.hurt_r
                self.lives -= 1
            if direction == DIRECTION_L:
                self.lives -= 1
                self.animation = self.hurt_l
            
            self.is_contact_enemy = False


    def animations(self,delta_ms):
        self.time_animations += delta_ms
        if not self.is_grounding and self.direction.y > 0:
            if self.direction_looking == DIRECTION_R:
                self.animation = self.fall_r
            else:
                self.animation = self.fall_l
        if self.time_animations >= self.frames_animations:
            self.time_animations = 0
            if self.frame < len(self.animation) - 1:
                self.frame += 1
            else:
                self.frame = 0

            self.image = self.animation[self.frame]


    def update(self,delta_ms,game_over):
        if game_over == 0:
            self.get_keys()
            self.animations(delta_ms)
        elif game_over == -1 and self.frame < 8:
            self.animation = self.dead_r
            self.animations(delta_ms)
            self.direction.x = 0
        else:
            return    



