def esPerfecto(n):
    sum=0
    for i in range(n-1,0,-1):
        if n%i == 0:
            sum+=i

    if n == sum:
        return True
    else:
        return False

def BuscarPerfectos(lista):
    cont = 1
    i = 0
    for i in lista:
        if i < 10:
            print (f"Comprobando el {i}")
            if(esPerfecto(i)):
                print(f'Número perfecto {cont}: {i}')
                cont+=1
        i+=1

lista = [8,3,6,4,9,28]
BuscarPerfectos(lista)
