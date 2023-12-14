import pygame
from support import importar_carpeta
from Bullets import Bullet
from tiles import AnimatedTile
from math import sin




class Player(pygame.sprite.Sprite):
    def __init__(self,pos,change_health,update_score):
        super().__init__()
        self.importar_imagenes_player()    
        self.frame_index = 0
        self.speed_animacion = 0.15
        self.image = self.animations["idle"][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)

        
        self.update_score = update_score


        self.jump_sound = pygame.mixer.Sound('C:/Users/topit/TheRickAdventures/recursos/jump.wav')
        self.hit_sound = pygame.mixer.Sound('C:/Users/topit/TheRickAdventures/recursos/hit.wav')


        self.bullet_group = pygame.sprite.Group()
        self.direction_bullet = 1
        self.cooldown = 0
        self.kills = 0

        self.status = "idle"
        self.pov_derecha = True

        #movimiento
        self.speed = 5
        self.direction = pygame.math.Vector2(0,0) #lista ue tiene un valor de x e y 
        self.gravity = 0.8
        self.jump_speed = -18
        self.air = False

        self.change_health = change_health
        self.godmode = False
        self.godmode_duration = 400
        self.damage_time = 0
    
    def importar_imagenes_player(self):
        player_path = 'C:/Users/topit/TheRickAdventures/RICKIMAGES/'
        self.animations = {'idle':[],'caminando':[],'muriendo':[]}
        
        
        for animation in self.animations.keys():
            full_path = player_path + animation            
            self.animations[animation] = importar_carpeta(full_path)
    
    def animate(self):
        animation = self.animations[self.status]


        self.frame_index += self.speed_animacion
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = self.image = animation[int(self.frame_index)]
        if self.pov_derecha:
            self.image = image
            
        else:
            flipped_image = pygame.transform.flip(image,True,False)
            self.image = flipped_image
        
        if self.godmode:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)

    def get_status(self):
        if self.direction.x != 0:
            self.status = "caminando"
        else:
            self.status = "idle"


    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.direction_bullet = 1
            self.pov_derecha = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.direction_bullet = -1
            self.pov_derecha = False
        elif keys[pygame.K_SPACE]:
            self.jump_sound.play()
            self.jump()           
        elif keys[pygame.K_s] and self.cooldown == 0:
                bullet = self.shoot()
                bullet.sound_bullet.play()
                self.bullet_group.add(bullet)
                self.cooldown = 1
        
  
        else:
            self.direction.x = 0
            self.shooting_cd()
            
    
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        if not self.air :
           self.direction.y = self.jump_speed
           self.air = True
           
     
    def shoot(self):
        return Bullet(self.rect.centerx,self.rect.centery,self.direction_bullet)

    def shooting_cd(self):
        if self.cooldown >= 20:
            self.cooldown = 0
        elif self.cooldown > 0:
            self.cooldown += 1

    def get_damage(self):
        if not self.godmode: 
            self.change_health(-25)
            self.godmode = True
            self.damage_time = pygame.time.get_ticks()
    
    def godmode_clock(self):
        if self.godmode:
            current_time = pygame.time.get_ticks()
            if current_time - self.damage_time >= self.godmode_duration:
                self.godmode = False
    
    def wave_value(self):
        self.hit_sound.play()
        value = sin(pygame.time.get_ticks())
        if value >= 0: return 255
        else: return 0
    
    def get_score(self):
        self.score = self.kills * 10 

    def check_bullet_colissions(self,enemies,terrain):
        for bullet in self.bullet_group:
            bullet_collisions = pygame.sprite.spritecollide(bullet,enemies,True)
            for bullet in bullet_collisions:
                self.kills +=1
                self.update_score(self.kills * 10)
            bullet_collisions_terrain =pygame.sprite.spritecollide(bullet,terrain,False)

        # Eliminar la bala si colisiona con enemigos o terreno
            if bullet_collisions or bullet_collisions_terrain:
                bullet.kill()
            
            

    def update(self,screen,enemies,terrain):
        self.get_input()
        self.get_status()
        self.animate()
        self.bullet_group.draw(screen)
        self.bullet_group.update()
        self.godmode_clock()
        self.check_bullet_colissions(enemies,terrain)
        self.wave_value
        
        

    