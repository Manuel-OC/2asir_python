def solicitarDatos():
    return int(input("Introduce el número"))

def Suma(n1,n2):
    sum=n1+n2
    return sum
    
def Producto(n1,n2):
    prod=n1*n2
    return prod

def Comparar(s,p):
    if p > s:
        return "El producto es mayor que la suma"
    elif p < s:
        return "La suma es mayor que el producto"
    else:
        return "El producto y la suma son iguales"

def Visualizar(s):
    print (f"{s}")

n1 = solicitarDatos()
n2 = solicitarDatos()
Visualizar(Comparar(Suma(n1,n2),Producto(n1,n2)))
