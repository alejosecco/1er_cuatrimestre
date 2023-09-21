from data_stark import lista_personajes
from funciones import *

flag = True
while(flag):
    respuesta = input(f"1. Normalizar datos lista\n elija una opcion:")
    if respuesta == "1":
        normalizar = star_normalizar_datos(lista_personajes)
        if normalizar == True:
            print("Datos normalizados")
            break
        else:
            print("“Hubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente”")
    else:
        print("seleccione una opcion valida")
        continue


