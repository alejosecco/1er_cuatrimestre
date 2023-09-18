"""""""""""
Ejercicio 01
Nos encargan el desarrollo de una aplicación que le permita a sus usuarios operar
en la bolsa de valores:
A) Para ello se cargarán los siguientes datos hasta que el usuario lo decida:
* Nombre
* Monto en pesos de la operación (no menor a $10000)
* Cantidad de instrumentos
* Tipo (CEDEAR, BONOS, MEP)
B) Luego del ingreso mostrar en pantalla todos los datos.
C) Realizar los siguientes informes:
1. Tipo de instrumento que más se operó.
2. Cantidad de usuarios que compraron entre 150 y 200 BONOS y que invirtieron
más de $50000.
3. Nombre y cantidad de instrumentos del usuario que compró BONOS o MEP,
que menos dinero invirtió. Puede ser más de uno.
4. Nombre de los usuarios que invirtieron en CEDEAR, cuya inversión supere el
monto promedio
5. Porcentaje de usuarios que no invirtieron en MEP, siempre y cuando el monto
no supere los $50000.
"""""""""

# Lista de 20 nombres random
nombres = ["Juan", "María", "Carlos", "Ana", "Luis", "Laura", "Diego", "Mónica", "Andrés", "Sofía",
           "Fernando", "Camila", "Gabriel", "Valentina", "Javier", "Isabella", "Miguel", "Lucía", "Eduardo", "Natalia"]

# Lista de 20 montos de dinero realistas no menores a 10000
montos_dinero = [15678, 23542, 141376, 68902, 78213, 52437, 95201, 67890, 32456, 79845,
                 104523, 83254, 67982, 54230, 30197, 89672, 45812, 75210, 63128, 100456]

# Lista con 20 tipos de inversión al azar entre "MEP", "CEDEAR" y "BONOS"
tipos_inversion = ["MEP", "CEDEAR", "BONOS", "MEP", "BONOS", "CEDEAR", "MEP", "BONOS", "CEDEAR", "CEDEAR",
                   "BONOS", "MEP", "CEDEAR", "BONOS", "MEP", "MEP", "BONOS", "CEDEAR", "BONOS", "MEP"]

cantidad_tipos = [221, 567, 170, 789, 456, 890, 345, 678, 901, 234,
                      567, 890, 123, 456, 789, 234, 567, 890, 123, 456]

for i in range(len(nombres)):
    nombre = nombres[i]
    inversion = montos_dinero[i]
    instrumento = tipos_inversion[i]
    cantidad = cantidad_tipos[i]
    print(f"{nombre:15} ${inversion}\t \t{instrumento:15}{cantidad}")

#1. Tipo de instrumento que más se operó.
contador_bonos = 0
contador_cedear = 0
contador_mep = 0
for i in range(len(nombres)):
    instrumento = tipos_inversion[i]
    match instrumento:
        case "BONOS":
            contador_bonos +=1
        case "CEDEAR":
            contador_cedear +=1
        case "MEP":
            contador_mep +=1 

lista_contadores = [contador_bonos , contador_cedear , contador_mep]



#2. Cantidad de usuarios que compraron entre 150 y 200 BONOS y que invirtieron más de $50000.
contador_punto_2 = 0
for i in range(len(nombres)):
    nombre = nombres[i]
    inversion = montos_dinero[i]
    instrumento = tipos_inversion[i]
    cantidad = cantidad_tipos[i]
    if instrumento == "BONOS" and inversion > 50000 and cantidad >=150 and cantidad <= 200:
        contador_punto_2 += 1

print(f"los que cumplen lo requerido fueron {contador_punto_2}")

#3. Nombre y cantidad de instrumentos del usuario que compró BONOS o MEP, que menos dinero invirtió. Puede ser más de uno.
bandera = False
monto_menor = 0
for i in range(len(nombres)):
    nombre = nombres[i]
    inversion = montos_dinero[i]
    instrumento = tipos_inversion[i]
    cantidad = cantidad_tipos[i]
    if instrumento == "BONOS" or instrumento == "MEP":
        if bandera == False or inversion < monto_menor:
            bandera = True
            monto_menor = inversion

for i in range(len(nombres)):
    inversion = montos_dinero[i]
    if inversion == monto_menor:
        print(f"nombre: {nombres[i]}\t {tipos_inversion[i]}\t cantidad: {cantidad_tipos[i]}")

#4. Nombre de los usuarios que invirtieron en CEDEAR, cuya inversión supere el monto promedio

acumulador = 0
for i in range(len(nombres)):
    inversion = montos_dinero[i]
    acumulador += inversion

promedio_inversion = acumulador / (len(montos_dinero))
for i in range(len(tipos_inversion)):
    nombre = nombres[i]
    inversion = montos_dinero[i]
    instrumento = tipos_inversion[i]
    cantidad = cantidad_tipos[i]
    if instrumento == "CEDEAR":
        if inversion > promedio_inversion:
            print(f"{nombre} supera la inversion promedio")

#5. Porcentaje de usuarios que no invirtieron en MEP, siempre y cuando el monto no supere los $50000.
contador = 0
for i in range(len(montos_dinero)):
    instrumento = tipos_inversion[i]
    inversion = montos_dinero[i]
    if instrumento != "MEP" and inversion < 50000:
        contador +=1

porcentaje = contador * 100 / (len(montos_dinero))
print(f"fue del {porcentaje}%")