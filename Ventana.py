import pygame
import sys
import json
# importar funciones de pantalla
from VentanaCarpet.Funciones.Cargando import Cargando
from VentanaCarpet.Funciones.Generar_titulo import generar_titulo
from VentanaCarpet.Funciones.Generar_icono_de_esquina import generar_icono_de_esquina
from VentanaCarpet.Funciones.Ventana_de_inicio import Ventana_de_inicio
# importar funciones de entidades
from VentanaCarpet.Funciones.Dibujar_entidades import Dibujar_entidades
from VentanaCarpet.Funciones.Mover_entidades import Mover_entidades
from VentanaCarpet.Funciones.Checar_coliciones_de_entidades import Checar_coliciones_de_entidades
from VentanaCarpet.Funciones.Ataque_de_NPCS import Ataque_de_NPCS
from VentanaCarpet.Funciones.Checar_vida_de_jugadores import Checar_vida_de_jugadores
# importar clases
from PezCarpet.Pez import Jugador
from NPC.MedusaCarpet.Medusa_normal.Medusa import Medusa
from NPC.MedusaCarpet.Medusa_Azul.Medusa_azul import Medusa_Azul
from NPC.MedusaCarpet.Medusa_Verde.Medusa_verde import Medusa_Verde
from NPC.MedusaCarpet.Medusda_morada.Medusa_Morada import Medusa_Morada
from NPC.Rey_medusaCarpet.Rey_Medusas import Rey_Medusa
from Objetos.CorasonesCarpet.Corason import Corazon
from Objetos.BurbujaCarpet.Burbuja import Burbuja
# importar constantes
from VentanaCarpet import Constantes_de_pantalla

opciones_de_administrador_activadas = True

pygame.init()

# Configuración de la ventana (No redimensionable)
fondo = pygame.display.set_mode((Constantes_de_pantalla.ANCHO_DE_PANTALLA, Constantes_de_pantalla.ALTO_DE_PANTALLA))

# Carga la imagen de fondo y ajusta su tamaño al de la ventana
fondo_imagen_de_inicio = pygame.image.load("VentanaCarpet/imagenes/Pantalla_De_Introduccion.png")
fondo_imagen_de_inicio = pygame.transform.scale(fondo_imagen_de_inicio, (Constantes_de_pantalla.ANCHO_DE_PANTALLA, Constantes_de_pantalla.ALTO_DE_PANTALLA))
fondo_imagen_1 = pygame.image.load("VentanaCarpet/imagenes/fondo.png")
fondo_imagen_1 = pygame.transform.scale(fondo_imagen_1, (Constantes_de_pantalla.ANCHO_DE_PANTALLA, Constantes_de_pantalla.ALTO_DE_PANTALLA))
fondo_pausa_1 = pygame.image.load("VentanaCarpet/imagenes/fondo_pausa1.PNG")
fondo_pausa_1 = pygame.transform.scale(fondo_pausa_1, (Constantes_de_pantalla.ANCHO_DE_PANTALLA, Constantes_de_pantalla.ALTO_DE_PANTALLA))

# Crea una instancia de la clase Jugador y las clases Medusas
medusa = Medusa()
medusa_azul = Medusa_Azul()
medusa_verde = Medusa_Verde()
medusa_morada = Medusa_Morada()
rey_medusa = Rey_Medusa()

pez = Jugador(1)
# Crear instancia de las clases de los objetos
corazon = Corazon(pez.Vida)
burbuja = Burbuja()

# Función para guardar el estado del juego
def save_game(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

# Función para cargar el estado del juego
def load_game(filename):
    try:
        with open(filename, 'r') as file:
            Partida_guardada = json.load(file)
            return Partida_guardada
    except FileNotFoundError:
        return {"Total_de_medusas_eliminadas": 0}

# Función para borrar el estado del juego
def borrar_partida(data, filename):
    data = {"Total_de_medusas_eliminadas": 0}
    with open(filename, 'w') as file:
        json.dump(data, file)

# Configura la ventana (imágenes y sonidos)
generar_icono_de_esquina()
generar_titulo(1, 100, 25, 14)
Cargando(3.5, Constantes_de_pantalla.ANCHO_DE_PANTALLA, Constantes_de_pantalla.ALTO_DE_PANTALLA)
sonido_fondo_1 = pygame.mixer.Sound("Musica/Ocean_Wave.wav")
sonido_fondo_2 = pygame.mixer.Sound("Musica/Tropical_Birds.wav")
sonido_fondo_1.play(-1)
sonido_fondo_2.play(-1)
pygame.mixer.music.load("Musica/audio1.wav")
pygame.mixer.music.play(-1)

# Guardar y cargar el juego al iniciar
Partida_guardada = load_game('savefile.json')
def main():
    modo_pausa = False
    while True:
        Total_de_medusas_eliminadas = (
        medusa.cantidad_de_medusas_eliminadas +
        medusa_azul.cantidad_de_medusas_azules_eliminadas +
        medusa_verde.cantidad_de_medusas_verdees_eliminadas +
        medusa_morada.cantidad_de_medusas_moradas_eliminadas 
        #+ 50
)
        keys = pygame.key.get_pressed()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_game({"Total_de_medusas_eliminadas": Total_de_medusas_eliminadas}, 'savefile.json')
                pygame.quit()
                sys.exit()
            elif keys[pygame.K_ESCAPE]:
                if not modo_pausa:
                    modo_pausa = True
                    pygame.mixer.music.pause()
                    save_game({"Total_de_medusas_eliminadas": Total_de_medusas_eliminadas}, 'savefile.json')
                else:
                    modo_pausa = False
                    pygame.mixer.music.unpause()
            
        if not modo_pausa:
            # Dibuja la imagen de fondo y entidades
            fondo.blit(fondo_imagen_1, (0, 0))
            Dibujar_entidades(pez, medusa, medusa_azul, medusa_verde, medusa_morada, rey_medusa, burbuja, corazon, fondo, keys, Total_de_medusas_eliminadas, opciones_de_administrador_activadas)
            # Dar comportamiento, coliciones y checar vida de entidades
            Checar_coliciones_de_entidades(pez, medusa, medusa_azul, medusa_verde, medusa_morada, rey_medusa, burbuja, keys, Total_de_medusas_eliminadas, fondo)
            
            Mover_entidades(pez, medusa, medusa_azul, medusa_verde, medusa_morada, rey_medusa, burbuja, keys, Total_de_medusas_eliminadas)

            Ataque_de_NPCS(medusa, medusa_azul, medusa_verde, medusa_morada, rey_medusa, pez, Total_de_medusas_eliminadas)

            Checar_vida_de_jugadores(pez)

            # Actualiza la pantalla
            pygame.display.update()            
            # Fin del juego
            if rey_medusa.Vida <= 0:
                if rey_medusa.rey_medusa_posicion.y <= 2500:
                    rey_medusa.rey_medusa_posicion.y += 2
                else:
                    return False
        else:
            fondo.blit(fondo_pausa_1, (0, 0))
            # Actualiza la pantalla
            pygame.display.update()

        # No guardar la información si el jugador muere
        if pez.Vida <= 0:
            borrar_partida({"Total_de_medusas_eliminadas": 0}, 'savefile.json')
            pygame.quit()
            sys.exit()

Ventana_de_inicio(fondo_imagen_de_inicio, fondo)
main()
