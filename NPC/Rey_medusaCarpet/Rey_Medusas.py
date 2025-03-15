import pygame
import random
from NPC.MedusaCarpet.Medusa_normal.Constantes_de_medusa import ALTO_DE_MEDUSA, ANCHO_DE_MEDUSA

class Rey_Medusa:
    def __init__(self):
        self.Vida = 100
                   
            #Crear sprites
        self.sprite_de_rey_medusa_A = pygame.image.load("NPC/Rey_medusaCarpet/Rey_medusaCarpet_sprite/rey_medusa1.png")
        self.sprite_de_rey_medusa_A = pygame.transform.scale(self.sprite_de_rey_medusa_A, (ANCHO_DE_MEDUSA*1.8, ALTO_DE_MEDUSA*3))
        self.sprite_de_rey_medusa_B = pygame.image.load("NPC/Rey_medusaCarpet/Rey_medusaCarpet_sprite/rey_medusa3.png")
        self.sprite_de_rey_medusa_B = pygame.transform.scale(self.sprite_de_rey_medusa_B, (ANCHO_DE_MEDUSA*1.8, ALTO_DE_MEDUSA*3))
            
        # Crear posicion
        self.rey_medusa_posicion = self.sprite_de_rey_medusa_A.get_rect(center=(ANCHO_DE_MEDUSA + 350, ALTO_DE_MEDUSA + 60))
            
        # Crear la hitbox como un rectángulo independiente
        self.hitbox = None
            
        self.Destino = None
        self.Destino_Aleatorio = None
        self.Tiempo_sin_electrocutar = 0
        self.rey_medusa_eliminada = False
        self.Electrocutando = False
        self.Tiempo_para_volver_a_resivir_daño = 0
        self.Sonido_de_eliminacion = pygame.mixer.Sound("Musica/Pop.wav")
          
    
    
    def update_hitbox(self):
        if not self.rey_medusa_eliminada:
            self.hitbox = pygame.Rect(self.rey_medusa_posicion.x, self.rey_medusa_posicion.y, ANCHO_DE_MEDUSA*1.3, ALTO_DE_MEDUSA*2.5) 
            self.hitbox.center = self.rey_medusa_posicion.center
        else: self.hitbox = None
    
    def Randomisar_Spawn_poin(self):
        self.Spawn_poin = random.randint(1,4)
        if self.Spawn_poin == 1:
            self.rey_medusa_posicion = self.sprite_de_rey_medusa_A.get_rect(center=(ANCHO_DE_MEDUSA + 350, ALTO_DE_MEDUSA + 60))
        if self.Spawn_poin == 2:
            self.rey_medusa_posicion = self.sprite_de_rey_medusa_A.get_rect(center=(ANCHO_DE_MEDUSA + 350, ALTO_DE_MEDUSA + -60))
        if self.Spawn_poin == 3:
            self.rey_medusa_posicion = self.sprite_de_rey_medusa_A.get_rect(center=(ANCHO_DE_MEDUSA + -350, ALTO_DE_MEDUSA + 60))
        if self.Spawn_poin == 4:
            self.rey_medusa_posicion = self.sprite_de_rey_medusa_A.get_rect(center=(ANCHO_DE_MEDUSA + -350, ALTO_DE_MEDUSA + -60))
                                     
                
    def mover_rey_medusa(self, Velocidad, Destino_X, Destino_Y, posicion_x_de_jugador, posicion_y_de_jugador):
        if self.Electrocutando == False:
            if self.Vida > 30:
                self.Destino = (Destino_X, Destino_Y)
                
                if self.Destino != self.rey_medusa_posicion.topleft:
                    if self.rey_medusa_posicion.x < Destino_X:
                        self.rey_medusa_posicion.x += Velocidad
                    elif self.rey_medusa_posicion.x > Destino_X:
                        self.rey_medusa_posicion.x -= Velocidad
                        
                    if self.rey_medusa_posicion.y < Destino_Y:
                        self.rey_medusa_posicion.y += Velocidad
                    elif self.rey_medusa_posicion.y > Destino_Y:
                        self.rey_medusa_posicion.y -= Velocidad
            else: #Correr si se ve bulnerable y debil
                if posicion_x_de_jugador > 0:
                    Destino_X -= Destino_X * 2
                else:
                    Destino_X += Destino_X * 2
                
                if posicion_y_de_jugador > 0:
                    Destino_Y -= Destino_Y * 2
                else:
                    Destino_Y += Destino_Y * 2
                if self.Destino != self.rey_medusa_posicion.topleft:
                    if self.rey_medusa_posicion.x < Destino_X:
                        self.rey_medusa_posicion.x += Velocidad*2
                    elif self.rey_medusa_posicion.x > Destino_X:
                        self.rey_medusa_posicion.x -= Velocidad*2
                        
                    if self.rey_medusa_posicion.y < Destino_Y:
                        self.rey_medusa_posicion.y += Velocidad*2
                    elif self.rey_medusa_posicion.y > Destino_Y:
                        self.rey_medusa_posicion.y -= Velocidad*2
        else:            
            if posicion_x_de_jugador < self.rey_medusa_posicion.x:
                self.rey_medusa_posicion.x -= Velocidad * .5
            elif posicion_x_de_jugador > self.rey_medusa_posicion.x:
                    self.rey_medusa_posicion.x += Velocidad * .5
            
            if posicion_y_de_jugador < self.rey_medusa_posicion.y:
                self.rey_medusa_posicion.y -= Velocidad * .5
            elif posicion_y_de_jugador > self.rey_medusa_posicion.y:
                self.rey_medusa_posicion.y += Velocidad * .5
                        
                
    def mover_rey_medusa_aleatoriamente(self, Velocidad, Limite_Norte, Limite_Sur, Limite_Este, Limite_Oeste, Total_de_medusas_eliminadas, posicion_x_de_jugador, posicion_y_de_jugador):
        if Total_de_medusas_eliminadas >= 100 and self.rey_medusa_eliminada == False:
            if self.Destino_Aleatorio is None or self.rey_medusa_posicion.collidepoint(self.Destino_Aleatorio):
                self.Destino_X_Aleatorio = random.randint(Limite_Oeste, Limite_Este)
                self.Destino_Y_Aleatorio = random.randint(Limite_Norte, Limite_Sur)
                self.Destino_Aleatorio = (self.Destino_X_Aleatorio, self.Destino_Y_Aleatorio)
            
            self.mover_rey_medusa(Velocidad, self.Destino_X_Aleatorio, self.Destino_Y_Aleatorio, posicion_x_de_jugador, posicion_y_de_jugador)
        
    def check_collision(self, keys, other_rect, Limite_Norte, Limite_Sur, Limite_Este, Limite_Oeste, evento_1, Total_de_medusas_eliminadas):
        if self.hitbox and self.hitbox.colliderect(other_rect) and evento_1 == False:
            if (keys in [pygame.K_SPACE, pygame.K_KP_0]) and self.Electrocutando == False and self.Tiempo_para_volver_a_resivir_daño <= 0:
                self.Vida -= 1
                self.Tiempo_para_volver_a_resivir_daño = 1000
            if self.Vida <= 0:      
                self.rey_medusa_eliminada = True
                self.Sonido_de_eliminacion.play(1)
                
            if self.Electrocutando == True and evento_1 == False:
                if (keys in [pygame.K_d, pygame.K_RIGHT]) and self.rey_medusa_posicion.x < Limite_Este:
                    self.rey_medusa_posicion.x += 20
                
                elif (keys in [pygame.K_a, pygame.K_LEFT]) and self.rey_medusa_posiciont.x > Limite_Oeste:
                    self.rey_medusa_posicion.x -= 20                
                
                elif (keys in [pygame.K_s, pygame.K_DOWN]) and self.rey_medusa_posicion.y > Limite_Norte:
                    self.rey_medusa_posicion.y += 20
                
                elif (keys in [pygame.K_w, pygame.K_UP]) and self.rey_medusa_posicion.y < Limite_Sur:
                    self.rey_medusa_posicion.y -= 20   
                else: return
                    
    def Ataque_de_rey_medusa(self):
        if self.rey_medusa_eliminada == False:       
            if self.Tiempo_sin_electrocutar < 1500 and self.Electrocutando == False:
                self.Tiempo_sin_electrocutar += 1
        
            elif self.Tiempo_sin_electrocutar <= 1500:
                self.Electrocutando = True
                self.Tiempo_sin_electrocutar -= 1
                if self.Tiempo_sin_electrocutar == 0:
                    self.Electrocutando = False
        
    def dibujar_rey_medusa(self, keys, pantalla, Total_de_medusas_eliminadas, opciones_de_administrador_activadas):
        if Total_de_medusas_eliminadas >= 100:
            if self.rey_medusa_eliminada == False: 
                self.update_hitbox()      
                #Dibujar sprite de rey medusa corespondiente
                if self.Electrocutando == False:
                    pantalla.blit(self.sprite_de_rey_medusa_A, self.rey_medusa_posicion)                
                else:
                    pantalla.blit(self.sprite_de_rey_medusa_B, self.rey_medusa_posicion)                
                
                if self.Tiempo_para_volver_a_resivir_daño > 0:
                    self.Tiempo_para_volver_a_resivir_daño -= 1
                  
                if keys[pygame.K_F3] and opciones_de_administrador_activadas == True:
                    pygame.draw.rect(pantalla, (0, 0, 225), self.hitbox, 2)  # Dibuja la hitbox para visualizarla  
                    

                    
    
        