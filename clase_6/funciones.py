import pygame

#CIRCULO    
def calcular_area_circulo(dimensiones:float):
    area = 3.14 * dimensiones ** 2
    perimetro = 3.14 * 2 * dimensiones
    mensaje = f"area: {area} perimetro: {perimetro}"
    return mensaje

def dibujar_circulo(figura:dict, ventana):
    dimensiones = figura['dimensiones']
    posicion_inicial = figura['posicion']
    color = figura['color']
    return pygame.draw.circle(ventana,color,posicion_inicial,dimensiones)

#CUADRADO/RECTANGULO
def calcular_area_rect(dimensiones:tuple):
    flag = True
    area = 0
    perimetro = 0
    for dato in dimensiones:
        if flag == True:
            area += dato
            flag = False
        else:
            area = area * dato
        perimetro += dato *2
    mensaje = f"area: {area:} perimetro: {perimetro}"
    return mensaje

def dibujar_rect(figura:dict, ventana):
    dimensiones = figura['dimensiones']
    posicion_inicial = figura['posicion']
    color = figura['color']
    return pygame.draw.rect(ventana,color,(posicion_inicial,dimensiones))


#TRIANGULO
def calcular_area_triangulo(dimensiones:tuple):
    area = 3
    perimetro = 2
    mensaje = f"area: {area} perimetro: {perimetro}"
    return mensaje

def dibujar_triangulo(figura:dict, ventana):
    dimensiones = figura['dimensiones']
    color = figura['color']
    return pygame.draw.polygon(ventana,color,dimensiones)


############################################################

# funciones generales
def mensaje_resultados(figura:dict):
    tipo = figura['type']
    dimensiones = figura['dimensiones']
    match (tipo):
        case "TRIANGULO":
            resultado = calcular_area_triangulo(dimensiones)
        case "RECT":
            resultado = calcular_area_rect(dimensiones)
        case "CIRCULO":
            resultado = calcular_area_circulo(dimensiones)
    return resultado

def dibujar_figura(figura:dict, ventana):
    tipo = figura['type']
    match (tipo):
        case "TRIANGULO":
            dibujo = dibujar_triangulo(figura,ventana)
        case "RECT":
            dibujo = dibujar_rect(figura,ventana)
        case "CIRCULO":
            dibujo = dibujar_circulo(figura, ventana)
    return  dibujo