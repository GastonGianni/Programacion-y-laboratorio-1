import pygame

from tiles import Tile
from settings import *
from player import Player
from enemy import Enemy
from rewards import Reward
from tramps import Tramp
from gui_button import Button
from bullet import Bullet

class Level:
    def __init__(self,level_data,surface) -> None:
        self.surface = surface
        self.setup_level(level_data)
        self.map_move_x = 0
        self.background = pygame.image.load("Resources\dark_bg\png\BG.png")
        self.background = pygame.transform.scale(self.background,(SCREEN_WIDTH,SCREEN_HEIGHT))
        self.game_over = 0


    def setup_level(self,layout):
        self.tiles = pygame.sprite.Group()
        self.rewards = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.enemies = pygame.sprite.Group()
        self.tramps = pygame.sprite.Group()
        
        
        for index_row, row in enumerate(layout):
            for index_column,cell in enumerate(row):
                x = index_column * tile_size
                y = index_row * tile_size
                if cell == 'X':
                    tile = Tile((x,y),tile_size,path=r"Resources\freescifiplatform\png\Tiles\Tile (5).png")
                    self.tiles.add(tile)
                if cell == 'T':
                    tramp = Tramp((x,y),tile_size,path=r"Resources\freescifiplatform\png\Tiles\Spike.png")
                    self.tramps.add(tramp)
                if cell == 'B':
                    sprite_rewards = Reward((x,y),50,path="Resources\coins\Free-Game-Coins-Sprite\PNG\Gold\Gold_{}.png")
                    self.rewards.add(sprite_rewards)
                if cell == 'P':
                    sprite_player = Player(pos=(x,y),speed = 8, gravity = 0.8,jump_speed= -16,jump_limit= 60, frames_animations=45,cooldown_shoot=12)
                    self.player.add(sprite_player)
                if cell == 'C':
                    sprite_enemy_one = Enemy(pos=((x,y)),speed = 7,gravity= 0.8,frames_animations= 60,size_w_stay=80,size_h_stay=100,size_w_run=75,size_h_run=100,size_w_dead=90,size_h_dead=100,path_stay=r"Resources\enemy_1\png\Idle ({0}).png",path_run=r"Resources\enemy_1\png\Run ({0}).png",path_dead=r"Resources\enemy_1\png\Dead ({0}).png",scale=1,quantity_stay=9,quantity_run=7,quantity_dead= 9,health=100)
                    self.enemies.add(sprite_enemy_one)
                if cell == 'Z':
                    sprite_enemy_two = Enemy(pos=((x,y)),speed = 3,gravity= 0.8,frames_animations= 60,size_w_stay=80,size_h_stay=100,size_w_run=75,size_h_run=100,size_w_dead=90,size_h_dead=110,path_stay=r"Resources\zombiefiles\png\male\Idle ({0}).png",path_run=r"Resources\zombiefiles\png\male\Walk ({0}).png",path_dead=r"Resources\zombiefiles\png\male\Dead ({0}).png",scale=1,quantity_stay=14,quantity_run=9,quantity_dead= 11,health=50)
                    self.enemies.add(sprite_enemy_two)
        

    def move_screen_x(self):
        player = self.player.sprite
        player_center = player.rect.centerx
        direction = player.direction.x

        if player_center < SCREEN_WIDTH / 4 and direction < 0: # 1200 / 4 = 300
            self.map_move_x = 8
            player.speed = 0
        elif player_center > SCREEN_WIDTH - (SCREEN_WIDTH/4) and direction > 0: # 1200 - 300 = 1100
            self.map_move_x = -8
            player.speed = 0
        else:
            self.map_move_x = 0
            player.speed = 5

    def collisions_x_player(self,game_over):
        '''
            - Aplicar movimiento horizontal
            - Chequear colisiones horizontales
        '''
        if game_over == 0:
            player = self.player.sprite
            player.movement_x() # Se genera movimiento horizontal
            for sprite_tile in self.tiles.sprites():  # Recorre los sprites de los tiles
                if sprite_tile.rect.colliderect(player.rect): # Chequea si hubo colisiones entre el rectangulo del player con el de cada tile
                    if player.direction.x < 0: # si es menor a 0, el jugador se mueve hacia la izquierda
                        player.rect.left = sprite_tile.rect.right # se asigna como posicion la izquierda del rect del player, como la derecha del rect del tile
                    elif player.direction.x > 0: # si es mayor a 0, el jugador se mueve hacia la derecha
                        player.rect.right = sprite_tile.rect.left  # se asigna como posicion la derecha del rect del player, como la izquierda del rect del tile

    def collisions_y_player(self,game_over):
        '''
            - Aplicar movimiento vertical
            - Chequear colisiones verticales
        '''
        if game_over == 0:
            player = self.player.sprite
            player.movement_y() # Se aplica la gravedad
            for sprite_tile in self.tiles.sprites():  
                if sprite_tile.rect.colliderect(player.rect): 
                    if player.direction.y > 0: 
                        player.rect.bottom = sprite_tile.rect.top
                        player.direction.y = 0
                        player.is_grounding = True
                        player.position_start_jump = player.rect.bottom
                    elif player.direction.y < 0:
                        player.rect.top = sprite_tile.rect.bottom  
                        player.direction.y = 0

    def collisions_x_enemy(self,delta_ms):
        for enemy in self.enemies.sprites():
            enemy.movement_x(delta_ms)
            for sprite_tile in self.tiles.sprites(): 
                if sprite_tile.rect.colliderect(enemy.rect):
                    if enemy.direction.x < 0 or enemy.direction_looking == DIRECTION_L:
                        enemy.rect.left = sprite_tile.rect.right 
                    elif enemy.direction.x > 0 or enemy.direction_looking == DIRECTION_R: 
                        enemy.rect.right = sprite_tile.rect.left
                    
    def collisions_y_enemy(self):
        for enemy in self.enemies.sprites():
            enemy.movement_y()
            for sprite_tile in self.tiles.sprites():  
                if sprite_tile.rect.colliderect(enemy.rect): 
                    if enemy.direction.y > 0: 
                        enemy.rect.bottom = sprite_tile.rect.top
                        enemy.direction.y = 0
                    elif enemy.direction.y < 0:
                        enemy.rect.top = sprite_tile.rect.bottom  
                        enemy.direction.y = 0             
    
    def collisions_player_coins(self):
        player = self.player.sprite
        for sprite_rewards in self.rewards.sprites():
            if sprite_rewards.rect.colliderect(player.rect):
                sprite_rewards.kill()
                player.score += 100

    def collisions_player_enemy(self):
        player = self.player.sprite
        for enemy in self.enemies.sprites():
            if enemy.rect.colliderect(player.rect):
                player.health -= 5
                print("Contacto con enemigo")

    def collisions_player_tramps(self):
        player = self.player.sprite
        for tramp_rect in self.tramps.sprites():
            if tramp_rect.collition_rect.colliderect(player.rect):
                player.rect.bottom -= 30
                player.health -= 4
                print("Contacto con trampas")

    def draw_lives(self):
        player = self.player.sprite
        pygame.draw.rect(self.surface,(255,0,0), (SCREEN_WIDTH - 450, 40, 400, 15))
        if player.health >= 0:
            pygame.draw.rect(self.surface,(0,255,0), (SCREEN_WIDTH - 450, 40, player.health, 15))

        for enemy in self.enemies.sprites():
            pygame.draw.rect(self.surface,(255,0,0), (enemy.rect.x + 15,enemy.rect.y, enemy.health, 10))
            if enemy.health >= 0:
                pygame.draw.rect(self.surface,(0,255,0), (enemy.rect.x + 15,enemy.rect.y, enemy.health, 10))

    def collision_bullets_enemy(self):
        player = self.player.sprite
        for kunai in player.kunais_list:
            for enemy in self.enemies.sprites():
                if kunai.rect.colliderect(enemy.hitbox):
                    player.kunais_list.remove(kunai)
                    enemy.health -= 5
                    print("Le dio al enemigo")

    def player_death(self):
        player = self.player.sprite

        if player.health <= 0:
            self.game_over = -1

    def enemy_death(self):
        for enemy in self.enemies.sprites():
            if enemy.health <= 0:
                enemy.dead()
                if enemy.frame == enemy.quantity_dead - 1:
                    enemy.kill()

    def run(self,delta_ms):
        # BACKGROUND
        self.surface.blit(self.background,self.background.get_rect())
        self.draw_lives()
        

        # PLATAFORMAS
        self.tiles.update(self.map_move_x)
        self.tiles.draw(self.surface)
        self.tramps.update(self.map_move_x)
        self.tramps.draw(self.surface)

        # MOVIMIENTO ESCENARIO
        self.move_screen_x()

        # MONEDAS
        self.rewards.update(delta_ms,self.map_move_x)
        self.rewards.draw(self.surface)

        # ENEMIGO
        self.enemies.update(delta_ms,self.map_move_x)
        self.collisions_y_enemy()
        self.collisions_x_enemy(delta_ms)
        self.enemy_death()
        self.enemies.draw(self.surface)

        # JUGADOR
        self.player.update(delta_ms,self.game_over)
        self.collisions_x_player(self.game_over)
        self.collisions_y_player(self.game_over)
        self.collisions_player_coins()
        self.collisions_player_enemy()
        self.collisions_player_tramps()
        self.collision_bullets_enemy()
        self.player_death()
        self.player.draw(self.surface)

        # KUNAIS
        for kunai in self.player.sprite.kunais_list:
            kunai.draw(self.surface)

        
        if DEBUG:
            player = self.player.sprite
            pygame.draw.rect(self.surface, (255,0,0), player.hitbox, 1)
            for enemy in self.enemies.sprites():
                pygame.draw.rect(self.surface,(255,255,0),enemy.hitbox,1)

            for trampa in self.tramps.sprites():
                trampa.show_debug(self.surface)

