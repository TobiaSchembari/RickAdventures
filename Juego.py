from clasesOverWorld import Overworld
from level import Level 
from UI import UI
import pygame
import sqlite3



class Game:
    def __init__(self,surface):
        #game attributes // declarados en esta clase ya ue es la unica vigente durante todo el juego y no por nivel.
        self.max_health = 100
        self.current_health = 100
        self.coins = 0
        self.score = 0

        self.bg_music = pygame.mixer.Sound('C:/Users/topit/TheRickAdventures/recursos/rick_morty_louder.mp3')
        self.overworld_bg_music =pygame.mixer.Sound('C:/Users/topit/TheRickAdventures/recursos/suspense.mp3')

        self.last_level = 3
        self.overworld = Overworld(0,self.last_level,surface,self.create_level)
        self.status = 'overworld'
        self.overworld_bg_music.play(loops = -1) #cuando temrina empeiza de nuevo 

        self.surface = surface

        self.ui = UI(surface)

    
    def create_level(self,current_level):
        self.overworld_bg_music.stop()
        self.bg_music.play(loops = -1)
        self.level = Level(current_level,self.surface,self.create_overworld,self.change_coins,self.change_health,self.update_score)
        self.status = 'level'

    def create_overworld(self,current_level,new_last_level):
        self.guardar_score_en_base_de_datos()
        if new_last_level > self.last_level:
            self.last_level = new_last_level
        self.overworld = Overworld(current_level,self.last_level,self.surface,self.create_level)
        self.status = 'overworld'
        self.overworld_bg_music.play(loops = -1)
        self.bg_music.stop()
    
    def change_health(self,amount):
        self.current_health += amount

    def change_coins(self,amount):
        self.coins += amount

    def update_score(self, points):
        self.score += points

    def game_over(self):
        if self.current_health <= 0:
            self.guardar_score_en_base_de_datos()
            self.current_health = 100
            self.coins = 0
            self.score = 0
            self.last_level = 3
            self.overworld = Overworld(0,self.last_level,self.surface,self.create_level)
            self.status = "overworld"

    

    # def guardar_score_en_base_de_datos(self):
    #     with sqlite3.connect("test_data_base.db") as conexion:
    #         try:
    #             sentencia = f'''
    #                     insert into SCORES (Nombre,Score,Coins) values("tobi",{self.score},{self.coins})

    #                 '''
    #             conexion.execute(sentencia)                
    #         except Exception as e:
    #                 print(f"Error: {e}")
    def guardar_score_en_base_de_datos(self):
        with sqlite3.connect("test_data2.db") as conexion:
            try:
            # Crear la tabla si no existe
                create_table_sentencia = '''
                    CREATE TABLE IF NOT EXISTS SCORES (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        Nombre TEXT,
                        Score INTEGER,
                        Coins INTEGER
                    );
                '''
                conexion.execute(create_table_sentencia)

                # Insertar datos en la tabla
                insert_sentencia = f'''
                    INSERT INTO SCORES (Nombre, Score, Coins) VALUES ("tobi", {self.score}, {self.coins});
                '''
                conexion.execute(insert_sentencia)
            except Exception as e:
                print(f"Error: {e}")
    
    def run(self):
        if self.status == 'overworld':
            self.overworld.run()
        else:
            self.level.run()
            self.ui.show_health(self.current_health,self.max_health)
            self.ui.show_coins(self.coins)
            self.ui.show_score(self.score)
            self.game_over()
            
            
            
            
 


    