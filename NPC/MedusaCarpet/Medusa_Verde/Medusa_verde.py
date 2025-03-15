import pygame
import random
from NPC.MedusaCarpet.Medusa_normal.Constantes_de_medusa import ALTO_DE_MEDUSA, ANCHO_DE_MEDUSA

class Medusa_Verde:
    def __init__(self):
        self.cantidad_de_medusas_verdees_eliminadas = 0
        
        # Cargar y escalar el sprite
        self.sprite_de_medusa_verde_A = pygame.image.load("NPC/MedusaCarpet/Medusa_Verde/Medusa_Verde_sprite/Medusa_verde1.png")
        self.sprite_de_medusa_verde_A = pygame.transform.scale(self.sprite_de_medusa_verde_A, (ANCHO_DE_MEDUSA*.9, ALTO_DE_MEDUSA*1.2))
        self.sprite_de_medusa_verde_B = pygame.image.load("NPC/MedusaCarpet/sprites/medusa2.png")
        self.sprite_de_medusa_verde_B = pygame.transform.scale(self.sprite_de_medusa_verde_B, (ANCHO_DE_MEDUSA*.9, ALTO_DE_MEDUSA*1.2))
        
        # Crear el rectángulo del sprite
        self.medusa_verde_posicion = self.sprite_de_medusa_verde_A.get_rect(center=(-300,-300))
        
        self.hitbox = None
        
        # Crear la hitbox como un rectángulo independiente
        
        self.Destino = None
        self.Destino_Aleatorio = None
        self.Tiempo_sin_electrocutar = 0
        self.medusa_eliminada = False
        self.Tiempo_que_lleva_eliminada_la_medusa = 0
        self.Electrocutando = False
        self.Sonido_de_eliminacion = pygame.mixer.Sound("Musica/Pop.wav")
        
        
    def update_hitbox(self):
        if not self.medusa_eliminada:
            self.hitbox = pygame.Rect(self.medusa_verde_posicion.x, self.medusa_verde_posicion.y, ANCHO_DE_MEDUSA*.45, ALTO_DE_MEDUSA)
            self.hitbox.center = self.medusa_verde_posicion.center
        else: self.hitbox = None

    
    def Randomisar_genero(self):
        self.Genero = random.randint(1,2)
        #Macho
        if self.Genero == 1:
            self.sprite_de_medusa_A = pygame.transform.scale(self.sprite_de_medusa_verde_A, (ANCHO_DE_MEDUSA*.5, ALTO_DE_MEDUSA*2))
            self.sprite_de_medusa_B = pygame.transform.scale(self.sprite_de_medusa_verde_B, (ANCHO_DE_MEDUSA*.5, ALTO_DE_MEDUSA*2))
            # Crear la hitbox como un rectángulo independiente
            self.hitbox = pygame.Rect(self.medusa_verde_posicion.x, self.medusa_verde_posicion.y, ANCHO_DE_MEDUSA*.45, ALTO_DE_MEDUSA)
            # Mover la hitbox junto con la medusa
            self.hitbox.center = self.medusa_verde_posicion.center        
        #Embra
        elif self.Genero == 2:
            self.sprite_de_medusa_A = pygame.transform.scale(self.sprite_de_medusa_verde_A, (ANCHO_DE_MEDUSA*.5, ALTO_DE_MEDUSA*3))
            self.sprite_de_medusa_B = pygame.transform.scale(self.sprite_de_medusa_verde_B, (ANCHO_DE_MEDUSA*.5, ALTO_DE_MEDUSA*3))
            # Crear la hitbox como un rectángulo independiente
            self.hitbox = pygame.Rect(self.medusa_verde_posicion.x, self.medusa_verde_posicion.y, ANCHO_DE_MEDUSA*.45, ALTO_DE_MEDUSA)
            # Mover la hitbox junto con la medusa
            self.hitbox.center = self.medusa_verde_posicion.center

    
    def Randomisar_Spawn_poin(self):
        self.Spawn_poin = random.randint(3,3)
        if self.Spawn_poin == 1:
            self.medusa_posicion = self.sprite_de_medusa_verde_A.get_rect(center=(565, 160))
        if self.Spawn_poin == 2:
            self.medusa_posicion = self.sprite_de_medusa_verde_A.get_rect(center=(515, 15))
        if self.Spawn_poin == 3:
            self.medusa_posicion = self.sprite_de_medusa_verde_A.get_rect(center=(-184, 160))
        if self.Spawn_poin == 4:
            self.medusa_posicion = self.sprite_de_medusa_verde_A.get_rect(center=(-184, 40))
                                     
                
    def mover_medusa(self, Velocidad, Destino_X, Destino_Y, Total_de_medusas_eliminadas, posicion_x_de_jugador, posicion_y_de_jugador):
        if Total_de_medusas_eliminadas < 100:
            if self.Electrocutando == False:
                self.Destino = (Destino_X, Destino_Y)
                
                if self.Destino != self.medusa_verde_posicion.topleft:
                    if self.medusa_verde_posicion.x < Destino_X:
                        self.medusa_verde_posicion.x += Velocidad
                    elif self.medusa_verde_posicion.x > Destino_X:
                        self.medusa_verde_posicion.x -= Velocidad
                        
                    if self.medusa_verde_posicion.y < Destino_Y:
                        self.medusa_verde_posicion.y += Velocidad
                    elif self.medusa_verde_posicion.y > Destino_Y:
                        self.medusa_verde_posicion.y -= Velocidad
        else:
            if self.Electrocutando == False:
                self.Destino = (Destino_X, Destino_Y)
                
                if self.Destino != self.medusa_verde_posicion.topleft:
                    if self.medusa_verde_posicion.x < Destino_X:
                        self.medusa_verde_posicion.x += Velocidad
                    elif self.medusa_verde_posicion.x > Destino_X:
                        self.medusa_verde_posicion.x -= Velocidad
                        
                    if self.medusa_verde_posicion.y < Destino_Y:
                        self.medusa_verde_posicion.y += Velocidad
                    elif self.medusa_verde_posicion.y > Destino_Y:
                        self.medusa_verde_posicion.y -= Velocidad
            else:
                if self.Electrocutando == True:
                    if posicion_x_de_jugador < self.medusa_verde_posicion.x:
                        self.medusa_verde_posicion.x -= Velocidad
                    elif posicion_x_de_jugador > self.medusa_verde_posicion.x:
                            self.medusa_verde_posicion.x += Velocidad
                    
                    if posicion_y_de_jugador < self.medusa_verde_posicion.y:
                        self.medusa_verde_posicion.y -= Velocidad
                    elif posicion_y_de_jugador > self.medusa_verde_posicion.y:
                        self.medusa_verde_posicion.y += Velocidad
                
    def mover_medusa_verde_aleatoriamente(self, Velocidad, Limite_Norte, Limite_Sur, Limite_Este, Limite_Oeste, Total_de_medusas_eliminadas, posicion_x_de_jugador, posicion_y_de_jugador):
        if Total_de_medusas_eliminadas >= 30:
            if self.Destino_Aleatorio is None or (self.hitbox and self.hitbox.collidepoint(self.Destino_Aleatorio)):
                self.Destino_X_Aleatorio = random.randint(Limite_Oeste, Limite_Este)
                self.Destino_Y_Aleatorio = random.randint(Limite_Norte, Limite_Sur)
                self.Destino_Aleatorio = (self.Destino_X_Aleatorio, self.Destino_Y_Aleatorio)
            
            self.mover_medusa(Velocidad, self.Destino_X_Aleatorio, self.Destino_Y_Aleatorio, Total_de_medusas_eliminadas, posicion_x_de_jugador, posicion_y_de_jugador)
        
    def check_collision(self, keys, other_rect, Limite_Norte, Limite_Sur, Limite_Este, Limite_Oeste,Total_de_medusas_eliminadas, evento_1):
        if self.hitbox and self.hitbox.colliderect(other_rect) and evento_1 == False:
            if (keys in [pygame.K_SPACE, pygame.K_KP_0]) and not self.Electrocutando:
                    self.cantidad_de_medusas_verdees_eliminadas +=1            
                    self.medusa_eliminada = True
                    self.Sonido_de_eliminacion.play(1)
                    
            elif self.Electrocutando == True and evento_1 == False:
                if (keys in [pygame.K_d, pygame.K_RIGHT]) and self.medusa_verde_posicion.x < Limite_Este:
                    self.medusa_verde_posicion.x += 25
                
                elif (keys in [pygame.K_a, pygame.K_LEFT]) and self.medusa_verde_posicion.x > Limite_Oeste:
                    self.medusa_verde_posicion.x -= 25                
                
                if (keys in [pygame.K_s, pygame.K_DOWN]) and self.medusa_verde_posicion.y > Limite_Norte:
                    self.medusa_verde_posicion.y += 25
                
                elif (keys in [pygame.K_w, pygame.K_UP])and self.medusa_verde_posicion.y < Limite_Sur:
                    self.medusa_verde_posicion.y -= 25 
                else: return
            
                    
    def Ataque_de_medusa(self, Total_de_medusas_eliminadas, Jugador):
        if Total_de_medusas_eliminadas < 100:
            if self.medusa_eliminada == False:       
                if self.Tiempo_sin_electrocutar < 1000 and self.Electrocutando == False:
                    self.Tiempo_sin_electrocutar += 1
            
                elif self.Tiempo_sin_electrocutar <= 1000:
                    self.Electrocutando = True
                    self.Tiempo_sin_electrocutar -= 1
                    if self.Tiempo_sin_electrocutar == 0:
                        self.Electrocutando = False
        else:
            if self.medusa_eliminada == False:       
                if self.Tiempo_sin_electrocutar < 1000 and self.Electrocutando == False:
                    self.Tiempo_sin_electrocutar += 1
                elif self.Tiempo_sin_electrocutar >= 1000:    
                    self.Electrocutando = True
                    if self.hitbox.colliderect(Jugador.hitbox) or self.hitbox.colliderect(Jugador.Cabeza_hitbox):
                        self.Electrocutando = False
                        self.Tiempo_sin_electrocutar = 0
                

    def dibujar_medusa_verde(self, keys, pantalla, Total_de_medusas_eliminadas, opciones_de_administrador_activadas):
            if Total_de_medusas_eliminadas >= 30:
                if self.medusa_eliminada == False:       
                    self.update_hitbox()
                    #Dibujar sprite de medusa corespondiente
                    if self.Electrocutando == False:
                        pantalla.blit(self.sprite_de_medusa_verde_A, self.medusa_verde_posicion)                
                    else: 
                        pantalla.blit(self.sprite_de_medusa_verde_B, self.medusa_verde_posicion)                
                
                if keys[pygame.K_F3] and opciones_de_administrador_activadas == True:
                    pygame.draw.rect(pantalla, (0, 0, 225), self.hitbox, 2)  # Dibuja la hitbox para visualizarla                  
                    
            else:
                self.medusa_verde_posicion.x = 1000
                self.Tiempo_que_lleva_eliminada_la_medusa += 1
                if self.Tiempo_que_lleva_eliminada_la_medusa >= 250:
                    self.Tiempo_que_lleva_eliminada_la_medusa = 0
                    self.Randomisar_Spawn_poin()
                    self.Randomisar_genero()
                    self.hitbox.center = self.medusa_verde_posicion.center
                    self.medusa_eliminada = False
