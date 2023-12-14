import pygame
from pygame.locals import *

from GUI_label  import *
from GUI_button_image  import *
from GUI_form import *
from GUI_slider import *
from classManejadoraNiveles import *
from GUI_Contenedor_levels import FormContenedor



class FormLevels(Form):
    def __init__(self,screen,x,y,w,h,color_background,border_color,active,path_img):
        super().__init__(screen,x,y,w,h,color_background,border_color,active =True)

        imagen_aux = pygame.image.load(path_img)        
        self._slave = imagen_aux
        self.manejador_levels = Manejador_Levels(self._master)
        self.portal1 = self.manejador_levels.get_nivel("nivel_1").end_point
        self.lista_jugadores = self.manejador_levels.get_nivel("nivel_1").lista_personajes
        


        ##############################
        self.btn_level_1 = Button_Image(self._slave,x,y,70,100,150,90,"recursos/level_0.png",self.play_level,"nivel_1")

        self.btn_level_2 = Button_Image(self._slave,x,y,70,250,150,90,"recursos/level_1.png",self.play_level,"nivel_2")

        self.btn_level_3 = Button_Image(self._slave,x,y,70,400,150,90,"recursos/level_2.png",self.play_level,"nivel_3")

        self.btn_menu_in_levels = Button_Image(self._slave,self._x,self._y,1400,650,70,40,"recursos/button_1.png",self.btn_menu_in_levels,"")
        ##############################

        self.lista_widgets.append(self.btn_level_1)
        self.lista_widgets.append(self.btn_level_2)
        self.lista_widgets.append(self.btn_level_3)
        self.lista_widgets.append(self.btn_menu_in_levels)
    
    def update(self,lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                self.draw()
                if self.portal1.cambio_level(self.lista_jugadores):
                   self.end_dialog()   
        else:
            self.hijo.update(lista_eventos)

    def play_level(self,level_x):
        nivel = self.manejador_levels.get_nivel(level_x)
        form_contenedor = FormContenedor(self._master,nivel)
        self.show_dialog(form_contenedor)

    
             
    
    def btn_menu_in_levels(self,param):
        self.end_dialog()
    

   
    