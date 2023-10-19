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
        return mensaje
    else:
        return False

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
            print(stark_nombre_con_iniciales(personaje))
    else:
        return False

#2.1
def generar_codigo_heroe(personaje:dict,id:int):
    """
    Brief:
    Parametros:
        1:
    Returns:
    """
    genero = personaje["genero"]
    match genero:
        case "M":
            retorno = "M-1"
        case "F":
            retorno = "F-2"
        case "NB":
            retorno = "NB-0"
        case _:
            return "N/A"        
    id = str(id).zfill(10 - len(retorno))
    retorno = f"{retorno}{id}"
    
    return retorno

#2.2
def stark_generar_codigos_heroes(lista:list):
    """
    Brief:
    Parametros:
        1:
    Returns:
    """
    flag = True
    if lista:
        for i in lista:
            if i:
                pass
            else: 
                flag = False
        contador = 0
        if flag:
            for personaje in lista:
                contador +=1
                codigo = (generar_codigo_heroe(personaje,contador))
                nombre = stark_nombre_con_iniciales(personaje)
                print(f"{nombre} | {codigo}")
            print(f"se asignaron {contador} codigos")
        else:
            return False

#3.1
def sanitizar_entero(numero:str):
    """
    Brief:
    Parametros:
        1:
        2:
    Returns:
    """
    try:
        numero = numero.strip()
        numero_sanitizado = int(numero)
        if retorno >0:
            retorno = numero_sanitizado
        else:
            retorno = -2
    except Exception:
        if  not numero.isdigit():
            retorno = -1
        else:
            retorno = -3
    return retorno

#3.2
def sanitizar_float(numero:str):
    """
    Brief:
    Parametros:
        1:
        2:
    Returns:
    """
    try:
        numero = numero.strip()
        numero_sanitizado = float(numero)
        if retorno >0:
            retorno = numero_sanitizado
        else:
            retorno = -2
    except Exception:
        if  not numero.isdigit():
            retorno = -1
        else:
            retorno = -3
    return retorno

#3.3
def sanitizar_string(valor:str,valor_por_defecto:str):
    try:
        valor = valor.strip()
        pass
    except:
        pass

#3.4
def sanitizar_dato(personaje:dict,clave:str,tipo:str):
    pass

#3.5

#4.1
def stark_imprimir_indice_nombre(lista:list):
    """
    Brief:
    Parametros:
        1:
        2:
    Returns:
    """
    nombres = []
    for i in lista:
        nombre = i["nombre"]
        nombre = re.sub('the ','',nombre)
        nombre = re.sub(' ','-',nombre)
        nombre = nombre.lower()
        nombres.append(nombre)
    cadena = "-"
    print(cadena.join(nombres))

#5.1
def generar_separador(patron:str,largo:int):
    try:
        if len(patron)>0 and len(patron) <3 and largo >0 and largo <=235:
            separador = []
            for i in range(largo):
                separador.append(patron)
            cadena = ""
            separador = cadena.join(separador)
            return separador
        else:
            return print("N/A")
    except Exception:
        return print("N/A")

#5.2
def generar_encabezado(titulo:str):
    try:
        titulo = titulo.upper()
        print("**********************************************************************************"
            f"\n{titulo}"
            "\n**********************************************************************************"
            )
    except:
        return "N/A"
#5.3
def imprimir_ficha_heroe(personaje:dict):
    generar_encabezado("principal")
    print(f"NOMBRE DEL HEROE:\t{stark_nombre_con_iniciales(personaje)}\n\n"
          f"IDENTIDAD SECRETA:\t{obtener_dato_formato(personaje["identidad"])}\n\n"
          f"CONSULTORA:\t{obtener_dato_formato(personaje["empresa"])}\n\n"
          f"CODIGO DE HEROE:\t{2}")
    generar_encabezado("fisico")
    print(f"ALTURA:\t{obtener_dato_formato(personaje["altura"])}\n\n"
          f"PESO:\t{obtener_dato_formato(personaje["peso"])}\n\n"
          f"FUERZA:\t{obtener_dato_formato(personaje["fuerza"])}")
    generar_encabezado("señas particulares")
    print(f"COLOR DE OJOS:\t{obtener_dato_formato(personaje["color_ojos"])}\n\n"
          f"COLOR DE PELO:\t{obtener_dato_formato(personaje["color_pelo"])}")



#5.4





def imprimir_menu():
    """
    Brief: imprime el menu del programa
    """
    print ("1. Imprimir la lista de nombres junto con sus iniciales"
           "\n2. Imprimir la lista de nombres y el código del mismo" 
            "\n3. Normalizar datos"
            "\n4. Imprimir índice de nombres"
            "\n5. Navegar fichas"
            "\n6. Salir")
    print(" ")

def validar_entero(numero:str):
    """
    Brief: valida que el dato que se le pasa sea un numero
    Parametros:
        1: numero a validar
    Returns: retorna un true si es un numero y false si no es un numero
    """
    if numero.isnumeric() == True and numero:
          respuesta = True
    else:
         respuesta = False
    return respuesta

def star_normalizar_datos(lista:list):
    """
    Brief: normaliza los datos numericos a int o flaot segun corresponda
    Parametros:
        1: lista de personajes
    Returns: retorna true en caso de normalizar 1 o mas datos y false en caso de que ya esten normalizador
    """
    for personaje in lista:
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

def stark_menu_principal():
    """
    Brief: imprime el menu y pide que de un numero que corresponda con las opciones
    Returns: retorna el dato validado o un false en caso de no ser un numero
    """
    imprimir_menu()
    usuario = input("Elija una opcion:")
    if validar_entero(usuario) == True:
         respuesta = usuario
    else:
         respuesta = False
    return respuesta