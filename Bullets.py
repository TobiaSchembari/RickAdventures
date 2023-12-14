import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,direccion):
        pygame.sprite.Sprite.__init__(self)

        self.velocidad = 12
        

        self.sound_bullet = pygame.mixer.Sound('C:/Users/topit/TheRickAdventures/graphics/character/space_shot_piu.mp3')
        self.sound_bullet.set_volume(0.1)

        self.image = pygame.image.load('C:/Users/topit/TheRickAdventures/graphics/character/bala.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

        self.direccion = direccion
    
    def update(self):
        self.rect.x += (self.direccion * self.velocidad)
        if self.rect.right < 0 or self.rect.left > 1200:
            self.kill()


