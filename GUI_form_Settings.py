import pygame
from pygame.locals import *

from GUI_label  import *
from GUI_button_image  import *
from GUI_form import *
from GUI_slider import *


class FormSettings(Form):
    def __init__(self,screen,x,y,w,h,color_background,border_color,active,path_img):
        super().__init__(screen,x,y,w,h,color_background,border_color,active)

        imagen_aux = pygame.image.load(path_img)
        
        self._slave = imagen_aux
        self.volume = 0.1
        self.flag_volume = True

        ##############################
        self.btn_play_image = Button_Image(self._slave,x,y,70,100,150,90,"C:/Users/topit/TheRickAdventures/recursos/button_0.png",self.btn_play_click,"")

        self.btn_pause_image = Button_Image(self._slave,x,y,70,250,150,90,"C:/Users/topit/TheRickAdventures/recursos/button_2.png",self.btn_pause_click,"")

        self.btn_back_image = Button_Image(self._slave,x,y,70,390,150,90,"C:/Users/topit/TheRickAdventures/recursos/button_back.png",self.btn_back_click,"")
        
      
        
        ##############################

        self.lista_widgets.append(self.btn_pause_image)
        self.lista_widgets.append(self.btn_play_image)
        self.lista_widgets.append(self.btn_back_image)
        

        
    def update(self,lista_eventos):
        if self.active:
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
    
    def btn_play_click(self,texto):
        self.close()
        pygame.mixer.music.play()
    
    def btn_pause_click(self,texto):
        pygame.mixer.music.pause()

    def btn_back_click(self,texto):
        self.end_dialog()
    
