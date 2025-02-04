def solicitarDatos():
    x = float(input('Introduce nota'))
    return x

def Media(n1,n2):
    return (n1+n2)/2

def estaAprobado(n):
    if n >= 5:
        print(f'Está aprobado con una media de {n}')
    else:
        print(f'Está suspenso con una media de {n}')

nota1 = solicitarDatos()
nota2 = solicitarDatos()

estaAprobado(Media(nota1,nota2))
