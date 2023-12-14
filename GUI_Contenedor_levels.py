import pygame
from pygame.locals import *
from GUI_form import *
from GUI_button_image import *

class FormContenedor(Form):
    def __init__(self,pantalla,level):
        pygame.mixer.music.pause()
        super().__init__(pantalla,0,0,pantalla.get_width(),pantalla.get_height(),"")
        level._slave = self._slave
        self.level = level
        self.btn_menu_in_game = Button_Image(self._slave,self._x,self._y,1400,650,70,40,"recursos/button_1.png",self.btn_menu_in_game,"")


        self.lista_widgets.append(self.btn_menu_in_game)
     
    def update(self,lista_eventos):
        self.level.update(lista_eventos)
        for widget in self.lista_widgets:
            widget.update(lista_eventos)
        self.draw()
    
    def btn_menu_in_game(self,param):
        self.end_dialog()
        
