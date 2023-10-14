# ESTRUCTURA EN PYGAME:
# pygame_06_mov_y_reb_grav:


# RGB:
# red, green, blue.
# 1byte = 8 bits = 256 valores
# pantalla columnas 1920 x filas 1080 = 2.073.600 pixeles (un led rgb)
# cada color es un byte 00000000 o 11111111
#     R    G     B
# (0-255,0-255,0-255)
# color rojo seria screen.fill((255,0,0))







# import pygame
# from sys import exit
# from config import *
# # INICIALIZAR MODULOS PYGAME
# pygame.init()

# #CREAMOS UN RELOS CON UNA CLASE .CLOCK
# clock = pygame.time.Clock()
# #CONFIGURACION PANTALLA PRINCIPAL
# #from config import * creamos el archivo config.py y agregamos la lista de colores, luego los importamos desde alla
# screen = pygame.display.set_mode((800,600)) #o ((size_screen))
# is_running = True
# contador = 0
# pygame.display.set_caption("Primer juego") # modigica el titulo de la ventana

# screen.fill((255,0,0)) #verde screen.fill((0,255,0)) " o lo importamos desde el archivo creado screen.fill(green)"

# rect_1 = pygame.Rect(0, 0, 200, 100)
# print(rect_1.center) #centro del rectangulo 1 da la salida (en coordenada)

# #                    x, y,  w,  h
# # la lista / tupla de colores deberia estar en un archivo llamado config.py

# # Otra forma de representar un cuadrado es a traves de una tupla pasandole 4 valores (no es un cuadrado)
# #
# rect_2 = (200, 200, 300, 150) # una tupla es una lista de elementos que solo esta 
# #preparada para ser leida y que agrupa a mas de un elemento

# FPS = 60

# while is_running:
#     clock.tick(FPS) # el reloj en este caso maneja las iteraciones por segundo
#     #detectar los eventos
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             is_running = False
#             #actualizar los elementos
    
#     contador +=1 # con esto vemos la iteracion del while
#    #actualizar los elementos
#     print(contador)
#     pygame.display.flip()  #la funcion flip actualiza toda la pantalla
#    #pygame.display.update() # solo actualiza una parte de la pantalla,sin pasarle parametros se comporta como flip, si se le pasa un rectangulo solo actualiza esa region
    
#     #pygame.draw.rect(donde?, color?crect,[borde])
#     # x_rectangulo = pygame.draw.rect(screen, green, rect_1) # el rect_1 fue construido como rectangulo
#     # y_tupla = pygame.draw.rect(screen, yellow, rect_2) #el rect_2 fue construido como tupla

# # pygame.draw.rect(donde?, color?, rect, [borde])
# # dibuja rectangulos en surface
#     #pygame.draw.rect(screen, green, rect_1)
#     r = pygame.draw.rect(screen, yellow, (200, 200, 300, 150),24,
#                      border_top_left_radius=40, border_bottom_right_radius=40) #el ultimo numero especifica el borde

#     pygame.draw.rect(screen, red, r, 2)
#     pygame.display.flip()
# pygame.quit()








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

# PROPIEDADES DEL RECTANGULO (tipo objeto):
#       |           \
#       |            \
#       |             \COORDENADAS: (Es un punto, se escriben en tuplas, como las tuplas son inmutables carecen de metodos, es para valores que no tienen que cambiar)
#       |                centro (center x, cente y)        
# VALORES UNICOS:        top Left (coordenada, punto arriba a la izquierda)
#    top                 top right   (coordenada, punto superior derecho )   
#    bottom              bottom left  (coordenada, punto inferior izquierdo)
#    left                bottom right (coordenada, punto inferior derecho )
#    right               mid top (coordenada, punto media arriba)
#    center x            mid bottom (coordenada, punto medio bajo)
#    center y            mid left (coordenada, punto medio de la izquierda)
#    width               midright (coordenada, punto medio de la derecha)
#    height              size (ancho y alto)


