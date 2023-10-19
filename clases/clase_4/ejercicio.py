import pygame

pygame.init()
BLANCO = (255,255,255)
ROJO= (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
NEGRO = (0,0,0)

h = 800
w = 800
ventana = pygame.display.set_mode((w,h), pygame.RESIZABLE)
pygame.display.set_caption("ejercicio clase 4")
screen = pygame.display.get_surface()
fondo = pygame.image.load("clase_4\website.jpg")

messi = {'nombre': "Lionesl Andres Messi", 'edad': 36, 'imagen': "clase_4\messi-argentine-2.jpg"}
di_maria = {'nombre': "Ángel Fabián Di María", 'edad': 35, 'imagen': "clase_4\dimaria.jpg"}
aguero = {'nombre':"Sergio Leonel Agüero del Castillo", 'edad': 35, 'imagen':"clase_4\kun.jpg"}


lista_personas = [messi, di_maria, aguero]

fuente = pygame.font.SysFont("Arial", 30)

flag = True
while flag:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            exit()
    w = screen.get_width()
    h = screen.get_height()
    fondo = pygame.transform.scale(fondo, (w, h))
    screen.blit(fondo, (0, 0))
    y = 50
    for persona in lista_personas:
        nombre = persona['nombre']
        edad = persona['edad']
        foto = persona['imagen']
        x = 50
        for dato in persona:
             if dato == "imagen":
                 imagen = pygame.image.load(persona[dato])
                 imagen = pygame.transform.scale(imagen, (200,200))
                 ventana.blit(imagen,(x,y))
             else:
                 texto = fuente.render(f"{persona[dato]}", True,ROJO )
                 ventana.blit(texto,(x,y))
             x += 400
        y += 200

            




    pygame.display.update()
            
        
            
        

pygame.quit()