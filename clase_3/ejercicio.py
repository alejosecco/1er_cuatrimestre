from data_stark import lista_personajes

while True:
    respuesta = int(input("1. mostrar todos los datos de cada superhéroe \n2. mostrar la identidad y el peso del superhéroe con mayor fuerza \n3. mostrar nombre e identidad del superhéroe más bajo \n4. determinar el peso promedio de los superhéroes masculinos \n5.  mostrar nombre y peso de los superhéroes los cuales su fueza supere a la fuerza promedio de todas las superhéroes de género femenino\n6. salir \nElija una opcion:"))
    print(" ")
    match(respuesta):
        case 1:
            #Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
            for personaje in lista_personajes:
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
        case 2:
             #B Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor fuerza (MÁXIMO)
            flag = False
            mayor_fuerza = 0
            for personaje in lista_personajes:
                fuerza = float(personaje['fuerza'])
                if flag == False or fuerza > mayor_fuerza:
                    mayor_fuerza = fuerza
                    flag = True
            for personaje in lista_personajes:
                fuerza = float(personaje['fuerza'])
                identidad = personaje['identidad']
                if fuerza == mayor_fuerza:
                    print(f"identidad: {identidad}\t fuerza: {fuerza}")
        case 3:
            #Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo (MÍNIMO)
            flag = False
            altura_minima = 0
            for personaje in lista_personajes:
                altura = float(personaje['altura'])
                if flag == False or altura < altura_minima:
                    altura_minima = altura
                    flag = True
            for personaje in lista_personajes:
                nombre = personaje['nombre']
                identidad = personaje['identidad']
                altura = float(personaje['altura'])
                if altura == altura_minima:
                    print(f"nombre: {nombre}\t identidad: {identidad}\t altura: {altura}")
        case 4:
            #Recorrer la lista y determinar el peso promedio de los superhéroes masculinos (PROMEDIO)
            acumulador = 0
            contador = 0
            for personaje in lista_personajes:
                peso = float(personaje['peso'])
                genero = personaje['genero']
                if genero == "M":
                    acumulador += peso
                    contador += 1
            promedio = acumulador / contador
            print(f"el promedio de peso de los masculinos es: {promedio}")
        case 5:
            #Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier género) los cuales su fuerza supere a la fuerza promedio de todas las superhéroes de género femenino
            acumulador = 0
            contador = 0
            for personaje in lista_personajes:
                fuerza = float(personaje['fuerza'])
                genero = personaje['genero']
                if genero == "F":
                    acumulador += fuerza
                    contador += 1
            promedio_femenino = acumulador / contador
            for personaje in lista_personajes:
                fuerza = float(personaje['fuerza'])
                nombre = personaje['nombre']
                peso = personaje['peso']
                if fuerza > promedio_femenino:
                    print(f"nombre: {nombre:20} peso: {peso}")
        case 6:
            break
    print(" ")