#
# rect_1 pygame.Rect(0, 0, 200, 100) # VARIABLE DE TIPO RECTANGULO, OBJETO EN MEMORIA
# print(rect_1.center)  # IMPRIME LA VARIABLE.
#
"""
import pygame
from sys import exit
from config import *
# INICIALIZAR MODULOS PYGAME
pygame.init()

#CREAMOS UN RELOS CON UNA CLASE .CLOCK
clock = pygame.time.Clock()
#CONFIGURACION PANTALLA PRINCIPAL

screen = pygame.display.set_mode((width,height))
is_running = True

pygame.display.set_caption("Primer juego") # modigica el titulo de la ventana

#metodo fill llenar de un color
screen.fill((custom)) #verde screen.fill((0,255,0)) " o lo importamos desde el archivo creado screen.fill(green)"

rect_1 = pygame.Rect(0, 0, 300, 100)
rect_1.center = center_screen

#print(rect_1.center) #centro del rectangulo 1 da la salida (en coordenada)

rect_2 = (200, 200, 300, 150) # una tupla es una lista de elementos que solo esta 


# CREAR NUEVA SUPERFICIE: una calco.
# size: coodenadas, nos pide un tamaño
calco = pygame.Surface((100, 50)) # 100x ancho, 50y de alto
calco.fill(blue)#en memoria lo que hicimos es agarramos una superficie, a donde vamos a pegar la calco azul 

rec_calco = calco.get_rect() #extraemos el rectangulo que tiene la superficie
#cuando tenemos una superficie y queremos obtener el rectangulo donde esta

rec_calco.center = center_screen #posicionar el rectangulo del calculo en el centro de la pantalla

y = 250

while is_running:
    clock.tick(FPS) # el reloj en este caso maneja las iteraciones por segundo

    #detectar los eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
            #actualizar los elementos


    #HACEMOS QUE HAGA PASADAS HACIA ABAJO (CAIDA):
    if y <= height : # desplazar hacia abajo solamente cuando Y sea menor al alto de la pantalla
        y += 1 
    else:
        y = -50
        print (y)

    #HACEMOS BAJAR:
    # if y < height -50 : # desplazar hacia abajo solamente cuando Y sea menor al alto de la pantalla
    #     y += 1 
    # print (y)

    #HACER SUBIR:
    # if y > 0: #hacemos subir al rectangulo hasta la parte superior, donde y es mayor que 0
    #     y -=1
    #     print(y)

    #velocidad = distancia / tiempo


    # DIBUJAMOS LA PANTALLA: cuando componemos una pantalla debemos ir del fondo hacia adelante
    # (primero dibujamos el fondo)

    screen.fill((custom))
    # DIBUJAMOS UN RECTANGULO:
    pygame.draw.rect(screen, blue, (350, y, 100, 50) )
    
    
    # # DIBUJAR UN PIXEL: permite trabajar a nivel de pixeles
    # pantalla = pygame.PixelArray(screen) #cuando temrinamos de pintar los pixeles siempre borrar la variable con del
    # pantalla[200][100] = white
    # del pantalla #borra la variable pantalla, para desbloquearla, de lo contrario tira error
    # # surface:, donde? que seria la pantalla en este caso el screen.
    

    # # DUBUJAR UN CIRCULO:
    # x = pygame.draw.circle(screen, magenta, (300 , 400), 100)
    # # se le pasa, 
    # # surface:, donde? que seria la pantalla en este caso el screen.
    # # color: en este caso el magenta
    # # coordenada: centro de pantalla en este caso lo saca del config
   

    # # DIBUJAR UNA LINEA:
    # pygame.draw.line(screen, blue, (0,0), x.center,2)
    # # surface:, donde? que seria la pantalla en este caso el screen.
    # # color: blue
    # # star_pos: desde donde? tupla, coordenada, el origen
    # # end_pos: hasta donde? tupla o parametro, el destino
    # # width: ancho de linea
    

    # # DIBUJAR UNA ELIPSE:
    # pygame.draw.ellipse(screen,green,(300, 300, 400, 200),10)
    # # surface:, donde? que seria la pantalla en este caso el screen.
    # # color: green
    # # rect: o valor de rectangulo ejemplo coordenada tupla
    # # width: ancho de linea
    

    # # DIBUJAR UN POLIGONO:
    # pygame.draw.polygon(screen,black,[(76, 267),(690, 345),(450,340)],0)
    # # surface:, donde? que seria la pantalla en este caso el screen.
    # # color: black
    # # points: Sequence[coordinate], nos dice una lista de puntos, una tupla a la cual luego ira conectando sus puntos
    # # widtg: ancho
    

    # r = pygame.draw.rect(screen, yellow, rect_1, 24,
    #                border_top_left_radius=40, border_bottom_right_radius=40) #el ultimo numero especifica el borde

    # PEGAR EL SURFACE (metodo blit):
    # screen.blit(calco, rec_calco) #pegamos la calco con el metodo blit (unimoslas sourfaces)
    # source: Surface, seria cual es la superficie que quiero pegar, en este caso la calco
    # dest: como destino una coordenada(coordinate)tupla x e y , o un valor, de rectangulo (rectValue)

    pygame.display.flip()
    
pygame.quit()

"""

