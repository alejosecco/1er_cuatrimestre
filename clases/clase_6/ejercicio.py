import pygame
from funciones import *

BLANCO = (255,255,255)
ROJO= (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
NEGRO = (0,0,0)
x_datos = 400
y_datos = 600

triangulo = {'type': "TRIANGULO",'dimensiones': ((400,400),(600,400),(400,300)),'posicion': (400,400),'color': BLANCO}
rectangulo = {'type': "RECT",'dimensiones': (280,140),'posicion': (400,400),'color': BLANCO}
cuadrado = {'type': "RECT",'dimensiones': (140,140), 'posicion': (400,400),'color': BLANCO}
circulo = {'type': "CIRCULO",'dimensiones': (70), 'posicion': (400,400),'color': BLANCO}

pygame.init()

w = 800
h = 800
PANTALLA = pygame.display.set_mode((w, h), pygame.RESIZABLE)
pygame.display.set_caption("clase 6")
PANTALLA.fill(NEGRO)

fuente = pygame.font.SysFont("Arial", 30)

flag = True
while flag:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag = False
        # aca se elige la figura 
        figura = circulo
        dibujar_figura(figura,PANTALLA)
        texto = fuente.render(mensaje_resultados(figura), True, BLANCO,VERDE)
        PANTALLA.blit(texto,(x_datos,y_datos))

    pygame.display.update()
pygame.quit()
