lista = [1,3,4,5,6,8,123,87,324]
c_i = 0
c_j = 0

for i in range(len(lista)-1):
    for j in range(i+1,len(lista)):
        if lista[i]> lista[j]:
            # auxiliar = lista[i]
            # lista[i] = lista[j]
            # lista[j] = auxiliar
            lista[i],lista[j] = lista[j],lista[i]

for i in range(len(lista)):
    print(lista[i])


