import pygame

class Vida(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()

        self.sprites = []
        for i in range(11):
            self.sprites.append(pygame.image.load(f'C:/Users/topit/TheRickAdventures/recursos/vida/1/{i+1}.png'))
        self.sprite_Actual = 0
        self.image = self.sprites[self.sprite_Actual]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x,pos_y]
        self.hitbox = pygame.Rect(525,60,40,40)
        self.recolectada =False
        self.flip = True
        self.pickup_sound = pygame.mixer.Sound('C:/Users/topit/TheRickAdventures/recursos/eat.mp3')

    def colision_vida(self,player):
        if pygame.sprite.spritecollide(self, player, False) and not self.recolectada:
            self.kill()
            self.pickup_sound.play()
            player.current_health += 80
            if player.current_health == player.max_health:
                player.current_health.vida = player.max_health
            self.recolectada = True 

    def update(self,player):
        self.sprite_Actual += 0.1
        if self.sprite_Actual >= len(self.sprites):
            self.sprite_Actual = 0
        self.image = self.sprites[int(self.sprite_Actual)]
        self.colision_vida(player)

        
    
    
