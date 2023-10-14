import json

with open ('preguntas_respuestas.json','r') as archivo:
    datos = json.load(archivo)

tematicas = datos['tematicas']

print(tematicas)