from data import lista_bzrp

bandera_primero = False
maximo_vistas = 0

for video in lista_bzrp:
    vistas = video["views"]
    if bandera_primero == False or vistas > maximo_vistas:        
        maximo_vistas = vistas
        bandera = True

print(maximo_vistas)

for video in lista_bzrp:
    vistas = video['views']
    if vistas == maximo_vistas:
        cancion = video['title']
        print(cancion)


promedio = 10.2

print(f"{promedio:0.2f}")
    