def Proceso(m,medias):
	contadores=[0,0,0,0]
	sumas=[0,0,0,0]

	for i in range(0,len(m)):
		for j in range(0,len(m[i])):
			if j%2==1:
				sumas[int(j/2)]+=m[i][j]
				contadores[int(j/2)]+=1

	print(sumas)
	print(contadores)
	for i in range(0,len(sumas)):
		medias.append(sumas[i]/contadores[i])

def Visualizar(medias):
	print(medias)

matriz=[
	[2,3,5,6,7,8],
	[1,2,3,4,5,6,7,8],
	[5,6,7,8]
]

medias=[]

Proceso(matriz,medias)
Visualizar(medias)