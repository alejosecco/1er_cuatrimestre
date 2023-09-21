from data_stark import lista_personajes
    
def star_normalizar_datos():
    for personaje in lista_personajes:
        flag = False
        if personaje["fuerza"] != int:
            personaje["fuerza"] = int(personaje["fuerza"])
            flag = True
        if personaje["altura"] != float:
            personaje["altura"] = float(personaje["altura"])
            flag = True
        if personaje["peso"] != float:
            personaje["peso"] = float(personaje["peso"])
            flag = True
    return flag

def obtener_dato(diccionario:dict,dato:str):
    respuesta = False
    if diccionario and dato in diccionario:
        respuesta = diccionario[dato]
        respuesta = respuesta
    return respuesta

def obtener_nombre(diccionario:dict):
    respuesta = False
    if diccionario and diccionario["nombre"]:
        nombre = diccionario["nombre"]
        respuesta = (f"nombre: {nombre}")
    return respuesta

def obtener_nombre_y_dato(diccionario:dict,dato:str):
    respuesta = False
    if diccionario and dato in diccionario:
        nombre = obtener_nombre(diccionario)
        dato_pedido = obtener_dato(diccionario, dato)
        respuesta = f"nombre: {nombre} | {dato}: {dato_pedido}"
    return respuesta

def obtener_maximo(lista:list,key:str):
    respuesta = False
    if lista:
        for personaje in lista:
            if personaje[key] == int or personaje[key] == float:
                dato = personaje[key]
                if respuesta == False or dato > respuesta:
                    respuesta = dato
    return respuesta

def obtener_minimo(lista:list,key:str):
    respuesta = False
    if lista:
        for personaje in lista:
            if personaje[key] == int or personaje[key] == float:
                dato = personaje[key]
                if respuesta == False or dato < respuesta:
                    respuesta = dato
    return respuesta

def obtener_dato_cantidad(lista:list,valor:int,key:str):
    pass
#########
