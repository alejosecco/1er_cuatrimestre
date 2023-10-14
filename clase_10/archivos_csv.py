import re


# nombres = ["Jose", "Carlos" , "Ana"]
# apellidos = ["Gomez", "Ruiz", "Perez"]
# edades = [20, 19, 34]

# with open("agenda.xlsx", "w") as archivo:
#     for i in range(len(nombres)):
#         mensaje = f"{nombres[i]},{apellidos[i]},{edades[i]}"
#         archivo.write(mensaje)

def parsear_agenda(path:str) ->list:
    agenda = []

    with open("agenda.csv", "r") as archivo:
        for linea in archivo:
            registro = re.split(",|\n", linea)
            contacto = {}
            contacto["nombre"] = registro[0]
            contacto["apellido"] = registro[1]
            contacto["edad"] = registro[2]
            agenda.append(contacto)

    return agenda

mi_agenda = parsear_agenda("agenda.csv")
if (len(mi_agenda) != 0):
    for contacto in mi_agenda:
        print(f"{contacto['nombre']:20} {contacto['apellido']:20} {contacto['edad']:20}")