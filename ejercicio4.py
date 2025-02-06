def solicitarDatos():
    return int(input("Introduce el número"))

def LaSumaEs(n1,n2):
    if (n1+n2) > 0:
        return "La suma es positiva"
    elif (n1+n2) < 0:
        return "La suma es negativa"
    else:
        return "La suma es 0"

def Visualizar(s):
    print (f"{s}")

n1 = solicitarDatos()
n2 = solicitarDatos()
Visualizar(LaSumaEs(n1,n2))
