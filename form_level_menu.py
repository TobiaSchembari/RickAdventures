import pygame
from pygame.locals import *

from GUI_button  import *
from GUI_label  import *
from GUI_button_image  import *
from GUI_textbox  import *
from GUI_widget  import *
from GUI_slider import *
from GUI_form import *
from GUI_picture_box import *
from GUI_form_Settings import FormSettings
from GUI_form_Levels import FormLevels

class Forms_menu_level(Form):
    def __init__(self,screen,x,y,w,h,color_background,border_color,border_size, active = True):
        super().__init__(screen,x,y,w,h,color_background,border_color,border_size)

        self.volume = 0.1
        self.flag_volume = True
        self.level_activo = False


        pygame.mixer.init()

        
        ################# CONTROLES #################
        pygame.mixer.music.load("recursos/rick_morty_louder.mp3")

        self.bg_image = PictureBox(self._slave,x,y,w,h,"recursos/icono.jpg")

        self.btn_settings_image = Button_Image(self._master,x,y,70,280,150,90,"recursos/button_3.png",self.btn_settings_click,"")
        #############################################

        # Anadir a lista de eventos los controles 
        self.lista_widgets.append(self.bg_image)
        self.lista_widgets.append(self.btn_settings_image)
        #############################################

        pygame.mixer.music.set_volume(self.volume)
        pygame.mixer.music.play(-1)
        
        self.render()
    
    def update(self,lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
        else: 
            self.hijo.update(lista_eventos)

   
    def btn_settings_click(self,lista_eventos):
        form_settings = FormSettings(self._master,0,0,1500,700,"black","Dark green",True,"recursos/settings_img.png")
        self.show_dialog(form_settings)
    
    def render(self):
        self._slave.fill(self._color_background)