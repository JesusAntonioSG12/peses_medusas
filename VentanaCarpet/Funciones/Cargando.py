import pygame
import random
import time
from VentanaCarpet.Constantes_de_pantalla import ALTO_DE_PANTALLA, ANCHO_DE_PANTALLA
def Cargando(Tiempo_de_espera_en_total, escala_x, escala_y):
    pygame.init()
    fondo = pygame.display.set_mode((ANCHO_DE_PANTALLA, ALTO_DE_PANTALLA))
    
    # Carga las imágenes (asegúrate de que las rutas sean correctas)
    Cargando_imagenes = [pygame.image.load(f"VentanaCarpet/sprites/Imagenes_Cargando/carga{i}.png") for i in range(1, 19)]
    
    # Calcula el tiempo de espera para cada imagen
    tiempo_por_imagen = Tiempo_de_espera_en_total / len(Cargando_imagenes)
    
    for imagen in Cargando_imagenes:
        imagen_escala = pygame.transform.scale(imagen, (int(escala_x), int(escala_y)))
        fondo.blit(imagen_escala, (0, 0))
        pygame.display.flip()  # Actualiza la pantalla
        time.sleep(tiempo_por_imagen)