def Completo(d):
    comp = True
    for clave, valor in d.items():
        for asiento in valor.keys():
            if valor[asiento] == 0:
                comp = False
    return comp

def Estado(d):
    print("Asi vamos: ")
    for clave, valor in d.items():
        cont = 0
        for valor2 in valor.values():
            cont+=1
            if valor2 == 0:
                print(f"{clave} butaca{cont} libre")
            else:
                print(f"{clave} butaca{cont} ocupado")

def Principal(teatro,filas,butacas):
    while True:
        fila=input("Inserte una fila")
        columna=input("Inserte una columna")
        
        if fila in filas and columna in butacas:
            if teatro[fila][columna] == 0:
                teatro[fila][columna] = 1
            else:
                print (f"La butaca {columna} de la fila {fila} esta ocupada")
            if Completo(teatro):
                break        
        else:
            print("La fila o la butaca no son válidas")
        
        Estado(teatro)
        
    print("Teatro lleno")

teatro = {
    'fila1':{
        'butaca1':0,
        'butaca2':0,
        'butaca3':0
    },
    'fila2':{
        'butaca1':0,
        'butaca2':0,
        'butaca3':0
    },
    'fila3':{
        'butaca1':0,
        'butaca2':0,
        'butaca3':0
    }
}

filas=['fila1','fila2','fila3']
butacas=['butaca1','butaca2','butaca3']

Principal(teatro,filas,butacas)