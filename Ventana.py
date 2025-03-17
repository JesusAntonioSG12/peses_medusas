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

opciones_de_administrador_activadas = False

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

# Guardar y cargar el juego al iniciar
Partida_guardada = json.load(open('savefile.json', 'r')) if "savefile.json" else {"Total_de_medusas_eliminadas": 0}
# Crea una instancia de la clase Jugador y las clases Medusas
medusa = Medusa()
medusa_azul = Medusa_Azul()
medusa_verde = Medusa_Verde()
medusa_morada = Medusa_Morada()
rey_medusa = Rey_Medusa()

pez = Jugador(1, Partida_guardada["Vida_del_jugador"])

# Crear instancia de las clases de los objetos
corazon = Corazon(pez.Vida)
burbuja = Burbuja()

modo_pausa = False

def handle_events():
    global modo_pausa
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_game({"Total_de_medusas_eliminadas": get_total_medusas(), "Vida_del_jugador": pez.Vida}, 'savefile.json')
            
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE:
                modo_pausa = not modo_pausa
                pygame.mixer.music.pause() if modo_pausa else pygame.mixer.music.unpause()
                
        # Pasar evento a check_collision para asegurar que solo ocurre una vez por pulsación
            if event.key in [pygame.K_SPACE, pygame.K_KP_0]:
                Checar_coliciones_de_entidades(pez, medusa, medusa_azul, medusa_verde, medusa_morada, rey_medusa, burbuja, event.key, get_total_medusas(), fondo)

def update_game():
    if not modo_pausa:
        # Verifica si get_total_medusas() alcanza un valor específico y cambia el audio
        if get_total_medusas() >= 100:  # Cambia "100" por el número deseado
            pygame.mixer.music.load("Musica/audio_jefe1.wav")
            pygame.mixer.music.play(-1)
        
        Checar_coliciones_de_entidades(pez, medusa, medusa_azul, medusa_verde, medusa_morada, rey_medusa, burbuja, pygame.key.get_pressed(), get_total_medusas(), fondo)
        Mover_entidades(pez, medusa, medusa_azul, medusa_verde, medusa_morada, rey_medusa, burbuja, pygame.key.get_pressed(), get_total_medusas())
        Ataque_de_NPCS(medusa, medusa_azul, medusa_verde, medusa_morada, rey_medusa, pez, get_total_medusas())
        Checar_vida_de_jugadores(pez)

        
def render_game():
    fondo.blit(fondo_imagen_1, (0, 0))
    Dibujar_entidades(pez, medusa, medusa_azul, medusa_verde, medusa_morada, rey_medusa, burbuja, corazon, fondo, pygame.key.get_pressed(), get_total_medusas(), opciones_de_administrador_activadas)
    pygame.display.update()
    
def get_total_medusas():
    return medusa.cantidad_de_medusas_eliminadas + medusa_azul.cantidad_de_medusas_azules_eliminadas + medusa_verde.cantidad_de_medusas_verdes_eliminadas + medusa_morada.cantidad_de_medusas_moradas_eliminadas + Partida_guardada["Total_de_medusas_eliminadas"]

# Función para guardar el estado del juego
def save_game(data, filename):
    json.dump(data, open(filename, 'w'))
    

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


def main():
    while True:
        get_total_medusas()
        pygame.time.set_timer(pygame.USEREVENT, 100)
        handle_events()
        if not modo_pausa:
            update_game()
            render_game()
        else:
            fondo.blit(fondo_pausa_1, (0, 0))
            pygame.display.update()
        
        if pez.Vida <= 0:
            json.dump({"Total_de_medusas_eliminadas": 0,"Vida_del_jugador": 5}, open('savefile.json', 'w'))

            if pez.posicion_de_jugador.y <= 1000:
                pez.posicion_de_jugador.y += 2 
            else:
                pygame.quit()
                sys.exit()
Ventana_de_inicio(fondo_imagen_de_inicio, fondo)
main()
