import pygame 
pygame.init()
class UI:
    def __init__(self,surface):


        #setup
        self.display_surface = surface

        #health
        self.health_bar = pygame.image.load('C:/Users/topit/TheRickAdventures/graphics/UI/health_bar.png')
        self.health_bar_topleft = (54,39)
        self.bar_max_width = 152
        self.bar_height = 4

        #coins
        self.coin = pygame.image.load('C:/Users/topit/TheRickAdventures/graphics/UI/coinG.png')
        self.coin_rect = self.coin.get_rect(topleft = (50,61))
        self.font = pygame.font.Font('C:/Users/topit/TheRickAdventures/graphics/UI/Gamer.ttf',40)

    def show_health(self,current,full):
        self.display_surface.blit(self.health_bar,(20,10))
        current_health_ratio = current / full
        current_bar_width = self.bar_max_width * current_health_ratio
        health_bar_rect = pygame.Rect((self.health_bar_topleft),(current_bar_width,self.bar_height))
        pygame.draw.rect(self.display_surface,'#dc4949',health_bar_rect)

    def show_coins(self,amount):
        self.display_surface.blit(self.coin,self.coin_rect)
        coin_amount_surf = self.font.render(str(amount),False,"#E5D29F")
        coin_amount_rect = coin_amount_surf.get_rect(midleft =(self.coin_rect.right +4,self.coin_rect.centery))
        self.display_surface.blit(coin_amount_surf,coin_amount_rect)
    
    def show_score(self,amount):
        score_string = self.font.render('SCORE',False,"#2F9331")
        self.display_surface.blit(score_string,(50,91))
        score_amount_surf = self.font.render(str(amount),False,"#E5D29F")
        self.display_surface.blit(score_amount_surf,(130,91))
