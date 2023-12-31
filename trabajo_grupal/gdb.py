# Idea del juego:

# El clásico juego de Barassi tiene como tema principal la adivinanza de palabras relacionadas con un tema específico, ya sea “cantantes argentinas”, “actores de hollywood”, “bandas de rock nacional”, entre otros y se le preguntan a 100 argentinos de manera aleatoria y se anotan sus respuestas
# Se elige una pregunta de manera aleatoria sobre una temática y el jugador tiene que elegir una posible respuesta a la pregunta realizada en la que al menos un argentino haya coincidido. Cuantos más argentinos hayan elegido esa respuesta  más puntos tendrá el jugador.
# El juego consta de 5 partidas para llegar al final del juego. Si el jugador acumula el total de 500 ganará el premio mayor de $1000000. En caso de que obtenga menos de ese puntaje se llevará el pozo acumulado que resultará de multiplicar la cantidad de puntos obtenidos por $500. 

# Funcionamiento del juego:

# Selección de temática: Al comienzo de cada partida, el juego elige aleatoriamente una temática. Sobre esa temática se realiza una pregunta.Por ejemplo.

# Temática: Cantantes argentinas
# Pregunta: Cantantes argentinas que tienen menos de 40 años.
# Respuestas posibles: 	
# Lali:		  43 argentinos
# Tini: 	  	  22 argentinos
# Nicki Nicole: 	  20 argentinos
# Maria Becerra:  14 argentinos
# Mercedes Sosa: 1 argentino

# Respuesta: El jugador ingresa su respuesta desde la pantalla (o teclado). Si la respuesta coincide con la elección de algún argentino el jugador puede seguir jugando. Deberá aparecer en pantalla la respuesta correcta junto con la cantidad de argentinos que la eligieron.

# Puntuación: Por cada argentino que eligió la palabra el jugador ganará un punto

# Tiempo: El jugador tiene 60 segundos para elegir una palabra sino perderá su oportunidad.

# Oportunidades:El jugador tiene 3 oportunidades para adivinar al menos una palabra, por cada 50 puntos el jugador ganará una oportunidad extra para seguir jugando..

# Consejo: Al armar el set de datos tener en cuenta como mínimo 5 respuestas diferentes de argentinos, con la cantidad de argentinos que eligieron esa respuesta.

# Comodines (Solo se pueden usar una sola vez en todo el juego):
# Retrasar el tiempo 10 segundos.
# Que aparezca la respuesta menos votada.
# Multiplicador de puntuación. Se multiplica x2 la puntuación de la próxima respuesta encontrada.

import random
from data_100arg import lista_tematicas

def elegir_tematica(lista:list):
    nombre_tematica = []
    for item in lista:
        nombre_tematica.append(item["nombre"])
        
    nombre_tematica = list(set(nombre_tematica))
    largo_lista = len(nombre_tematica) -1
    tematica = nombre_tematica[random.randint(0,largo_lista)]
    
    return tematica

def elegir_pregunta(lista: list, tematica: str):
    lista_preguntas = []
    for item in lista:
        if item["nombre"] == tematica:
            lista_preguntas.append(item) # devuelve el dict
    
    largo_lista = len(lista_preguntas) -1
    pregunta = lista_preguntas[random.randint(0,largo_lista)]

    return pregunta

def comparar_respuesta(pregunta:dict, respuesta:str):
    if pregunta["Respuesta_1"] == respuesta:
        puntos = pregunta["Cantidad_R1"]
    elif pregunta["Respuesta_2"] == respuesta:
        puntos = pregunta["Cantidad_R2"]
    elif pregunta["Respuesta_3"] == respuesta:
        puntos = pregunta["Cantidad_R3"]
    elif pregunta["Respuesta_4"] == respuesta:
        puntos = pregunta["Cantidad_R4"]
    elif pregunta["Respuesta_5"] == respuesta:
        puntos = pregunta["Cantidad_R5"]
    else:
        puntos = 0

    return puntos

tematica = elegir_tematica(lista_tematicas)
pregunta = elegir_pregunta(lista_tematicas, tematica)
print(tematica)
print(pregunta["Pregunta"])

contador_intentos = 3
puntos_usuario = 0
puntos_aumentos = 0
respuesta_C = []
print(f"Intentos: {contador_intentos}")
print(f"Puntos: {puntos_usuario}")
while True:
    flag_repetido = False
    respuesta_usuario = input("Ingrese la respuesta que usted piense correcta: ")
    puntos = comparar_respuesta(pregunta, respuesta_usuario)
    
    for rta in respuesta_C:
        if rta == respuesta_usuario:
            print("Dijiste la misma respuesta")
            contador_intentos -= 1 
            flag_repetido = True

    if puntos == 0:
        contador_intentos -= 1 
    elif flag_repetido == False:
        respuesta_C.append(respuesta_usuario)
        puntos_usuario += puntos
        puntos_aumentos += puntos
        puntos_aumentos += puntos

    if puntos_aumentos >= 50:
        puntos_aumentos -= 50
        contador_intentos += 1 

    print(f"Puntos: {puntos_usuario}")
    print(f"Intentos: {contador_intentos}")

    if contador_intentos == 0:
        break

    # verificar que sea multiplo de 50 y sumar intento

    #si no coincide
    #contador_intentos--
    #break cuando contador == 0
