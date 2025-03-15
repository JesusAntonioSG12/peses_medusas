import pygame
import random
from Objetos.BurbujaCarpet import Constantes_de_burbuja

class Burbuja:
    def __init__(self):
        #Cargar y transformar sprites
        self.Burbuja_sprite_1 = pygame.image.load("Objetos/BurbujaCarpet/sprites/Burbuja1.png")
        self.Burbuja_sprite_1 = pygame.transform.scale(self.Burbuja_sprite_1,(Constantes_de_burbuja.ANCHO_DE_BURBUJA,Constantes_de_burbuja.ALTO_DE_BURBUJA))
        
        self.Burbuja_sprite_2 = pygame.image.load("Objetos/BurbujaCarpet/sprites/Burbuja2.png")
        self.Burbuja_sprite_2 = pygame.transform.scale(self.Burbuja_sprite_2,(Constantes_de_burbuja.ANCHO_DE_BURBUJA,Constantes_de_burbuja.ALTO_DE_BURBUJA))
        
        self.Burbuja_sprite_3 = pygame.image.load("Objetos/BurbujaCarpet/sprites/Burbuja3.png")
        self.Burbuja_sprite_3 = pygame.transform.scale(self.Burbuja_sprite_3,(Constantes_de_burbuja.ANCHO_DE_BURBUJA,Constantes_de_burbuja.ALTO_DE_BURBUJA))
        
        self.Burbuja_posicion = self.Burbuja_sprite_1.get_rect(center=(70, 500))
        
        self.Burbuja_reventada = False
        self.tipo_de_burbuja = 1
        # Crear la hitbox como un rectángulo independiente
        self.hitbox = pygame.Rect(self.Burbuja_posicion.x, self.Burbuja_posicion.y, 90, 90)
        self.hitbox.center = self.Burbuja_posicion.center
        self.Randomisar_burbuja = None
        
    def Dibujar_burbuja(self, pantalla, keys, Total_de_medusas_eliminadas, opciones_de_administrador_activadas, vida):
        self.Total_de_medusas_eliminadas = Total_de_medusas_eliminadas       
        if self.Total_de_medusas_eliminadas >= 5:
            if self.tipo_de_burbuja == None:
                if self.Total_de_medusas_eliminadas >= 15:
                        if vida >= 4:
                            self.tipo_de_burbuja = 1                 
                        elif vida == 3 or vida == 2:
                            self.tipo_de_burbuja = 2
                        elif vida == 1:
                            self.Randomisar_burbuja = random.randint(1,10)
                            if self.Randomisar_burbuja == 7:
                                self.tipo_de_burbuja = 3  
                            else:
                                self.tipo_de_burbuja = 2
                else:
                    if vida > 3:
                            self.tipo_de_burbuja = 1                    
                    elif vida <= 3:
                        self.tipo_de_burbuja = 2                    
        
            if self.tipo_de_burbuja == 1:
                pantalla.blit(self.Burbuja_sprite_1, self.Burbuja_posicion)
            elif self.tipo_de_burbuja == 2:
                pantalla.blit(self.Burbuja_sprite_2, self.Burbuja_posicion)
            elif self.tipo_de_burbuja == 3:
                pantalla.blit(self.Burbuja_sprite_3, self.Burbuja_posicion)
            
            if keys[pygame.K_F3] and opciones_de_administrador_activadas == True:
                    pygame.draw.rect(pantalla, (0, 225,100), self.hitbox, 2)  # Dibuja la hitbox
                
                
    def Mover_Burbuja(self):
        if self.Burbuja_reventada == False:
            if self.Burbuja_posicion.y <= -550 and self.Burbuja_reventada == False:
                self.Burbuja_posicion.y = 500    
            else:
                self.Burbuja_posicion.y -= 1
                self.hitbox.center = self.Burbuja_posicion.center

    def check_collision(self, total_medusas_eliminadas ,vida, pez_hitboz, pez_cabeza_hitboz, event_key):
        if self.Burbuja_reventada == False and total_medusas_eliminadas >= 5:
            if self.hitbox.colliderect((pez_hitboz) or (pez_cabeza_hitboz)):
                if event_key in [pygame.K_SPACE, pygame.K_KP_0]:
                    self.Burbuja_reventada = True
                    if self.Burbuja_reventada == True:
                        self.tipo_de_burbuja = None
                        self.Burbuja_posicion.y = 2000
                        self.Burbuja_reventada = False
