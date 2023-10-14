# a = 10
# b = 0


# try:
#     c = a/b
#     print(c)
# except:
#     print("error")

# lista = [5,3]
# try:
#     a = int(input("ingrese el dividendo: "))
#     b = int(input("ingrese el divisor: "))

#     print(lista[b])

#     c  = a/b
#     print(c)
# except ZeroDivisionError:
#     print("dividiste por 0")
# except ValueError:
#     print("no ingresaste un numero")
# except NameError:
#     print("variable no definida")
# except IndexError:
#     print("el indice buscado no corresponde con la lista")
# except Exception as ex:
#     print(type(ex))
# else:
#     print("no hay error")

# finally:
#     print("finalizo el programa")

# flag = True
# while flag:
#     try:
#         a = int(input("ingrese un numero"))
#         flag = False
#     except ValueError:
#         print("error, reingrese ")
# c = a +5
# print(c)


def pedir_entero(mensaje, mensaje_error, intentos, min, max) ->int | None:
    retorno = None
    for i in range(intentos):
        valor = input(mensaje)
        try:
            valor = int(valor)
            if valor < min or valor >max:
                raise Exception(f"el valor {valor} esta fuera de rango")
            retorno = valor
            break
        except ValueError:
            print(mensaje_error)

    return retorno

try:
    numero  = pedir_entero("ingrese nota: ","error al ingresar la nota", 3, 1,10)
    if numero != None:
        print(f"el numero ingresado es: {numero}")
    else:
        print("maximo intentos")
except Exception as ex:
    print(type(ex))
