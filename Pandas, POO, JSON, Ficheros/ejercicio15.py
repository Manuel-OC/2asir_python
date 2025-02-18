#Escribir un archivo binario
import pickle

lista_nombres = [
  ["Luis", "1ASIR", [4,5,6,7,8]],
  ["Antonio", "2ASIR", [6,7,8,9,10,4]]
  ]


fichero_binario = open ("lista_alumnos.bin", "wb")

pickle.dump(lista_nombres, fichero_binario)

fichero_binario.close()