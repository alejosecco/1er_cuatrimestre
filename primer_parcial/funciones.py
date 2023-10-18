import random

def elegir_tematica(lista:list):
    """
    Brief: se encarga de elegir aleatoriamente una tematica
    Parametros:
        1: lista con tematicas/preguntas
    Returns: retorna una tematica
    """
    tematicas = []
    for i in lista:
        tematicas.append(i["tematica"])
    tematicas = list(set(tematicas))

    largo_lista = len(tematicas) -1
    return tematicas[random.randint(0,largo_lista)]

def elegir_pregunta(tematica:str,lista:list):
    """
    Brief: se encarga de elegir una pregunta dentro de la tematica de forma aleatoria
    Parametros:
        1: tematica en la que se busca
        2: lista con tematicas/preguntas
    Returns: una pregunta dentro de la tematica
    """
    preguntas = []
    for i in lista:
        if i["tematica"] == tematica:
            preguntas.append(i)

    largo_lista = len(preguntas) -1
    return preguntas[random.randint(0,largo_lista)]
    

def borrar_tematica(tematica:str,lista:list):
    """
    Brief: se encarga de borrar la tematica de la cual ya se uso una pregunta
    Parametros:
        1: la tematica que se va a borrar
        2: lista con tematicas/preguntas
    """
    for i in range(0,len(lista)-1):
        try:
            if lista[i]["tematica"] == tematica:
                lista.pop(i)
        except IndexError:
            pass
    
def normalizar_respuesta(respuesta:str):
    """
    Brief:
    Parametros:
        1: 
    Returns:
    """
    pass

def obtener_respuesta_y_normalizar():
    """
    Brief:
    Parametros:
        1: 
    Returns:
    """
    respuesta = input("Ingrese la respuesta que usted piense correcta: ")
    respuesta_normalizada = normalizar_respuesta(respuesta)
    
    return respuesta_normalizada

def obtener_puntos(pregunta:dict, respuesta:str):
    """
    Brief: se encarga de comparar la respuesta del usuario con las correctas y devolver los puntos correspondientes
    Parametros:
        1: la pregunta que se le hizo al usuario
        2: la respuesta dada por el usuario
    Returns: los puntos obtenidos
    """
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

def mostrar_respuestas(pregunta:dict):
    """
    Brief: muestra las respuestas posibles a la pregunta 
    Parametros:
        1: pregunta que se le hizo al usuario
    """
    respuesta_1 = pregunta["Respuesta_1"]
    cantidad_r1 = pregunta["Cantidad_R1"]
    respuesta_2 = pregunta["Respuesta_2"]
    cantidad_r2 = pregunta["Cantidad_R2"]
    respuesta_3 = pregunta["Respuesta_3"]
    cantidad_r3 = pregunta["Cantidad_R3"]
    respuesta_4 = pregunta["Respuesta_4"]
    cantidad_r4 = pregunta["Cantidad_R4"]
    respuesta_5 = pregunta["Respuesta_5"]
    cantidad_r5 = pregunta["Cantidad_R5"]
    print("respuestas:\n"
          f"{respuesta_1}: {cantidad_r1} argentinos\n"
          f"{respuesta_2}: {cantidad_r2} argentinos\n"
          f"{respuesta_3}: {cantidad_r3} argentinos\n"
          f"{respuesta_4}: {cantidad_r4} argentinos\n"
          f"{respuesta_5}: {cantidad_r5} argentinos\n")
          
    


def obtener_premio(puntos:int):
    """
    Brief: se encarga de calcular el premio segun los puntos obtenidos
    Parametros:
        1: puntos que obtuvo el usuario en el juego
    Returns: retorna el total del premio
    """
    if puntos == 500:
        premio = 1000000
    else:
        premio = puntos * 500
    
    return premio

def ronda_juego(lista:list):
    """
    Brief: es una rondas del juego la cual esta hecha para utilizarse varias veces
    Parametros:
        1: lista con tematicas/preguntas
    Returns: retorna los puntos ganados en la ronda
    """
    acumulador_puntos = 0
    tematica = elegir_tematica(lista)
    pregunta = elegir_pregunta(tematica,lista)
    print (tematica)
    intentos = 5
    respuestas_ingresadas = []
    puntos_obtenidos = 0
    while intentos > 0 :
        flag = True
        print (pregunta["Pregunta"])
        respuesta_usuario = input("ingrese la respuesta: ")#obtener_respuesta_y_normalizar()
        puntos_obtenidos = obtener_puntos(pregunta,respuesta_usuario)
        for rta in respuestas_ingresadas:
            if respuesta_usuario == rta:
                print("ya ingresaste esta respuesta")
                flag = False
        if puntos_obtenidos == 0:
            print("no")
        elif flag == True:
            print("si")
            respuestas_ingresadas.append(respuesta_usuario)
            acumulador_puntos += puntos_obtenidos
        else:
            print("no")
        intentos -=1
        print(f"intentos restantes: {intentos}")
        print(f"llevas {acumulador_puntos} de 100 puntos")
    mostrar_respuestas(pregunta)
    borrar_tematica(tematica,lista)
    return acumulador_puntos


def obtener_nombre_jugador():
    """
    Brief:
    Parametros:
        1: 
    Returns:
    """


def anotar_punjates_nombres():
    """
    Brief:
    Parametros:
        1: 
    Returns:
    """
    