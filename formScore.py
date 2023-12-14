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







class FormScore(Form):
    def __init__(self,screen,x,y,w,h,color_background,border_color,active,path_img):
        super().__init__(screen,x,y,w,h,color_background,border_color,active)

        imagen_aux = pygame.image.load(path_img)
        
        self._slave = imagen_aux