import pygame
import time

import pygame.locals
from PezCarpet.Constantes_de_pez import ALTO_DE_PERSONAJE, ANCHO_DE_PERSONAJE

class Jugador:
    def __init__(self, tipo_de_jugador):
        # Cargar sprite
        self.tipo_de_jugador = tipo_de_jugador
        self.Jugador1_imagen_A = pygame.image.load("PezCarpet/PezCarpet_Sprites/regular_fish_sprite/Pez_1.png")
        self.Jugador1_imagen_A = pygame.transform.scale(self.Jugador1_imagen_A, (ANCHO_DE_PERSONAJE * 1.40, ANCHO_DE_PERSONAJE * 1.5))
        self.Jugador1_imagen_B = pygame.image.load("PezCarpet/PezCarpet_Sprites/regular_fish_sprite/Pez_2.png")
        self.Jugador1_imagen_B = pygame.transform.scale(self.Jugador1_imagen_B, (ANCHO_DE_PERSONAJE * 1.40, ANCHO_DE_PERSONAJE * 1.5))
        self.Jugador1_imagen_C = pygame.image.load("PezCarpet/PezCarpet_Sprites/regular_fish_sprite/Pez_3.png")
        self.Jugador1_imagen_C = pygame.transform.scale(self.Jugador1_imagen_C, (ANCHO_DE_PERSONAJE * 1.40, ANCHO_DE_PERSONAJE * 1.5))
        self.Jugador1_imagen_D = pygame.image.load("PezCarpet/PezCarpet_Sprites/regular_fish_sprite/Pez_4.png")
        self.Jugador1_imagen_D = pygame.transform.scale(self.Jugador1_imagen_D, (ANCHO_DE_PERSONAJE * 1.40, ANCHO_DE_PERSONAJE * 1.5))
        
        self.Reciviendo_daño = False              
        self.tiempo_resiviendo_daño = 0
        self.posicion_de_jugador = self.Jugador1_imagen_A.get_rect()
        self.posicion_de_jugador.center = (ANCHO_DE_PERSONAJE + 10, ALTO_DE_PERSONAJE + 10)
        self.velocidad_de_jugador = 1
        self.Vida = 5
        self.mirar_a = "derecha"
        self.sonido_electrocucion_1 = pygame.mixer.Sound("Musica/electrocutando1.wav")
        self.sonido_electrocucion_2 = pygame.mixer.Sound("Musica/electrocutando2.wav")
        self.sonido_electrocucion_3 = pygame.mixer.Sound("Musica/electrocutando3.wav")
        # Crear hitbox y posicionarla
        self.hitbox = pygame.Rect(self.posicion_de_jugador.x, self.posicion_de_jugador.y, ANCHO_DE_PERSONAJE + 20, ALTO_DE_PERSONAJE)
        self.hitbox.center = self.posicion_de_jugador.center
        self.Cabeza_hitbox = pygame.Rect(self.posicion_de_jugador.x + 20, self.posicion_de_jugador.y + 20, ANCHO_DE_PERSONAJE - 30, ALTO_DE_PERSONAJE)
        
    def mover_jugador(self, keys, Limite_Norte, Limite_Sur, Limite_Este, Limite_Oeste):
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            if keys[pygame.K_LSHIFT] and self.Vida > 1:
                self.posicion_de_jugador.x -= self.velocidad_de_jugador * 2 if self.posicion_de_jugador.x > Limite_Oeste else 0
            else:
                self.posicion_de_jugador.x -= self.velocidad_de_jugador if self.posicion_de_jugador.x > Limite_Oeste else 0
            self.mirar_a = "izquierda"
                
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            if keys[pygame.K_LSHIFT] and self.Vida > 1:
                self.posicion_de_jugador.x += self.velocidad_de_jugador * 2 if self.posicion_de_jugador.x < Limite_Este else 0
            else:
                self.posicion_de_jugador.x += self.velocidad_de_jugador if self.posicion_de_jugador.x < Limite_Este else 0
            self.mirar_a = "derecha"
                
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            if keys[pygame.K_LSHIFT] and self.Vida > 1:
                self.posicion_de_jugador.y -= self.velocidad_de_jugador * 2 if self.posicion_de_jugador.y > Limite_Norte else 0
            else:
                self.posicion_de_jugador.y -= self.velocidad_de_jugador if self.posicion_de_jugador.y > Limite_Norte else 0
            
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            if keys[pygame.K_LSHIFT] and self.Vida > 1:
                self.posicion_de_jugador.y += self.velocidad_de_jugador * 2 if self.posicion_de_jugador.y < Limite_Sur else 0
            else:
                self.posicion_de_jugador.y += self.velocidad_de_jugador if self.posicion_de_jugador.y < Limite_Sur else 0

        # Cierre forzado 1 (Escape + shift)
        elif keys[pygame.K_ESCAPE] and keys[pygame.K_LSHIFT]:
            pygame.quit()
      
        self.hitbox.center = self.posicion_de_jugador.center  # mover hitbox         
        if self.mirar_a == "derecha":
            self.Cabeza_hitbox.x = self.posicion_de_jugador.x + 50
        if self.mirar_a == "izquierda":
            self.Cabeza_hitbox.x = self.posicion_de_jugador.x - 1
        self.Cabeza_hitbox.y = self.posicion_de_jugador.y + 20
        
    def aplicar_dano(self, daño_por_aplicar, empuje, keys, tiempo_rsiviendo_daño = 10): 
            self.Vida -= daño_por_aplicar 
            # Empujón lateral
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:    
                self.posicion_de_jugador.x += (empuje * self.velocidad_de_jugador * 2) if keys[pygame.K_LSHIFT] and self.Vida > 1 else (empuje * self.velocidad_de_jugador)
            elif keys[pygame.K_a] or keys[pygame.K_LEFT]: 
                self.posicion_de_jugador.x -= (empuje * self.velocidad_de_jugador * 2) if keys[pygame.K_LSHIFT] and self.Vida > 1 else (empuje * self.velocidad_de_jugador)
            # Empujón vertical
            if keys[pygame.K_w] or keys[pygame.K_UP]:   
                self.posicion_de_jugador.y += (empuje * self.velocidad_de_jugador * 2) if keys[pygame.K_LSHIFT] and self.Vida > 1 else (empuje * self.velocidad_de_jugador)
            elif keys[pygame.K_s] or keys[pygame.K_DOWN]: 
                self.posicion_de_jugador.y += (empuje * self.velocidad_de_jugador * 2) if keys[pygame.K_LSHIFT] and self.Vida > 1 else (empuje * self.velocidad_de_jugador)
            # Empujón adicional si no se presionan teclas de dirección
            else:
                if self.mirar_a == "derecha":
                    self.posicion_de_jugador.x -= (empuje * self.velocidad_de_jugador * 2)
            

            
    def check_collision(self, keys, Total_de_medusas_eliminadas, medusa_hitbox, medusa_electrocutando, medusa_azul_hitbox, medusa_azul_electrocutando, medusa_verde_hitbox, medusa_verde_electrocutando, medusa_morada_hitbox, medusa_morada_electrocutando, rey_medusa_hitbox, rey_medusa_electrocutando, burbuja_hitbox, Burbuja_tipo):
        if self.Reciviendo_daño == False:
            if medusa_hitbox and ((self.hitbox.colliderect(medusa_hitbox)) or (self.Cabeza_hitbox.colliderect(medusa_hitbox))) and medusa_electrocutando:
                self.aplicar_dano(1, 25, keys, 2)
                self.Reciviendo_daño = True
                self.sonido_electrocucion_1.play(0) 
                self.sonido_electrocucion_3.play(0)  
            elif medusa_azul_hitbox and ((self.hitbox.colliderect(medusa_azul_hitbox)) or (self.Cabeza_hitbox.colliderect(medusa_azul_hitbox))) and medusa_azul_electrocutando and Total_de_medusas_eliminadas >= 5:
                self.aplicar_dano(1, 25, keys)
                self.Reciviendo_daño = True
                self.sonido_electrocucion_1.play(0) 
                self.sonido_electrocucion_3.play(0)
            elif medusa_verde_hitbox and ((self.hitbox.colliderect(medusa_verde_hitbox)) or (self.Cabeza_hitbox.colliderect(medusa_verde_hitbox))) and medusa_verde_electrocutando and Total_de_medusas_eliminadas >= 30:
                self.aplicar_dano(1, 25, keys)
                self.Reciviendo_daño = True
                self.sonido_electrocucion_1.play(0) 
                self.sonido_electrocucion_3.play(0)
            elif medusa_morada_hitbox and ((self.hitbox.colliderect(medusa_morada_hitbox)) or (self.Cabeza_hitbox.colliderect(medusa_morada_hitbox))) and medusa_morada_electrocutando and Total_de_medusas_eliminadas >= 50:
                self.aplicar_dano(1, 25, keys)
                self.sonido_electrocucion_1.play(0) 
                self.sonido_electrocucion_3.play(0)
                self.Reciviendo_daño = True
            elif rey_medusa_hitbox and ((self.hitbox.colliderect(rey_medusa_hitbox)) or (self.Cabeza_hitbox.colliderect(rey_medusa_hitbox))) and rey_medusa_electrocutando and Total_de_medusas_eliminadas >= 50:
                self.aplicar_dano(1, 25, keys)
                self.sonido_electrocucion_1.play(0) 
                self.sonido_electrocucion_3.play(0)
                self.Reciviendo_daño = True
            if ((self.hitbox.colliderect(burbuja_hitbox)) or (self.Cabeza_hitbox.colliderect(burbuja_hitbox))) and Total_de_medusas_eliminadas >= 5 and keys in [pygame.K_SPACE]:   
                if Burbuja_tipo == 2:
                    self.Vida += 1
                elif Burbuja_tipo == 3:
                    self.Vida += 3
                    
        if self.Reciviendo_daño == True:
            if self.tiempo_resiviendo_daño < 500:
                self.tiempo_resiviendo_daño += 1
            else:
                self.Reciviendo_daño = False
                self.tiempo_resiviendo_daño = 0       


    def check_hp(self):
        # Checar que la Vida no se salga de los parametros (menor que 0)
        if self.Vida <= 0:
            self.Vida = 0
            self.Reciviendo_daño = True
            if self.posicion_de_jugador.y <= 1000:
                self.posicion_de_jugador.y += 2           
            else:
                pygame.quit()     
        # Checar que la Vida no se salga de los parametros (mayor que 5)
        elif self.Vida > 5:
            self.Vida = 5
        else:
            # Checar que la Vida no sea decimal
            self.Vida = round(self.Vida)

            
            
    def dibujar_jugador(self, pantalla, keys, opciones_de_administrador_activadas):
        if self.tipo_de_jugador == 1:
            if self.Reciviendo_daño == False:
                if self.mirar_a == "derecha":
                    pantalla.blit(self.Jugador1_imagen_A, self.posicion_de_jugador)
                elif self.mirar_a == "izquierda":
                    pantalla.blit(self.Jugador1_imagen_B, self.posicion_de_jugador)
            elif self.Reciviendo_daño == True:
                if self.mirar_a == "derecha":
                    pantalla.blit(self.Jugador1_imagen_C, self.posicion_de_jugador)
                elif self.mirar_a == "izquierda":
                    pantalla.blit(self.Jugador1_imagen_D, self.posicion_de_jugador)
        # Dibuja las hitboxes (rectángulos) de las colisiones
        if keys[pygame.K_F3] and opciones_de_administrador_activadas == True:
            pygame.draw.rect(pantalla, (255, 0, 0), self.hitbox, 2)  # Rojo para el jugador
            pygame.draw.rect(pantalla, (255, 0, 0), self.Cabeza_hitbox, 3)
