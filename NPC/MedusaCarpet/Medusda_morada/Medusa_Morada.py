import pygame
import random
from NPC.MedusaCarpet.Medusa_normal.Constantes_de_medusa import ALTO_DE_MEDUSA, ANCHO_DE_MEDUSA

class Medusa_Morada:
    def __init__(self):
        self.Vida = 1
        self.cantidad_de_medusas_moradas_eliminadas = 0

            #Crear sprites
        self.sprite_de_medusa_morada_A = pygame.image.load("NPC/MedusaCarpet/Medusda_morada/Medusda_morada_sprite/medusamorada1.png")
        self.sprite_de_medusa_morada_A = pygame.transform.scale(self.sprite_de_medusa_morada_A, (ANCHO_DE_MEDUSA, ALTO_DE_MEDUSA))
        self.sprite_de_medusa_morada_B = pygame.image.load("NPC/MedusaCarpet/sprites/medusa2.png")
        self.sprite_de_medusa_morada_B = pygame.transform.scale(self.sprite_de_medusa_morada_B, (ANCHO_DE_MEDUSA, ALTO_DE_MEDUSA))
            
        # Crear posicion
        self.medusa_morada_posicion = self.sprite_de_medusa_morada_A.get_rect(center=(-184.5, 160.5))
            
        # Crear la hitbox como un rectángulo independiente
        self.hitbox = None
        
        self.Destino = None
        self.Destino_Aleatorio = None
        self.Tiempo_sin_electrocutar = 0
        self.medusa_morada_eliminada = False
        self.Electrocutando = False
        self.Tiempo_para_volver_a_resivir_daño = 0
        self.Sonido_de_eliminacion = pygame.mixer.Sound("Musica/Pop.wav")
        self.Tiempo_que_lleva_eliminada_la_medusa = 0
    
    def update_hitbox(self):
        if not self.medusa_morada_eliminada:
            self.hitbox = pygame.Rect(self.medusa_morada_posicion.x, self.medusa_morada_posicion.y, ANCHO_DE_MEDUSA*.55, ALTO_DE_MEDUSA)
            self.hitbox.center = self.medusa_morada_posicion.center
        else: self.hitbox = None
    
    def Randomisar_genero(self):
        self.Genero = random.randint(1,2)
        #Macho
        if self.Genero == 1:
            self.sprite_de_medusa_morada_A = pygame.transform.scale(self.sprite_de_medusa_morada_A, (ANCHO_DE_MEDUSA, ALTO_DE_MEDUSA))
            self.sprite_de_medusa_morada_B = pygame.transform.scale(self.sprite_de_medusa_morada_B, (ANCHO_DE_MEDUSA, ALTO_DE_MEDUSA))
            # Crear la hitbox como un rectángulo independiente
            self.hitbox = pygame.Rect(self.medusa_morada_posicion.x, self.medusa_morada_posicion.y, ANCHO_DE_MEDUSA*.55, ALTO_DE_MEDUSA)
            # Mover la hitbox junto con la medusa
            self.hitbox.center = self.medusa_morada_posicion.center
        #Embra
        elif self.Genero == 2:
            self.sprite_de_medusa_morada_A = pygame.transform.scale(self.sprite_de_medusa_morada_A, (ANCHO_DE_MEDUSA, ALTO_DE_MEDUSA))
            self.sprite_de_medusa_morada_B = pygame.transform.scale(self.sprite_de_medusa_morada_B, (ANCHO_DE_MEDUSA, ALTO_DE_MEDUSA))
            # Crear la hitbox como un rectángulo independiente
            self.hitbox = pygame.Rect(self.medusa_morada_posicion.x, self.medusa_morada_posicion.y, ANCHO_DE_MEDUSA*.53, ALTO_DE_MEDUSA)
            # Mover la hitbox junto con la medusa
            self.hitbox.center = self.medusa_morada_posicion.center

    def Randomisar_Spawn_poin(self):
        self.Spawn_poin = random.randint(1,4)
        if self.Spawn_poin == 1:
            self.medusa_morada_posicion = self.sprite_de_medusa_morada_A.get_rect(center=(565.5, 160.5))
        if self.Spawn_poin == 2:
            self.medusa_morada_posicion = self.sprite_de_medusa_morada_A.get_rect(center=(515.5, 15.5))
        if self.Spawn_poin == 3:
            self.medusa_morada_posicion = self.sprite_de_medusa_morada_A.get_rect(center=(-184.5, 160.5))
        if self.Spawn_poin == 4:
            self.medusa_morada_posicion = self.sprite_de_medusa_morada_A.get_rect(center=(-184.5, 40.5))
                                                         
                
    def mover_medusa_morada(self, Velocidad, Destino_X, Destino_Y, Total_de_medusas_eliminadas, posicion_x_de_jugador, posicion_y_de_jugador):
        if Total_de_medusas_eliminadas < 100:
            if self.Electrocutando == False:
                self.Destino = (Destino_X, Destino_Y)
                
                if self.Destino != self.medusa_morada_posicion.topleft:
                    if self.medusa_morada_posicion.x < Destino_X:
                        self.medusa_morada_posicion.x += Velocidad
                    elif self.medusa_morada_posicion.x > Destino_X:
                        self.medusa_morada_posicion.x -= Velocidad
                        
                    if self.medusa_morada_posicion.y < Destino_Y:
                        self.medusa_morada_posicion.y += Velocidad
                    elif self.medusa_morada_posicion.y > Destino_Y:
                        self.medusa_morada_posicion.y -= Velocidad
        else:
            if self.Electrocutando == False:
                self.Destino = (Destino_X, Destino_Y)
                
                if self.Destino != self.medusa_morada_posicion.topleft:
                    if self.medusa_morada_posicion.x < Destino_X:
                        self.medusa_morada_posicion.x += Velocidad
                    elif self.medusa_morada_posicion.x > Destino_X:
                        self.medusa_morada_posicion.x -= Velocidad
                        
                    if self.medusa_morada_posicion.y < Destino_Y:
                        self.medusa_morada_posicion.y += Velocidad
                    elif self.medusa_morada_posicion.y > Destino_Y:
                        self.medusa_morada_posicion.y -= Velocidad
            else:
                if self.Electrocutando == True:
                    if posicion_x_de_jugador < self.medusa_morada_posicion.x:
                        self.medusa_morada_posicion.x -= Velocidad
                    elif posicion_x_de_jugador > self.medusa_morada_posicion.x:
                            self.medusa_morada_posicion.x += Velocidad
                    
                    if posicion_y_de_jugador < self.medusa_morada_posicion.y:
                        self.medusa_morada_posicion.y -= Velocidad
                    elif posicion_y_de_jugador > self.medusa_morada_posicion.y:
                        self.medusa_morada_posicion.y += Velocidad
                        
        
                
    def mover_medusa_morada_aleatoriamente(self, Velocidad, Limite_Norte, Limite_Sur, Limite_Este, Limite_Oeste, Total_de_medusas_eliminadas, posicion_x_de_jugador, posicion_y_de_jugador):
        if Total_de_medusas_eliminadas >= 50 and self.medusa_morada_eliminada == False:
            if self.Destino_Aleatorio is None or self.medusa_morada_posicion.collidepoint(self.Destino_Aleatorio):
                self.Destino_X_Aleatorio = random.randint(Limite_Oeste, Limite_Este)
                self.Destino_Y_Aleatorio = random.randint(Limite_Norte, Limite_Sur)
                self.Destino_Aleatorio = (self.Destino_X_Aleatorio, self.Destino_Y_Aleatorio)
            
            self.mover_medusa_morada(Velocidad, self.Destino_X_Aleatorio, self.Destino_Y_Aleatorio, Total_de_medusas_eliminadas, posicion_x_de_jugador, posicion_y_de_jugador)
        
    def check_collision(self, keys, other_rect, Limite_Norte, Limite_Sur, Limite_Este, Limite_Oeste, evento_1, Total_de_medusas_eliminadas):
        if self.hitbox and self.hitbox.colliderect(other_rect) and evento_1 == False:
            if self.medusa_morada_eliminada == False:
                if (keys in [pygame.K_SPACE, pygame.K_KP_0]) and not self.Electrocutando and self.Tiempo_para_volver_a_resivir_daño <= 0:
                    self.Vida = self.Vida - 1
                    self.Tiempo_para_volver_a_resivir_daño = 250
                
                if self.Vida == 0:      
                    self.medusa_morada_eliminada = True
                    self.Sonido_de_eliminacion.play(1)
                    self.cantidad_de_medusas_moradas_eliminadas += 1

                if self.Electrocutando == True and evento_1 == False:
                    if (keys in [pygame.K_d, pygame.K_RIGHT]) and self.medusa_morada_posicion.x < Limite_Este:
                        self.medusa_morada_posicion.x += 20
                    
                    elif (keys in [pygame.K_a, pygame.K_LEFT]) and self.medusa_morada_posicion.x > Limite_Oeste:
                        self.medusa_morada_posicion.x -= 20                
                    
                    elif (keys in [pygame.K_s, pygame.K_DOWN]) and self.medusa_morada_posicion.y > Limite_Norte:
                        self.medusa_morada_posicion.y += 20
                    
                    elif (keys in [pygame.K_w, pygame.K_UP]) and self.medusa_morada_posicion.y < Limite_Sur:
                        self.medusa_morada_posicion.y -= 20
                    else:
                        return
                    
    def Ataque_de_medusa_morada(self):
        if self.medusa_morada_eliminada == False:       
            if self.Tiempo_sin_electrocutar < 250 and self.Electrocutando == False:
                self.Tiempo_sin_electrocutar += 1
        
            elif self.Tiempo_sin_electrocutar <= 1500:
                self.Electrocutando = True
                self.Tiempo_sin_electrocutar -= 1
                if self.Tiempo_sin_electrocutar == 0:
                    self.Electrocutando = False
        
    def dibujar_medusa_morada(self, keys, pantalla, Total_de_medusas_eliminadas, opciones_de_administrador_activadas):
        if Total_de_medusas_eliminadas >= 50:
            if self.medusa_morada_eliminada == False:
                self.update_hitbox();      
                #Dibujar sprite de rey medusa corespondiente
                if self.Electrocutando == False:
                    pantalla.blit(self.sprite_de_medusa_morada_A, self.medusa_morada_posicion)                
                else:
                    pantalla.blit(self.sprite_de_medusa_morada_B, self.medusa_morada_posicion)                
                
                if self.Tiempo_para_volver_a_resivir_daño > 0:
                    self.Tiempo_para_volver_a_resivir_daño -= 1
                  
                if keys[pygame.K_F3] and opciones_de_administrador_activadas == True:
                    pygame.draw.rect(pantalla, (0, 0, 225), self.hitbox, 2)  # Dibuja la hitbox para visualizarla  
                    
            else:
                self.medusa_morada_posicion.x = 10000
                self.Tiempo_que_lleva_eliminada_la_medusa += 1
                if self.Tiempo_que_lleva_eliminada_la_medusa >= 250:
                    self.Tiempo_que_lleva_eliminada_la_medusa = 0
                    self.Randomisar_Spawn_poin()
                    self.Randomisar_genero()
                    self.hitbox.center = self.medusa_morada_posicion.center
                    self.Vida = 5
                    self.medusa_morada_eliminada = False
                    
    
        