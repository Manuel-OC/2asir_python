def DarLaVuelta(m):
	burbuja=0
	
	for i in range(0,len(m)):
		for j in range(0,len(m[i])-2):
			burbuja=m[i][j]
			m[i][j]=m[i][len(m[i])-j-1]
			m[i][len(m[i])-j-1]=burbuja

	return m

def Visualizar(r):
	for i in r:
		print(i)

mimatriz = [
	[1,2,3,4,5],
	[1,2,3,4,5],
	[1,2,3,4,5]
]

Visualizar(DarLaVuelta(mimatriz))