###############################################################################################################

# ECTORES DE LA APLICACION:
# IMPORTAMOS LAS FUNCIONES de pygame, sys y config.
import pygame
from sys import exit
from config import *



# INICIALIZAR LOS MODULOS DE PYGAME:
pygame.init()
# CREA UNA INSTANCIA DE UN OBJETO DE TIPO RELOJ PARA CONTROLAR AL LA VELOCIDAD DEL BUCLE PRINCIPAL
clock = pygame.time.Clock()

gravedad = True #bandera de subida o caida del block

# CONFIGURACION DE PANTALLA PRINCIPAL:
screen = pygame.display.set_mode(size_screen)
# PONEMOS UN TITULO EN LA VENTANA
pygame.display.set_caption("Primer Jueguito")


#HACER QUE EL RECTANGULO SE DESPLACE HACIA ABAJO


#COLOCAR BLOQUE DE LOGICA DE  ELEMENTOS A MOSTRAR
block = pygame.Rect(300, 300, 150, 100) #posicion 


# SE CREA UNA VARIABLE is_running, QUE ES LA QUE CONTROLA EL BUCLE PRINCIPAL
is_running = True

# BUCLE PRINCIPAL:
while is_running:
    clock.tick(FPS)
    # MANEJO DE EVENTOS:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            is_running = False


    if gravedad == True:
    # CAIDA DE BLOCK CON DETENCION EN EL INFERIOR DE LA PANTALLA


        if block.bottom <= height:  # mientras sea menor o igual al alto
                                    # en cada iteracion aumenta el top
            block.top += SPEED # top es la coordenada Y || +Y baja, -Y sube # left es la coordenada x || +X derecha, -X izquierda
        else:
            gravedad = False      # gravedad = not gravedad
    
    else:
        # SUBIDA DE BLOCK CON DETENCION EN EL SUPERIOR DE LA PANTALLA
        if block.top >= 0: # mientras que el top sea mayor o igual 
            block.top -= SPEED
        else:
            gravedad = True   # gravedad = not gravedad



    # ACTUALIZAR LOS ELEMENTOS:
    # if y <= height:
    #     y += 1
    # else:
    #     y = -50

    # if y > 0:
    #   y -= 1
    print(300)

    # DIBUJAR LA PANTALLA
    screen.fill(black) #fondo de pantalla
    pygame.draw.rect(screen, blue, block) #dibujamos el block creado

    # ACTUALIZACION DE LA PANTALLA:
    pygame.display.flip()

pygame.quit()

###############################################################################################################