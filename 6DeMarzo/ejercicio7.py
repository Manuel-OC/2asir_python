def Proceso(repetidos,m):
	aux=[]
	for i in range(0,len(m)):
		for j in range(0,len(m[i])):
			if m[i][j] in aux and m[i][j]%2==1:
				repetidos.append(m[i][j])
			else:
				aux.append(m[i][j])


def Anular(m,r):
	for i in range(0,len(m)):
		for j in range(0,len(m[i])):
			if m[i][j] in r:
				m[i][j]=0 
	print(m)

m = [
	[7,4,9],
	[2,8,3],
	[9,1,7],
]
repetidos=[]
Proceso(repetidos,m)
Anular(m,repetidos)