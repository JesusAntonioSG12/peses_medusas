def Dibujar_entidades(pez, medusa, medusa_azul, medusa_verde, medusa_morada, rey_medusa, burbuja, corazon, fondo, keys, Total_de_medusas_eliminadas, opciones_de_administrador_activadas):    
        # Dibuja las medusas       
        medusa.dibujar_medusa(keys, fondo, opciones_de_administrador_activadas)  
        medusa_azul.dibujar_medusa_azul(keys, fondo, Total_de_medusas_eliminadas, opciones_de_administrador_activadas)
        medusa_verde.dibujar_medusa_verde(keys, fondo, Total_de_medusas_eliminadas, opciones_de_administrador_activadas)
        medusa_morada.dibujar_medusa_morada(keys, fondo, Total_de_medusas_eliminadas, opciones_de_administrador_activadas)
        rey_medusa.dibujar_rey_medusa(keys, fondo, Total_de_medusas_eliminadas, opciones_de_administrador_activadas)
        
        # Dibujar objetos
        burbuja.Dibujar_burbuja(fondo, keys, Total_de_medusas_eliminadas, opciones_de_administrador_activadas, pez.Vida) 
        #mostrar jugador
        pez.dibujar_jugador(fondo, keys, opciones_de_administrador_activadas)
        # mostrar la vida
        corazon.Mostrar_vida(fondo, pez.Vida)
        