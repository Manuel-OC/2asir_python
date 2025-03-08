def CrearDiccionario(matriz):
	d={}
	for i in range(0,len(matriz)):
		d[matriz[i][0]] = matriz[i][1]
	print(d)

matriz=[
	[0,1],
	[2,3],
	[4,5],
]

CrearDiccionario(matriz)
