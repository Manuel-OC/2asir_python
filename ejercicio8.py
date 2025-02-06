def Media(m):
    sum = 0
    for i in m:
        sum+=i
        
    return sum/len(m)

def MostrarMedia(d):
    for i in d:
        nom = i['Nombre']
        med = Media(i['Notas'])
        print(f"La media de {nom} es {med}")

diccionario = [
    {
    "Nombre" : "Sara",
    "Curso" : 1,
    "Notas" : [5,3,5,2]
},
    {
    "Nombre" : "Lolo",
    "Curso" : 2,
    "Notas" : [3,7,8,4]
},
    {
    "Nombre" : "Migue",
    "Curso" : 2,
    "Notas" : [7,4,9,1]
}
]
MostrarMedia(diccionario)
