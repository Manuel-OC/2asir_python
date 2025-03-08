def Entrada(vect):
	cont=0
	while cont<8:
		aux=int(input("Introduzca un multiplo de 7"))
		if aux%7==0:
			vect[cont] = aux
			cont+=1

def Visualizar(r):
	for i in range(0,len(r)):
		print(r[i])

def Visualizar2(r):
	r.reverse()
	for i in range(0,len(r)):
		if r[i]%2==0:
			print(r[i])

vect=[0,0,0,0,0,0,0,0]
Entrada(vect)
Visualizar(vect)
Visualizar2(vect)