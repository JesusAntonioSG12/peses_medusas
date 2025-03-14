import pygame

def Ventana_de_inicio(fondo_imagen_de_inicio, fondo):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        keys = pygame.key.get_pressed()
        
        fondo.blit(fondo_imagen_de_inicio, (0, 0))
        pygame.display.flip()
        
        if keys[pygame.K_SPACE]:
            return False

        