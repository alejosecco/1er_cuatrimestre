from data_stark import lista_personajes
from funciones import *

#6
while True:
    numero = stark_menu_principal()
    match numero:
        case "1":
            stark_imprimir_nombres_con_iniciales(lista_personajes)
        case "2":
            stark_generar_codigos_heroes(lista_personajes)
        case "3":
            normalizar = star_normalizar_datos(lista_personajes)
            if normalizar == True:
                print("Se normalizo la lista correctamente")
            else:
                print("No se pudo normalizar la lista")
        case "4":
            stark_imprimir_indice_nombre(lista_personajes)
        case "5":
            pass
        case "6":
            break
        case _:
            print("elija una opcion valida")
    print("")



    #normalizar usar sanitizar