def Media(m):
    sum = 0
    for i in m:
        sum+=i
        
    return sum/len(m)

def Visualizar(r):
    print(r)

lista = [6,5,8,7]

diccionario = {
    "Nombre" : "Lolo",
    "Curso" : "2"
}

diccionario["Media"] = Media(lista)

print (diccionario["Media"])
