from VentanaCarpet import Constantes_de_pantalla

def Checar_coliciones_de_entidades(pez, medusa, medusa_azul, medusa_verde, medusa_morada, rey_medusa, burbuja, keys, Total_de_medusas_eliminadas, pantalla):       
        
        # Verifica la colisión entre el jugador y la medusa
        medusa.check_collision(keys, pez.Cabeza_hitbox, pez.hitbox, Constantes_de_pantalla.LIMITE_NORTE, Constantes_de_pantalla.LIMITE_SUR, Constantes_de_pantalla.LIMITE_ESTE, Constantes_de_pantalla.LIMITE_OESTE, pez.Reciviendo_daño)
        medusa_azul.check_collision(keys, pez.Cabeza_hitbox, Constantes_de_pantalla.LIMITE_NORTE, Constantes_de_pantalla.LIMITE_SUR, Constantes_de_pantalla.LIMITE_ESTE, Constantes_de_pantalla.LIMITE_OESTE, Total_de_medusas_eliminadas, pez.Reciviendo_daño)
        medusa_verde.check_collision(keys, pez.Cabeza_hitbox, Constantes_de_pantalla.LIMITE_NORTE, Constantes_de_pantalla.LIMITE_SUR, Constantes_de_pantalla.LIMITE_ESTE, Constantes_de_pantalla.LIMITE_OESTE, Total_de_medusas_eliminadas, pez.Reciviendo_daño)
        medusa_morada.check_collision(keys, pez.Cabeza_hitbox, Constantes_de_pantalla.LIMITE_NORTE, Constantes_de_pantalla.LIMITE_SUR, Constantes_de_pantalla.LIMITE_ESTE, Constantes_de_pantalla.LIMITE_OESTE, pez.Reciviendo_daño, Total_de_medusas_eliminadas)
        rey_medusa.check_collision(keys, pez.Cabeza_hitbox, Constantes_de_pantalla.LIMITE_NORTE, Constantes_de_pantalla.LIMITE_SUR, Constantes_de_pantalla.LIMITE_ESTE, Constantes_de_pantalla.LIMITE_OESTE, pez.Reciviendo_daño, Total_de_medusas_eliminadas)
        
        pez.check_collision(keys, Total_de_medusas_eliminadas, medusa.hitbox, medusa.Electrocutando, medusa_azul.hitbox, medusa_azul.Electrocutando, medusa_verde.hitbox, medusa_verde.Electrocutando, medusa_morada.hitbox, medusa_morada.Electrocutando, rey_medusa.hitbox, rey_medusa.Electrocutando, burbuja.hitbox, burbuja.tipo_de_burbuja)
        burbuja.check_collision(Total_de_medusas_eliminadas, pez.Vida, pez.hitbox, pez.Cabeza_hitbox, keys)
