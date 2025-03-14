import pygame
import random

def generar_titulo(minimo_de_probabilidad,maximo_de_probabilidad,numero_necesario_para_titulo_especial_1,numero_necesario_para_titulo_especial_2):
    titulo = random.randint(minimo_de_probabilidad,maximo_de_probabilidad)
    if titulo != numero_necesario_para_titulo_especial_1 and titulo != numero_necesario_para_titulo_especial_2:
        pygame.display.set_caption("Peces y Medusas v1.0")
    
    elif titulo == numero_necesario_para_titulo_especial_1:
        pygame.display.set_caption("Medusas y Peces")

    elif titulo == numero_necesario_para_titulo_especial_2:
        pygame.display.set_caption("Ajolotes y más ajolotes")
        icono = pygame.image.load("VentanaCarpet/imagenes/Ajolote.png")
        pygame.display.set_icon(icono)