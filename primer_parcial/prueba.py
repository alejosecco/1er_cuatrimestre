import json
import os
import preguntas_respuestas

datos = json.load(open(r"C:\Users\secco\OneDrive\Escritorio\tecnicatura\1er_cuatrimestre\programacion\primer_parcial\preguntas_respuestas.json","r"))

tematicas = datos['tematicas']

print(datos)