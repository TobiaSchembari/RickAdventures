import pygame
from support import importar_carpeta

class Tile(pygame.sprite.Sprite):
    def __init__(self,size,x,y):
        super().__init__()
        self.image = pygame.Surface((size,size))
        
        self.rect = self.image.get_rect(topleft = (x,y))

    def update(self,x_change):
        self.rect.x += x_change


class StaticTile(Tile):
    def __init__(self,size,x,y,surface):
         super().__init__(size,x,y)
         self.image = surface


class AnimatedTile(Tile):
    def __init__(self, size, x, y,path):
        super().__init__(size, x, y)
        self.frames = importar_carpeta(path)
        self.frame_index = 0
        self.image = self.frames[self.frame_index]

    def animate(self):
        self.frame_index += 0.15
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]
    
    def update(self,level_mover): #sobreescribiendo update
        self.animate()
        self.rect.x += level_mover