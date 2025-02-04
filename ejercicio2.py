def solicitarDatos():
    return int(input("Introduce el número"))

def esPerfecto(n):
    sum=0
    for i in range(n-1,0,-1):
        if n%i == 0:
            sum+=i

    if n == sum:
        return True
    else:
        return False
        
def Visualizar(r):
    if r:
        print("Es perfecto")
    else:
        print("No es perfecto")

n = solicitarDatos()
Visualizar(esPerfecto(n))
