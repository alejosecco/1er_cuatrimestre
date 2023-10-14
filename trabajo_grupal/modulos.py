import random

def elegir_tematica(lista):
    nombres_tematicas = []
    for items in lista:
        nombres_tematicas.append(items['nombre'])

    nombres_tematicas = set(nombres_tematicas)

    return nombres_tematicas[random.randint(0,len(nombres_tematicas)-1)]

def elegir_pregunta()
    pass


def input_usuario():
    respuesta = input("ingrese una palabra")


def matchear_respuesta():
    pass
