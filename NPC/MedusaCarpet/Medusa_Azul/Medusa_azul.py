import pygame
import random
from NPC.MedusaCarpet.Medusa_normal.Constantes_de_medusa import ALTO_DE_MEDUSA, ANCHO_DE_MEDUSA

class Medusa_Azul:
    def __init__(self):
        self.cantidad_de_medusas_azules_eliminadas = 0
        
        # Cargar y escalar el sprite
        self.sprite_de_medusa_azul_A = pygame.image.load("NPC/MedusaCarpet/Medusa_Azul/Medusa_Azul_Sprites/medusaAzul1.png")
        self.sprite_de_medusa_azul_A = pygame.transform.scale(self.sprite_de_medusa_azul_A, (ANCHO_DE_MEDUSA*.9, ALTO_DE_MEDUSA*.85))
        self.sprite_de_medusa_azul_B = pygame.image.load("NPC/MedusaCarpet/sprites/medusa2.png")
        self.sprite_de_medusa_azul_B = pygame.transform.scale(self.sprite_de_medusa_azul_B, (ANCHO_DE_MEDUSA*.9, ALTO_DE_MEDUSA*.85))
        
        # Crear el rectángulo del sprite
        self.medusa_azul_posicion = self.sprite_de_medusa_azul_A.get_rect(center=(-300,-300))
        
        # Crear la hitbox como un rectángulo independiente
        self.hitbox = pygame.Rect(self.medusa_azul_posicion.x, self.medusa_azul_posicion.y, ANCHO_DE_MEDUSA*.45, ALTO_DE_MEDUSA*.85)
        
        self.Destino = None
        self.Destino_Aleatorio = None
        self.Tiempo_sin_electrocutar = 0
        self.medusa_eliminada = False
        self.Tiempo_que_lleva_eliminada_la_medusa = 0
        self.Electrocutando = False
        self.Sonido_de_eliminacion = pygame.mixer.Sound("Musica/Pop.wav")
        
        # Mover la hitbox junto con la medusa
        self.hitbox.center = self.medusa_azul_posicion.center

    
    def Randomisar_genero(self):
        self.Genero = random.randint(1,2)
        #Macho
        if self.Genero == 1:
            self.sprite_de_medusa_A = pygame.transform.scale(self.sprite_de_medusa_azul_A, (ANCHO_DE_MEDUSA*.9, ALTO_DE_MEDUSA*.85))
            self.sprite_de_medusa_B = pygame.transform.scale(self.sprite_de_medusa_azul_B, (ANCHO_DE_MEDUSA*.9, ALTO_DE_MEDUSA*.85))
            # Crear la hitbox como un rectángulo independiente
            self.hitbox = pygame.Rect(self.medusa_azul_posicion.x, self.medusa_azul_posicion.y, ANCHO_DE_MEDUSA*.45, ALTO_DE_MEDUSA*.85)
            # Mover la hitbox junto con la medusa
            self.hitbox.center = self.medusa_azul_posicion.center
        
        #Embra
        elif self.Genero == 2:
            self.sprite_de_medusa_A = pygame.transform.scale(self.sprite_de_medusa_azul_A, (ANCHO_DE_MEDUSA*.8, ALTO_DE_MEDUSA*.86))
            self.sprite_de_medusa_B = pygame.transform.scale(self.sprite_de_medusa_azul_B, (ANCHO_DE_MEDUSA*.8, ALTO_DE_MEDUSA*.86))
            # Crear la hitbox como un rectángulo independiente
            self.hitbox = pygame.Rect(self.medusa_azul_posicion.x, self.medusa_azul_posicion.y, ANCHO_DE_MEDUSA*.45, ALTO_DE_MEDUSA*.85)
            # Mover la hitbox junto con la medusa
            self.hitbox.center = self.medusa_azul_posicion.center

    
    def Randomisar_Spawn_poin(self):
        self.Spawn_poin = random.randint(1,4)
        if self.Spawn_poin == 1:
            self.medusa_azul_posicion = self.sprite_de_medusa_azul_A.get_rect(center=(565.5, 160.5))
        if self.Spawn_poin == 2:
            self.medusa_azul_posicion = self.sprite_de_medusa_azul_A.get_rect(center=(515.5, 15.5))
        if self.Spawn_poin == 3:
            self.medusa_azul_posicion = self.sprite_de_medusa_azul_A.get_rect(center=(-184.5, 160.5))
        if self.Spawn_poin == 4:
            self.medusa_azul_posicion = self.sprite_de_medusa_azul_A.get_rect(center=(-184.5, 40.5))
                                     
                
    def mover_medusa(self, Velocidad, Destino_X, Destino_Y, Total_de_medusas_eliminadas, posicion_x_de_jugador, posicion_y_de_jugador):
        if Total_de_medusas_eliminadas < 100:
            if self.Electrocutando == False:
                self.Destino = (Destino_X, Destino_Y)
                
                if self.Destino != self.medusa_azul_posicion.topleft:
                    if self.medusa_azul_posicion.x < Destino_X:
                        self.medusa_azul_posicion.x += Velocidad
                    elif self.medusa_azul_posicion.x > Destino_X:
                        self.medusa_azul_posicion.x -= Velocidad
                        
                    if self.medusa_azul_posicion.y < Destino_Y:
                        self.medusa_azul_posicion.y += Velocidad
                    elif self.medusa_azul_posicion.y > Destino_Y:
                        self.medusa_azul_posicion.y -= Velocidad
        else:
            if self.Electrocutando == False:
                self.Destino = (Destino_X, Destino_Y)
                
                if self.Destino != self.medusa_azul_posicion.topleft:
                    if self.medusa_azul_posicion.x < Destino_X:
                        self.medusa_azul_posicion.x += Velocidad
                    elif self.medusa_azul_posicion.x > Destino_X:
                        self.medusa_azul_posicion.x -= Velocidad
                        
                    if self.medusa_azul_posicion.y < Destino_Y:
                        self.medusa_azul_posicion.y += Velocidad
                    elif self.medusa_azul_posicion.y > Destino_Y:
                        self.medusa_azul_posicion.y -= Velocidad
            else:
                if self.Electrocutando == True:
                    if posicion_x_de_jugador < self.medusa_azul_posicion.x:
                        self.medusa_azul_posicion.x -= Velocidad
                    elif posicion_x_de_jugador > self.medusa_azul_posicion.x:
                            self.medusa_azul_posicion.x += Velocidad
                    
                    if posicion_y_de_jugador < self.medusa_azul_posicion.y:
                        self.medusa_azul_posicion.y -= Velocidad
                    elif posicion_y_de_jugador > self.medusa_azul_posicion.y:
                        self.medusa_azul_posicion.y += Velocidad
                    
        # Mover la hitbox junto con la medusa
        self.hitbox.center = self.medusa_azul_posicion.center
                
    def mover_medusa_azul_aleatoriamente(self, Velocidad, Limite_Norte, Limite_Sur, Limite_Este, Limite_Oeste, Total_de_medusas_eliminadas, posicion_x_de_jugador, posicion_y_de_jugador):
        if Total_de_medusas_eliminadas >= 5:
            if self.Destino_Aleatorio is None or self.medusa_azul_posicion.collidepoint(self.Destino_X_Aleatorio, self.Destino_Y_Aleatorio):
                self.Destino_X_Aleatorio = random.randint(Limite_Oeste, Limite_Este)
                self.Destino_Y_Aleatorio = random.randint(Limite_Norte, Limite_Sur)
                self.Destino_Aleatorio = (self, Velocidad, self.Destino_X_Aleatorio,  self.Destino_Y_Aleatorio, Total_de_medusas_eliminadas, posicion_x_de_jugador, posicion_y_de_jugador)
            
            self.mover_medusa(Velocidad, self.Destino_X_Aleatorio, self.Destino_Y_Aleatorio, Total_de_medusas_eliminadas, posicion_x_de_jugador, posicion_y_de_jugador)
        
    def check_collision(self, keys, other_rect, Limite_Norte, Limite_Sur, Limite_Este, Limite_Oeste, Total_de_medusas_eliminadas, evento_1):
        if self.hitbox.colliderect(other_rect) and evento_1 == False:
            print("MEDUSA AZUL")
            if Total_de_medusas_eliminadas >= 5:    
                if self.hitbox.colliderect(other_rect):
                    if (keys[pygame.K_SPACE] or keys[pygame.K_KP_0]) and self.Electrocutando == False:
                        self.cantidad_de_medusas_azules_eliminadas +=1            
                        self.medusa_eliminada = True
                        self.Sonido_de_eliminacion.play(1)
                        
                elif self.Electrocutando == True and evento_1 == False:
                    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and self.medusa_azul_posicion.x < Limite_Este:
                        self.medusa_azul_posicion.x += 25
                    
                    elif (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.medusa_azul_posicion.x > Limite_Oeste:
                        self.medusa_azul_posicion.x -= 25                
                    
                    if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and self.medusa_azul_posicion.y > Limite_Norte:
                        self.medusa_azul_posicion.y += 25
                    
                    elif (keys[pygame.K_w] or keys[pygame.K_UP])and self.medusa_azul_posicion.y < Limite_Sur:
                        self.medusa_azul_posicion.y -= 25 
                    else:
                        return
            
                    
    def Ataque_de_medusa(self):
        if self.medusa_eliminada == False:       
            if self.Tiempo_sin_electrocutar < 1000 and self.Electrocutando == False:
                self.Tiempo_sin_electrocutar += 1
        
            elif self.Tiempo_sin_electrocutar <= 1000:
                self.Electrocutando = True
                self.Tiempo_sin_electrocutar -= 1
                if self.Tiempo_sin_electrocutar == 0:
                    self.Electrocutando = False
        
    def dibujar_medusa_azul(self, keys, pantalla, Total_de_medusas_eliminadas, opciones_de_administrador_activadas):
        if Total_de_medusas_eliminadas >= 5:
            if self.medusa_eliminada == False:       
                #Dibujar sprite de medusa corespondiente
                if self.Electrocutando == False:
                    pantalla.blit(self.sprite_de_medusa_azul_A, self.medusa_azul_posicion)                
                if self.Electrocutando == True:
                    pantalla.blit(self.sprite_de_medusa_azul_B, self.medusa_azul_posicion)                
                
                if keys[pygame.K_F3] and opciones_de_administrador_activadas == True:
                    pygame.draw.rect(pantalla, (0, 0, 225), self.hitbox, 2)  # Dibuja la hitbox para visualizarla                  
                    
            else:
    
                self.medusa_azul_posicion.x = 1000
                self.Tiempo_que_lleva_eliminada_la_medusa += 1
                if self.Tiempo_que_lleva_eliminada_la_medusa >= 250:
                    self.Tiempo_que_lleva_eliminada_la_medusa = 0
                    self.Randomisar_Spawn_poin()
                    self.Randomisar_genero()
                    self.hitbox.center = self.medusa_azul_posicion.center
                    self.medusa_eliminada = False
        