import pygame

class Corazon:
    def __init__(self,vida_del_jugador):
        #Cargar los sprites
        self.Corazon_sprite_1 = pygame.image.load("Objetos/CorasonesCarpet/corasones_normal/corazon1.png")
        self.Corazon_sprite_1 = pygame.transform.scale(self.Corazon_sprite_1,(40,40))
        
        self.Corazon_sprite_2 = pygame.image.load("Objetos/CorasonesCarpet/corasones_normal/corazon2.png")
        self.Corazon_sprite_2 = pygame.transform.scale(self.Corazon_sprite_2,(84,40))
        
        self.Corazon_sprite_3 = pygame.image.load("Objetos/CorasonesCarpet/corasones_normal/corazon3.png")
        self.Corazon_sprite_3 = pygame.transform.scale(self.Corazon_sprite_3,(128,40))
        
        self.Corazon_sprite_4 = pygame.image.load("Objetos/CorasonesCarpet/corasones_normal/corazon4.png")
        self.Corazon_sprite_4 = pygame.transform.scale(self.Corazon_sprite_4,(172,40))
        
        self.Corazon_sprite_5 = pygame.image.load("Objetos/CorasonesCarpet/corasones_normal/corazon5.png")
        self.Corazon_sprite_5 = pygame.transform.scale(self.Corazon_sprite_5,(216,40))
        
        #Establecer la variables de la vida
        self.vida_del_jugador = vida_del_jugador
        #Pocion
        self.pocion = (10,10)
        
    
    def dibujar_corazones(self, pantalla, sprite):
        pantalla.blit(sprite, self.pocion)
        
            
    def Mostrar_vida(self, pantalla, vida_del_jugador):
        if self.vida_del_jugador == 5:
            self.dibujar_corazones(pantalla, self.Corazon_sprite_5)
        
        elif self.vida_del_jugador == 4:
            self.dibujar_corazones(pantalla, self.Corazon_sprite_4)
        
        elif self.vida_del_jugador == 3:
            self.dibujar_corazones(pantalla, self.Corazon_sprite_3)
        
        elif self.vida_del_jugador == 2:
            self.dibujar_corazones(pantalla, self.Corazon_sprite_2)
        
        elif self.vida_del_jugador == 1:
            self.dibujar_corazones(pantalla, self.Corazon_sprite_1)
               
        #Checar la vida
        self.vida_del_jugador = vida_del_jugador
    # El juego tiene 589 lineas de codigo beta 2 [23/11/2024] #