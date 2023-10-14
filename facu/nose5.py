# ESTRUCTURA EN PYGAME:
# pygame_05_mov_x_det_grav:


# IMPORTAMOS LAS FUNCIONES de pygame, sys y config.
import pygame
from sys import exit
from config import *



# INICIALIZAR LOS MODULOS DE PYGAME:
pygame.init()
# CREA UNA INSTANCIA DE UN OBJETO DE TIPO RELOJ PARA CONTROLAR AL LA VELOCIDAD DEL BUCLE PRINCIPAL
clock = pygame.time.Clock()

gravedad_x = True #bandera de subida o caida del block

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


    if gravedad_x == True:
    # MOVIMIENTO LATERAL BLOCK CON DETENCION EN EL LATERAL DERECHO DE LA PANTALLA

        if block.right <= width:  # mientras sea menor o igual al ancho
                                    # en cada iteracion aumenta el left
            block.left += SPEED # left es la coordenada X || +X derecha, -X izquierda || +Y baja, -Y sube # left es la coordenada x 
  
    
    else:
        # MOVIMIENTO LATERAL DEL BLOCK CON DETENCION EN EL LATERAL IZQUIERDO DE LA PANTALLA
        if block.left >= 0: # mientras que el left sea mayor o igual 
            block.right -= SPEED # en cada iteracion decrementa la X por lo tanto se mueve a la izquierda




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