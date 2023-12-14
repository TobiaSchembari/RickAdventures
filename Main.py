import pygame, sys
from settings import * 
from Juego import Game
from forms import Forms


#setup game
screen = pygame.display.set_mode((screen_W,screen_H))

clock = pygame.time.Clock()

titulo = pygame.display.set_caption("Wubba Lubba DUB DUB")

icono  = pygame.image.load('C:/Users/topit/TheRickAdventures/recursos/icono.jpg')
pygame.display.set_icon(icono)


form_principal = Forms(screen,0,0,1500,700,"Black","Dark green",5,True)

game = Game(screen)





pygame.init()
 


while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill("Black")

    game.run()
    form_principal.update(events)
     
        


    pygame.display.flip()
    pygame.display.update()
    clock.tick(60) 