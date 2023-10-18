# import pygame
from funciones import *
from preguntas_respuestas import lista_tematicas
# NEGRO = (0,0,0)

# pygame.init()

# w = 800
# h = 800
# PANTALLA = pygame.display.set_mode((w, h), pygame.RESIZABLE)
# pygame.display.set_caption("100 Argentinos dicen")
# PANTALLA.fill(NEGRO)

# fuente = pygame.font.SysFont("Arial", 30)
# vidas = 3
# puntos = 0
# puntos2 = 0

# flag = True
# while flag:
#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT:
#             flag = False
#     pygame.display.update()
    
# pygame.quit()

vidas = 3
puntos = 0
puntos2 = 0


intentos = 5
while intentos > 0 and vidas > 0:
    print(f"total puntos: {puntos}")
    print(f"vidas restantes: {vidas}")
    puntos_ronda = ronda_juego(lista_tematicas)
    puntos += puntos_ronda
    puntos2 += puntos_ronda
    if puntos2 >= 50:
        vidas +=1
        puntos2 -= 50
    intentos -=1
    if puntos_ronda == 0:
        vidas -=1
premio = obtener_premio(puntos)
print(f"puntos finales: {puntos}\n vidas: {vidas}")
print(f"el premio total es de: ${premio}")
print("termino el juego")


#normalizar respuestas y listas - usar json y hacer lo de resultado funal con csv, con nombre y resultado - 