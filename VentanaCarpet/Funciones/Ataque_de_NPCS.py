def Ataque_de_NPCS(medusa, medusa_azul, medusa_verde, medusa_morada, rey_medusa, Jugador, Total_de_medusas_eliminadas):
    medusa.Ataque_de_medusa()
    medusa_azul.Ataque_de_medusa()
    medusa_verde.Ataque_de_medusa(Total_de_medusas_eliminadas, Jugador)
    medusa_morada.Ataque_de_medusa_morada()
    rey_medusa.Ataque_de_rey_medusa()