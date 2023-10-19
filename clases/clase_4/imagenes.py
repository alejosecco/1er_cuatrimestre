import pygame

pygame.init()

ventana = pygame.display.set_mode((800,800))
pygame.display.set_caption("imagenes")

imagen = pygame.image.load("clase_4\messi-argentine-2.jpg")
imagen = pygame.transform.scale(imagen,(200,200))
imagen = pygame.transform.flip(imagen, False, False )
#imagen = pygame.transform.rotate(imagen,(45))
x =  0
flag = True
while flag:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag = False
    
    ventana.blit(imagen, (x, 100))
    x +=220
    if x >= 800:
        x = 0
    pygame.display.update()
pygame.quit()
