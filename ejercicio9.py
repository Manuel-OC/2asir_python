def MostrarAsignaturaPeorNota(d):
    menor = 999
    
    for i in d:
        valor = d[i]
        if valor < menor:
            menor = valor
            asignatura = i
    
    return asignatura

def Visualizar(r):
    print(r)

diccionario = {
    "mates" : 6,
    "lengua" : 5,
    "ingles" : 8,
    "informatica" : 7
}

Visualizar(MostrarAsignaturaPeorNota(diccionario))
