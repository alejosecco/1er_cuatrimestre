'''
UTN Tecnologies, una reconocida software factory se encuentra en la busqueda de ideas para su proximo
desarrollo en python,
que promete revolucionar el mercado.
Las posibles aplicaciones son las siguientes:
    # Inteligencia artificial (IA),
    # Realidad virtual/aumentada (RV/RA),
    # Internet de las cosas (IOT) o
    # Procesamiento de lenguaje natural (NLP).


Para ello, realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas:


A) Los datos a ingresar por cada empleado encuestado son:
    * nombre del empleado
    * edad (no menor a 18)
    * genero (Masculino - Femenino - Otro)
    * tecnologia (IA, RV/RA, IOT, NLP)  
B) Cargar por terminal 10 encuestas.
C) Determinar:
    1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y
    50 años inclusive.
    2) - Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea
    Femenino o su edad se encuentre entre los 33 y 40.
    3) - Nombre y tecnología que votó, de los empleados de género masculino con mayor edad.
    de ese género.
'''


lista_nombres = ["Juan", "María", "Pedro", "Ana", "Luis", "Carla", "Diego", "Laura", "José", "Marta",
                    "Gabriel", "Elena", "Pablo", "Lucía", "Ricardo", "Valeria", "Fernando", "Sofía", "Hugo", "Clara"]


lista_edades = [25, 30, 45, 38, 42, 25, 49, 32, 19, 49,
                    32, 22, 29, 27, 19, 49, 27, 22, 49, 27]
       
lista_generos = ["Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino", "Femenino",
                        "Otro", "Femenino", "Masculino", "Otro", "Masculino", "Femenino", "Masculino", "Femenino", "Masculino",
                        "Femenino", "Masculino", "Otro"]
       
lista_tecnologias = ["IOT", "RV/RA", "NLP", "IA", "NLP", "IOT", "RV/RA", "IOT", "IA", "NLP",
                    "RV/RA", "RV/RA", "NLP", "RV/RA", "IA", "IOT", "NLP", "IOT", "IA", "IA"]  

#A

for i in range(len(lista_edades)):
    nombre = lista_nombres[i]
    edad = lista_edades[i]
    genero = lista_generos[i]
    tecnologia = lista_tecnologias[i]
    print(f"{nombre:15} {edad}\t {genero:15} {tecnologia}")

#C

#1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
contador_punto_1 = 0
for i in range(len(lista_edades)):
    nombre = lista_nombres[i]
    edad = lista_edades[i]
    genero = lista_generos[i]
    tecnologia = lista_tecnologias[i]
    if genero == "Masculino" and (tecnologia == "IOT" or tecnologia == "IA") and edad >= 25 and edad <= 50:
        contador_punto_1 += 1
print(f"la cantidad de personas que cumplen con los requisitos son {contador_punto_1}")

#2) - Porcentaje de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40.
contador_punto_2 = 0
bandera = False
for i in range(len(lista_edades)):
    nombre = lista_nombres[i]
    edad = lista_edades[i]
    genero = lista_generos[i]
    tecnologia = lista_tecnologias[i]
    
    if tecnologia != "IA" and (genero != "Femenino" or edad <=33 and edad >= 40):
        contador_punto_2 += 1
        bandera = True
    
if bandera == True: 
    porcentaje = (contador_punto_2 * 100) / len(lista_edades)
    print(f"el porcentaje fue de {porcentaje}%")
else:
    print("no hay personas que cumplan estas caracteristicas")

#3) - Nombre y tecnología que votó, de los empleados de género masculino con mayor edad de ese género.
bandera_punto_3 = False
edad_maxima = 0
for i in range(len(lista_edades)):
    edad = lista_edades[i]
    if bandera == False or edad > edad_maxima:
        bandera == True
        edad_maxima = edad

for i in range(len(lista_edades)):
    nombre = lista_nombres[i]
    edad = lista_edades[i]
    genero = lista_generos[i]
    tecnologia = lista_tecnologias[i]
    if edad == edad_maxima:
        print(f"{nombre}\t {tecnologia}")



