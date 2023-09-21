#1. Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.
def calcular_area_circulo(radio:float):
    area = 3.14 * radio ** 2
    return area

#2. Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.
def par_impar(numero:int):
    if numero % 2 == 0:
        mensaje = f"el numero {numero} es par"
    else:
        mensaje = f"el numero {numero} es impar"
    return mensaje
    
#3. Diseña una función que tome una lista de números y devuelva la suma de todos los elementos.
def suma_lista(lista:list):
    acumulador = 0
    for numero in lista:
        acumulador += numero
    return acumulador

#4. Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.
def maximo(numero_1:float, numero_2:float, numero_3:float):
    flag = True
    numero_maximo = 0
    numeros = [numero_1,numero_2,numero_3]
    for i in numeros:
        if flag == True or i > numero_maximo:
            flag = False
            numero_maximo = i
    return numero_maximo

#5. Escribe una función que tome una cadena como entrada y devuelva la cadena invertida.
def invertir_cadena(cadena:str):
    cadena_invertida = cadena[::-1]
    return cadena_invertida

#6. Crea una función que reciba una lista de palabras y devuelva una nueva lista con las palabras ordenadas alfabéticamente.
def ordenar_alf(lista:list):
    lista_ordenada = sorted(lista)
    return lista_ordenada

#7. Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.
def potencia(base:int, exponente:int):
    resultado = base ** exponente
    return resultado

#8. Define una función que reciba una lista de números y devuelva una nueva lista con solo los números pares.
def lista_pares(lista:list):
    pares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        return pares

#9. Escribe una función que tome una lista de números y calcule el producto de todos los elementos.
def producto(lista:list):
    acumulador = 0
    flag = True
    for i in lista:
        if flag == True:
            acumulador = i 
            flag = False
        else:
            acumulador *= i
    return acumulador

#10. Crea una función que determine si una cadena dada es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
def palindromo(cadena:str):
    if cadena == cadena[::-1]:
        mensaje = "es palindromo"
    else:
        mensaje = "no es palindromo"
    return mensaje