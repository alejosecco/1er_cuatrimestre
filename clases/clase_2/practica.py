import pygame

BLANCO = (255,255,255)
ROJO= (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
NEGRO = (0,0,0)

lista_animales = ["perro", "gato","conejo" ]

pygame.init()

ventana  = pygame.display.set_mode((500,500))
pygame.display.set_caption("primer ventana")

#icon = pygame.image.load("")
#pygame.display.set_icon(icon)
ventana.fill(AZUL)

fuente = pygame.font.SysFont("Arial", 30)
texto = fuente.render("hola buenas", True,ROJO,VERDE)

flag = True 
while flag:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag = False
    y = 50
    for animal in lista_animales:
        texto = fuente.render(animal, True,ROJO, VERDE)
        ventana.blit(texto,(50,y))
        y += 70





    #1. Tipo de instrumento que más se operó.
    contador_bonos = 0
    contador_cedear = 0
    contador_mep = 0
    for i in range(len(nombres)):
        instrumento = tipos_inversion[i]
        match instrumento:
            case "BONOS":
                contador_bonos +=1
            case "CEDEAR":
                contador_cedear +=1
            case "MEP":
                contador_mep +=1 

    lista_contadores = [contador_bonos , contador_cedear , contador_mep]



    #2. Cantidad de usuarios que compraron entre 150 y 200 BONOS y que invirtieron más de $50000.
    contador_punto_2 = 0
    for i in range(len(nombres)):
        nombre = nombres[i]
        inversion = montos_dinero[i]
        instrumento = tipos_inversion[i]
        cantidad = cantidad_tipos[i]
        if instrumento == "BONOS" and inversion > 50000 and cantidad >=150 and cantidad <= 200:
            contador_punto_2 += 1

    print(f"los que cumplen lo requerido fueron {contador_punto_2}")

    #3. Nombre y cantidad de instrumentos del usuario que compró BONOS o MEP, que menos dinero invirtió. Puede ser más de uno.
    bandera = False
    monto_menor = 0
    for i in range(len(nombres)):
        nombre = nombres[i]
        inversion = montos_dinero[i]
        instrumento = tipos_inversion[i]
        cantidad = cantidad_tipos[i]
        if instrumento == "BONOS" or instrumento == "MEP":
            if bandera == False or inversion < monto_menor:
                bandera = True
                monto_menor = inversion

    for i in range(len(nombres)):
        inversion = montos_dinero[i]
        if inversion == monto_menor:
            print(f"nombre: {nombres[i]}\t {tipos_inversion[i]}\t cantidad: {cantidad_tipos[i]}")

    #4. Nombre de los usuarios que invirtieron en CEDEAR, cuya inversión supere el monto promedio

    acumulador = 0
    for i in range(len(nombres)):
        inversion = montos_dinero[i]
        acumulador += inversion

    promedio_inversion = acumulador / (len(montos_dinero))
    for i in range(len(tipos_inversion)):
        nombre = nombres[i]
        inversion = montos_dinero[i]
        instrumento = tipos_inversion[i]
        cantidad = cantidad_tipos[i]
        if instrumento == "CEDEAR":
            if inversion > promedio_inversion:
                print(f"{nombre} supera la inversion promedio")

    #5. Porcentaje de usuarios que no invirtieron en MEP, siempre y cuando el monto no supere los $50000.
    contador = 0
    for i in range(len(montos_dinero)):
        instrumento = tipos_inversion[i]
        inversion = montos_dinero[i]
        if instrumento != "MEP" and inversion < 50000:
            contador +=1

    porcentaje = contador * 100 / (len(montos_dinero))
    print(f"fue del {porcentaje}%")

    
    pygame.display.update()
    
pygame.quit()
