# ESTRUCTURA EN PYGAME:
# pygame_01_est:

# 1 Configurar
# 2 Detectar eventos (nos metemos en el while para relevar eventos)
# 3 Actualizar eventos.
# 4 Dibujar la pantalla.
# 5 Actualizar la vista (Mostrar la pantalla en cada iteracion)
# 6 luego volvemos a comenzar
# 7 finalizar
#  *en el caso quit para salir entre el paso 2 y 3, salta al 7

# import sys IMPORTA EL MODULO SYS y para que funcione es sys.exit()
# import pygame
# from sys import exit

# pygame.init() #inicializa modulos, sonido, mouse, teclado, video.

# screen = pygame.display.set_mode((800,600)) #guardamos en la variable screen a lo que retorna la funcion display para poder manipularlo
# #screen es un objeto.
# pygame.display.set_caption("Primer juego") # modigica el titulo de la ventana

# while True:

#     for event in pygame.event.get():
#         print(event)
#         if event.type == pygame.QUIT: # pregunta si el evento es QUIT, para salir. el evento pygame.QUIT equivale a 256, es por eso que figura int
#             pygame.quit() # seria lo opuesto de pygame.init() desconecta el pygame
#             exit()  #o sys.exit() si importamos todo sys, con import sys
#             # salimos del for y del while matando el proceso, como un Ctrl+c


# MISMO CODIGO UTILIZANDO BANDERAS:

# import pygame
# from sys import exit

# screen = pygame.display.set_mode((800,600))
# is_running = True

# pygame.display.set_caption("Primer juego") # modigica el titulo de la ventana

# while is_running:
#     for event in pygame.event.get():
#         print(event)
#         if event.type == pygame.QUIT:
#             is_running = False

# pygame.quit()
##exit() sin el exit seria una mejor opcion ya que no forzamos a terminar el 
# programa sino que dejamos que la aplicacion termine porque realmente se termino el programa

###############################################################################################################

# RGB:
# red, green, blue.
# 1byte = 8 bits = 256 valores
# pantalla columnas 1920 x filas 1080 = 2.073.600 pixeles (un led rgb)
# cada color es un byte 00000000 o 11111111
#     R    G     B
# (0-255,0-255,0-255)
# color rojo seria screen.fill((255,0,0))

import pygame
from sys import exit
from config import *
# INICIALIZAR MODULOS PYGAME
pygame.init()

#CREAMOS UN RELOS CON UNA CLASE .CLOCK
clock = pygame.time.Clock()
#CONFIGURACION PANTALLA PRINCIPAL
#from config import * creamos el archivo config.py y agregamos la lista de colores, luego los importamos desde alla
screen = pygame.display.set_mode((800,600)) #o ((size_screen))
is_running = True
contador = 0
pygame.display.set_caption("Primer juego") # modigica el titulo de la ventana

screen.fill((255,0,0)) #verde screen.fill((0,255,0)) " o lo importamos desde el archivo creado screen.fill(green)"

rect_1 = pygame.Rect(0, 0, 200, 100)
#                    x, y,  w,  h
# la lista / tupla de colores deberia estar en un archivo llamado config.py

# Otra forma de representar un cuadrado es a traves de una tupla pasandole 4 valores (no es un cuadrado)
#
rect_2 = (200, 200, 300, 150) # una tupla es una lista de elementos que solo esta 
#preparada para ser leida y que agrupa a mas de un elemento



FPS = 60

while is_running:
    clock.tick(FPS) # el reloj en este caso maneja las iteraciones por segundo
    #detectar los eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            #actualizar los elementos
    
    contador +=1 # con esto vemos la iteracion del while
   #actualizar los elementos
    print(contador)
    pygame.display.flip()  #la funcion flip actualiza toda la pantalla
   #pygame.display.update() # solo actualiza una parte de la pantalla,sin pasarle parametros se comporta como flip, si se le pasa un rectangulo solo actualiza esa region
    
    #pygame.draw.rect(donde?, color?crect,[borde])
    x_rectangulo = pygame.draw.rect(screen, green, rect_1) # el rect_1 fue construido como rectangulo
    y_tupla = pygame.draw.rect(screen, yellow, rect_2) #el rect_2 fue construido como tupla

pygame.quit()

#CUANDO HABLAMOS DE UNA INSTANCIA, NOS REFERIMOS A UNA CLASE, REPRESENTADA POR UNA VARIABLE.
#NORMALMENTE LAS CLASES TIENEN LA INICIAL EN MAYUSCULA.
# NOS PERMITE FABRICAR OBJETOS DE TIPO CLOCK, (CONTRUCTOR)

    #pygame -->paquete,
    #time--> modulo, 
    #Clock --> una clase que esta dentro del modulo time.

    # clock = pygame.time.Clock()

    #dentro de un modulo se pueden guardar funciones, clases y variables.


# COORDENADAS:
# El punto 0,0 es el extremo superior 
# hablamos de extremo inferior derecho de y,x
# El eje X incrementa de izquierda a derecha
# -x <-----0----->  +x
# El eje Y incrementa de arriba hacia abajo
#           -Y
#            |
#            |     
#            |                         
#            |
#           +Y

#           -Y ___width___|
#            |
#            |
# -X <_0,0._______> +X   _
#            |//////////////////////       |
#            |//zona de pantalla////    height
#            |//////////////////////       |
#           +Y                             -

# width = 800
# height = 600

###############################################################################################################
# EN pygame todo es un cuadrado, al que se le quita parte del mismo para formar un objeto
# Por ejemplo un circulo en realidad es un cuadrado al que se le quita las esquinas

#dos formas de dibujar u rectangulo.
# 1) con un constructor, definimos al rectangulo con top, left, width, height
# react_1 = pygame.Rect()
#--------------------------------------
#                TOP                  |
#                                     |
# lefth                      right    |
#                                     |
#                                     |
#              bottom                 |
#--------------------------------------


#ubicacion
#tamaño

# |----------------------------------------|
# | top left      mid top                  |
# |       ------------------* top right  |
# |       |                   |            |
# | left |  center *         | mid       |
# |       |                   |            |
# |       ------------------*            |
# | left bottom  mid bottom   right bottom |
# |----------------------------------------|

# El punto center tiene una propiedad que es center x, center y (es una tupla)
# Todos los puntos antes mencionados y detallados quedn definidos por el valor


"""
import pygame
from sys import exit
from config import *
pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((800,600))
is_running = True
contador = 0
pygame.display.set_caption("Primer juego")

screen.fill((255,0,0))

rect_1 = pygame.Rect(0, 0, 200, 100)

rect_2 = (200, 200, 300, 150)

FPS = 60

while is_running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            
    contador +=1
    print(contador)

    pygame.display.flip() 
    
    x_rectangulo = pygame.draw.rect(screen, green, rect_1)
    y_tupla = pygame.draw.rect(screen, yellow, rect_2)

pygame.quit()
"""