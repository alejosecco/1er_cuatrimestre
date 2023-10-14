import random

def elegir_tematica(lista:list):
    """
    Brief:
    Parametros:
        1: 
    Returns:
    """
    tematicas = []
    for i in lista:
        tematicas.append(i["tematica"])
    tematicas = list(set(tematicas))

    largo_lista = len(tematicas) -1
    return tematicas[random.randint(0,largo_lista)]

def elegir_pregunta(tematica:str,lista:list):
    """
    Brief:
    Parametros:
        1: 
    Returns:
    """
    preguntas = []
    for i in lista:
        if i["tematica"] == tematica:
            preguntas.append(i)

    largo_lista = len(preguntas) -1
    return preguntas[random.randint(0,largo_lista)]
    

def borrar_tematica(tematica:str,lista:list):
    """
    Brief:
    Parametros:
        1: 
    Returns:
    """
    for i in range(0,len(lista)-1):
        if lista[i]["tematica"] == tematica:
            lista.pop(i)
    
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
    Brief:
    Parametros:
        1: 
    Returns:
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
    Brief:
    Parametros:
        1: 
    Returns:
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
          
    

def sumar_vidas(vidas:int,puntos:int):
    """
    Brief:
    Parametros:
        1: 
    Returns:
    """
    if puntos >= 50:
        vidas +=1
        puntos -= 50
    return vidas, puntos

def premio(puntos:int):
    """
    Brief:
    Parametros:
        1: 
    Returns:
    """
    if puntos == 500:
        premio = 1000000
    else:
        premio = puntos * 500
    
    return premio

def ronda_juego(lista:list,vidas:int,puntos:int,puntos_para_vidas:int):
    """
    Brief:
    Parametros:
        1: 
    Returns:
    """
    tematica = elegir_tematica(lista)
    pregunta = elegir_pregunta(tematica,lista)
    print (tematica)
    flag = True
    intentos = 5
    while flag:
        if intentos ==0:
            print("te quedaste sin intentos")
            break
        print (pregunta["Pregunta"])
        respuesta_usuario = input("hola")#obtener_respuesta_y_normalizar()
        puntos_obtenidos = obtener_puntos(pregunta,respuesta_usuario)
        if puntos_obtenidos != 0:
            print("si")
            puntos += puntos_obtenidos
            puntos_para_vidas += puntos_obtenidos
        else:
            print("no")
        intentos -=1
    if puntos == 0:
        vidas -=1
    vidas, puntos_para_vidas = sumar_vidas(vidas,puntos_para_vidas)
    print(f"total puntos: {puntos}")
    print(f"vidas restantes: {vidas}")
    mostrar_respuestas(pregunta)
    borrar_tematica(tematica,lista)
    # print(puntos_para_vidas)
    return vidas, puntos



from preguntas_respuestas import lista_tematicas
# for i in range(3):
ronda_juego(lista_tematicas,3,0,0)