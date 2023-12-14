import pygame
from tiles import AnimatedTile

class Boss(AnimatedTile):
    def __init__(self, size, x, y):
        super().__init__(size, x, y, 'C:/Users/topit/TheRickAdventures/enemy/runBoss')
        self.rect.y += size - self.image.get_size()[1]
        self.speed = 2

    
    def move(self):
        self.rect.x += self.speed
    
    def change_pov(self):
        if self.speed > 0:
           self.image = pygame.transform.flip(self.image,True,False)
        
    def change_dir(self):
        
        self.speed *= -1
    
    def update(self,level_mover):
        self.rect.x += level_mover
        self.animate()
        self.move()
        self.change_pov()
        