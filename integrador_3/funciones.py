import re
from data_stark import lista_personajes

#1.1
def extraer_iniciales(nombre:str):
    """
    Brief:
    Parametros:
        1: 
    Returns:
    """
    if nombre:
        iniciales = re.sub('the ','',nombre)
        iniciales = re.sub('-',' ',iniciales)
        iniciales = re.sub('[a-z]+','',iniciales)
        iniciales = re.sub(' ','.',iniciales)
    else:
        iniciales = "N/A"

    return iniciales

#1.2
def obtener_dato_formato(dato:str):
    """
    Brief:
    Parametros:
        1: 
    Returns:
    """
    if dato:
        result = re.sub(' |-','_',dato)
        result = result.lower()
    else:
        result = False
    return result

#1.3
def stark_nombre_con_iniciales(personaje:dict):
    """
    Brief:
    Parametros:
        1: 
    Returns:
    """
    if personaje and "nombre" in personaje:
        nombre = personaje['nombre']
        iniciales = extraer_iniciales(nombre)
        nombre_normalizado = obtener_dato_formato(nombre)
        mensaje = f"* {nombre_normalizado} ({iniciales})"
        print(mensaje)
        flag = True
    else:
        flag = False
    return flag

#1.4
def stark_imprimir_nombres_con_iniciales(lista:list):
    """
    Brief:
    Parametros:
        1: 
    Returns:
    """
    if lista:
        for personaje in lista:
            stark_nombre_con_iniciales(personaje)
        flag = True
    else:
        flag = False
    return flag

#2.1
def generar_codigo_heroe(personaeje:dict,id:int):
    """
    Brief:
    Parametros:
        1: 
        2:
    Returns:
    """
    pass

#2.2

#3.1

#3.2

#3.3

#3.4

#3.5

#4.1

#5.1

#5.2

#5.3

#5.4

#6
