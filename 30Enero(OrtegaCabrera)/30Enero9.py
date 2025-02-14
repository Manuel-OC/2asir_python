#-------------------------------- FUNCIONES ------------------------------

def Proceso (matriz):
	tab_resul = []
	for fila in matriz:
		tab_resul.append(Ultimo_fila(fila))
	return tab_resul

def Ultimo_fila(tab):
	return tab[len(tab)-1]

def Visualizar (tab):
	for valor in tab:
		print(valor)

#-------------------------------- PROGRAMA PRINCIPAL ------------------------------

matriz = [
	[1,2,3,4,5,6],
	[1,2,3,4,5,6,7],
	[1,2,3,4,5,6,7,8]
]

resul = Proceso(matriz)
Visualizar(resul)