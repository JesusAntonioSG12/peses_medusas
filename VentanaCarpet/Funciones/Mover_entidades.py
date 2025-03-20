from VentanaCarpet import Constantes_de_pantalla

def Mover_entidades(pez, medusa, medusa_azul, medusa_verde, medusa_morada, rey_medusa, burbuja, keys, Total_de_medusas_eliminadas):
        # Mover jugadores
        pez.mover_jugador(keys, Constantes_de_pantalla.LIMITE_NORTE, Constantes_de_pantalla.LIMITE_SUR, Constantes_de_pantalla.LIMITE_ESTE, Constantes_de_pantalla.LIMITE_OESTE) 
        
        # Llama al método para mover la medusa aleatoriamente
        if rey_medusa.Vida > 0:
                medusa.mover_medusa_aleatoriamente(1, Constantes_de_pantalla.LIMITE_NORTE, Constantes_de_pantalla.LIMITE_SUR, Constantes_de_pantalla.LIMITE_ESTE, Constantes_de_pantalla.LIMITE_OESTE, Total_de_medusas_eliminadas, pez.posicion_de_jugador.x, pez.posicion_de_jugador.y)
                medusa_azul.mover_medusa_azul_aleatoriamente(1.25, Constantes_de_pantalla.LIMITE_NORTE, Constantes_de_pantalla.LIMITE_SUR, Constantes_de_pantalla.LIMITE_ESTE, Constantes_de_pantalla.LIMITE_OESTE, Total_de_medusas_eliminadas, pez.posicion_de_jugador.x, pez.posicion_de_jugador.y)
                medusa_verde.mover_medusa_verde_aleatoriamente(1.50, Constantes_de_pantalla.LIMITE_NORTE, Constantes_de_pantalla.LIMITE_SUR, Constantes_de_pantalla.LIMITE_ESTE, Constantes_de_pantalla.LIMITE_OESTE, Total_de_medusas_eliminadas, pez.posicion_de_jugador.x, pez.posicion_de_jugador.y)
                medusa_morada.mover_medusa_morada_aleatoriamente(1.25, Constantes_de_pantalla.LIMITE_NORTE, Constantes_de_pantalla.LIMITE_SUR, Constantes_de_pantalla.LIMITE_ESTE, Constantes_de_pantalla.LIMITE_OESTE, Total_de_medusas_eliminadas, pez.posicion_de_jugador.x, pez.posicion_de_jugador.y)
                rey_medusa.mover_rey_medusa_aleatoriamente(1.25, Constantes_de_pantalla.LIMITE_NORTE, Constantes_de_pantalla.LIMITE_SUR, Constantes_de_pantalla.LIMITE_ESTE, Constantes_de_pantalla.LIMITE_OESTE, Total_de_medusas_eliminadas, pez.posicion_de_jugador.x, pez.posicion_de_jugador.y)
        
        # Mover objetos
        burbuja.Mover_Burbuja()