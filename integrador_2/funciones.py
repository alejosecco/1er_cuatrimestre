#0
def star_normalizar_datos(lista:list):
    """
    Brief:
    Parametros:
        1: 
        2:
    Returns:
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

#1.1
def obtener_dato(diccionario:dict,dato:str):
    """
    Brief:
    Parametros:
        1: 
        2:
    Returns:
    """
    if diccionario and dato in diccionario:
        respuesta = diccionario[dato]
    else:
        False
    return respuesta

#1.2
def obtener_nombre(diccionario:dict):
    """
    Brief:
    Parametros:
        1: 
        2:
    Returns:
    """
    nombre = obtener_dato(diccionario,"nombre")
    if nombre == False:
        respuesta = False
    else: 
        respuesta = (f"nombre: {nombre}")
    return respuesta

#2
def obtener_nombre_y_dato(diccionario:dict,dato:str):
    """
    Brief:
    Parametros:
        1: 
        2:
    Returns:
    """
    nombre = obtener_nombre(diccionario)
    dato_pedido = obtener_dato(diccionario, dato)
    if nombre != False and dato != False:
        respuesta = f"nombre: {nombre} | {dato}: {dato_pedido}"
    else:
        respuesta = False
    return respuesta

# #3.1
def obtener_maximo(lista:list,key:str):
    """
    Brief:
    Parametros:
        1: 
        2:
    Returns:
    """
    flag = False
    respuesta = 0
    if lista:
        for personaje in lista:
            dato = obtener_dato(personaje,key)
            if flag == False or dato > respuesta:
                    flag = True
                    respuesta = dato
    else:
        respuesta = False
    return respuesta
#3.2
def obtener_minimo(lista:list,key:str):
    """
    Brief:
    Parametros:
        1: 
        2:
    Returns:
    """
    flag = False
    respuesta = 0
    if lista:
        for personaje in lista:
            dato = obtener_dato(personaje,key)
            if flag == False or dato < respuesta:
                    flag = True
                    respuesta = dato
    else:
        respuesta = False
    return respuesta

#3.3
def obtener_dato_cantidad(lista:list,valor:int,key:str):
    """
    Brief:
    Parametros:
       1: 
       2:
    Returns:
    """
    lista_dato = []
    for personaje in lista:
         if personaje[key] == valor:
              lista_dato.append(personaje['nombre'])
    return lista_dato
              

#3.4
def stark_imprimir_heroes(lista:list):
    """
    Brief:
    Parametros:
        1: 
        2:
    Returns:
    """
    for personaje in lista:
                nombre = personaje['nombre']
                identidad = personaje['identidad']
                empresa = personaje['empresa']
                altura = personaje['altura']
                peso = personaje['peso']
                genero = personaje['genero']
                color_ojos = personaje['color_ojos']
                color_pelo =  personaje['color_pelo']
                fuerza = personaje['fuerza']
                inteligencia = personaje['inteligencia']
                print(f"nombre: {nombre}\nidentidad: {identidad}\nempresa: {empresa}\naltura: {altura}\npeso: {peso}\ngenero: {genero}\ncolor de ojos; {color_ojos}\ncolor de pelo: {color_pelo}\nfuerza: {fuerza}\ninteligencia: {inteligencia}")
                print(" ")

#4.1
def sumar_datos_heroe(lista:list,key:str):
    """
    Brief:
    Parametros:
        1: 
        2:
    Returns:
    """
    acumulador = 0
    for personaje in lista:
            acumulador += obtener_dato(personaje,key)
    return acumulador

#4.2
def dividir(dividendo:float,divisor:float):
    """
    Brief:
    Parametros:
        1: 
        2:
    Returns:
    """
    resultado = False
    if divisor != 0:
        resultado = dividendo / divisor
    return resultado

#4.3
def calcular_promedio(lista:list,dato:str):
    """
    Brief:
    Parametros:
        1: 
        2:
    Returns:
    """
    dividendo = sumar_datos_heroe(lista, dato)
    divisor = len(lista)
    promedio = dividir(dividendo, divisor)
    return promedio

#4.4
def mostrar_promedio_dato(lista:list,dato:str):
    """
    Brief:
    Parametros:
        1: 
        2:
    Returns:
    """
    if lista:
        respuesta = calcular_promedio(lista, dato)
    else:
        respuesta = False
    return respuesta

#5.1
def imprimir_menu():
    print ("\n2. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB" +
            "\n3. Recorrer la lista y determinar cuál es el superhéroe más alto de género F"+
            "\n4. Recorrer la lista y determinar cuál es el superhéroe más alto de género M" + 
            "\n5.  Recorrer la lista y determinar cuál es el superhéroe más débil de género M"+
            "\n6. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB"+
            "\n7. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB"+
            "\n8. Determinar cuántos superhéroes tienen cada tipo de color de ojos"+
            "\n9. Determinar cuántos superhéroes tienen cada tipo de color de pelo."+
            "\n10. Listar todos los superhéroes agrupados por color de ojos"+
            "\n11. Listar todos los superhéroes agrupados por tipo de inteligencia"+
            "\n12. salir")
    print(" ")

#5.2
def validar_entero(numero:str):
    if numero.isnumeric() == True and numero:
          respuesta = True
    else:
         respuesta = False
    return respuesta

#5.3
def stark_menu_principal():
    imprimir_menu()
    usuario = input("Elija una opcion:")
    if validar_entero(usuario) == True:
         respuesta = usuario
    else:
         respuesta = False
    return respuesta

##
def obtener_superheroes_por_genero(lista:list,genero:str):
    lista_genero = []
    for personaje in lista:
          if personaje["genero"] == genero:
               lista_genero.append(personaje)
    return lista_genero
##
def lista_tipos(key:str):
    if key == "ojos":
        tipos = ["Blue","Green","Brown","Yellow","Hazel","Silver","Red"]
    elif key == "pelo":
        tipos = ["black","Auburn","White","Brown","No Hair","Blond","Green","","Red",]
    elif key == "inteligencia":
        tipos = ["average","high","good",""]
    return tipos

#6
def stark_marvel_app(lista:list):
    while True:
        print("1. Normalizar datos")
        primer_numero = input("Elija una opcion:")
        if validar_entero(primer_numero) == True:
            match(primer_numero):
                case "1":
                    break
                case _:
                        print("elija una opcion valida")
                        print(" ")
                        continue
    while True:
        star_normalizar_datos(lista)
        numero = stark_menu_principal()
        if validar_entero(numero) == True:
            match(numero):
                case "2":
                    for personaje in obtener_superheroes_por_genero(lista,"NB"):
                        print(personaje['nombre'])
                case "3":
                    lista_genero = obtener_superheroes_por_genero(lista,"F")
                    print(obtener_dato_cantidad(lista_genero,obtener_maximo(lista_genero,"altura"),"altura"))
                case "4":
                    lista_genero = obtener_superheroes_por_genero(lista,"M")
                    print(obtener_dato_cantidad(lista_genero,obtener_maximo(lista_genero,"altura"),"altura"))
                case "5":
                    lista_genero = obtener_superheroes_por_genero(lista,"M")
                    print(obtener_dato_cantidad(lista_genero,obtener_minimo(lista_genero,"fuerza"),"fuerza"))
                case "6":
                    lista_genero = obtener_superheroes_por_genero(lista,"NB")
                    print(obtener_dato_cantidad(lista_genero,obtener_minimo(lista_genero,"fuerza"),"fuerza"))
                case "7":
                    lista_genero = obtener_superheroes_por_genero(lista,"NB")
                    print(mostrar_promedio_dato(lista_genero,"fuerza"))
                case "8":
                    for color in lista_tipos("ojos"):
                        lista_color = obtener_dato_cantidad(lista,color,"color_ojos")
                        mensaje = f"{color}: {len(lista_color)}"
                        print(mensaje)
                case "9":
                    for color in lista_tipos("pelo"):
                        lista_color = obtener_dato_cantidad(lista,color,"color_pelo")
                        mensaje = f"{color}: {len(lista_color)}"
                        print(mensaje)
                case "10":
                    for color in lista_tipos("ojos"):
                        lista_color = obtener_dato_cantidad(lista,color,"color_ojos")
                        mensaje = f"{color}: {lista_color}"
                        print (mensaje)
                case "11":
                    for inteligencia in lista_tipos("inteligencia"):
                        lista_inteligencia = obtener_dato_cantidad(lista,inteligencia,"inteligencia")
                        mensaje = f"{inteligencia}: {lista_inteligencia}"
                        print (mensaje)
                case "12":
                    break 
                case _:
                    print("elija una opcion valida")
                    print(" ")