import pygame
from tiles import Tile ,StaticTile ,AnimatedTile 
from coins import Coin
from settings import tile_size ,screen_W,screen_H
from player import Player
from support import import_csv_layout ,import_graphics
from enemy import Enemy
from game_data import levels
from claseVidaRecolectable import Vida




class Level:
    def __init__(self,current_level,surface,create_overworld,change_coins,change_health,update_score):
        #setup general
        self.display_surface = surface
        self.level_mover = 0
        self.backgorund = pygame.image.load("BG.png")

        self.coin_sound = pygame.mixer.Sound('C:/Users/topit/TheRickAdventures/recursos/coin.wav')


        self.change_coins = change_coins
        self.update_score = update_score

        #overworld
        self.create_overworld = create_overworld
        self.current_level = current_level
        level_data = levels[self.current_level]
        self.new_last_level = level_data['unlock']

        #setup player
        player_layout= import_csv_layout(level_data['player'])
        self.player = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.GroupSingle()
        self.player_setup(player_layout,change_health,update_score)

 
        


        #setup terreno
        terrain_layout = import_csv_layout(level_data['terrain'])
        self.terrain_sprites = self.create_tile_group(terrain_layout,'terrain')

        #setup water
        water_layout = import_csv_layout(level_data['water'])
        self.water_sprites = self.create_tile_group(water_layout,'water')

        #setup coins
        coins_layout = import_csv_layout(level_data['coins'])
        self.coins_sprites = self.create_tile_group(coins_layout,'coins')

        #setup enemigos
        enemy_layout = import_csv_layout(level_data['enemigos'])
        self.enemy_sprites = self.create_tile_group(enemy_layout,'enemigos')

        #setup limites
        limite_layout = import_csv_layout(level_data['limites'])
        self.limite_sprite = self.create_tile_group(limite_layout,'limites')

    # def crear_vidas(self):
    #     vida_1 = Vida(800,400)
    #     vida_2 = Vida(500,250)
    #     vida_3 = Vida(100,600)
    #     moving_vida = pygame.sprite.Group()
    #     moving_vida.add(vida_1,vida_2,vida_3)
    #     lista_vidas  = [vida_1,vida_2,vida_3]
    #     return lista_vidas
       
    def create_tile_group(self,layout,type):
        sprite_group = pygame.sprite.Group()


        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                if val != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    
                    if type == 'terrain':
                        terrain_tile_list = import_graphics('C:/Users/topit/TheRickAdventures/graphics/terrain/terrain_tiles.png')
                        tile_surface = terrain_tile_list[int(val)]
                        sprite = StaticTile(tile_size,x,y,tile_surface)
                        
                    if type == 'coins':
                        if val == '0':
                            sprite = Coin(tile_size,x,y,'C:/Users/topit/TheRickAdventures/graphics/coins/gold',5)
                        if val == '1':
                            sprite = Coin(tile_size,x,y,'C:/Users/topit/TheRickAdventures/graphics/coins/silver',1)
                    
                    
                    if type == 'enemigos':
                        sprite = Enemy(tile_size,x,y)
                    
                    if type == 'limites':
                        sprite = Tile(tile_size,x,y)

                    if type == 'water':
                        water_tile_list = import_graphics('C:/Users/topit/TheRickAdventures/graphics/decoration/water/1.png')
                        tile_surface = water_tile_list[int(val)]
                        sprite = StaticTile(tile_size,x,y,tile_surface)
                        


                    sprite_group.add(sprite)


            

        return sprite_group


    def enemy_colision_limite(self):
        for enemy in self.enemy_sprites.sprites():
            if pygame.sprite.spritecollide(enemy,self.limite_sprite,False):
               enemy.change_dir()

    def setup_level(self,layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index,row in enumerate(layout): #enumerate index,info
            for col_index, col in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                   
                if col == "X":
                   tile = Tile((x,y),tile_size)
                   self.tiles.add(tile)
                if col == "P":
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)

    def scroll_x (self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_W /4 and direction_x < 0:
            self.level_mover = 5
            player.speed = 0 
        elif player_x > screen_W - (screen_W /4) and direction_x > 0:
            self.level_mover = -5
            player.speed = 0 
        else:
            self.level_mover = 0
            player.speed = 5 

    def horizontal_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.terrain_sprites.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.terrain_sprites.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.air = False
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
    
    def player_setup(self,layout,change_health,update_score):

        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if val == '0':
                    sprite = Player((x,y),change_health,update_score)
                    self.player.add(sprite)
                   
                if val == '1':
                    start_surface = pygame.image.load('C:/Users/topit/TheRickAdventures/graphics/character/hat.png').convert_alpha()
                    sprite = StaticTile(tile_size,x,y,start_surface)
                    self.goal.add(sprite)

    def check_death(self):
        if self.player.sprite.rect.top > screen_H:
            self.create_overworld(self.current_level,0)
    
    def check_win(self):
        if pygame.sprite.spritecollide(self.player.sprite,self.goal,False):
            self.create_overworld(self.current_level,self.new_last_level)

    def check_coin_collisions(self):
        collided_coins = pygame.sprite.spritecollide(self.player.sprite,self.coins_sprites,True)
        
        if collided_coins:
            self.coin_sound.play()
            for coin in collided_coins:
                self.change_coins(coin.value)
                self.update_score(coin.value)
                
                
    def check_enemy_collisions(self):
        enemy_collisions = pygame.sprite.spritecollide(self.player.sprite,self.enemy_sprites,False)
        
        if enemy_collisions:
            for enemy in enemy_collisions:
                self.player.sprite.get_damage()
                
    def run(self):

        #BG
        self.display_surface.blit(self.backgorund, (0, 0))
        

        #run terreno
        self.terrain_sprites.draw(self.display_surface)
        self.terrain_sprites.update(self.level_mover)

        #run coins
        self.coins_sprites.draw(self.display_surface)
        self.coins_sprites.update(self.level_mover)

        #run enemies
        self.enemy_sprites.draw(self.display_surface)
        self.enemy_sprites.update(self.level_mover)
        self.enemy_colision_limite()

        #limites
        self.limite_sprite.update(self.level_mover)

        #agua
        self.water_sprites.draw(self.display_surface)
        self.water_sprites.update(self.level_mover)
        
        #comienzo y termino del nivel 
        self.goal.update(self.level_mover)
        self.goal.draw(self.display_surface)

       


        # self.tiles.update(self.level_mover)#el argumento pasado sera el culpable de mover el level horizontalmente
        # self.tiles.draw(self.display_surface)
        self.scroll_x()
        

        #check status 
        self.check_death()
        self.check_win()
        self.check_coin_collisions()
        self.check_enemy_collisions()
        #player
        self.player.update(self.display_surface,self.enemy_sprites,self.terrain_sprites)
        self.horizontal_collision()
        self.vertical_collision()
        self.player.draw(self.display_surface)
        
        
        

        