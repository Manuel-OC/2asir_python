def Proceso(matriz):
	for i in range(1,len(matriz)-1):
		for j in range(1,len(matriz[i])-1):
			if matriz[i][j]%matriz[i-1][j]==0 and matriz[i+1][j]%matriz[i-1][j]==0 and matriz[i][j-1]%matriz[i-1][j]==0 and matriz[i][j+1]%matriz[i-1][j]==0:
				print(matriz[i])

matriz = [
	[4,7,9,45],
	[1,5,6,3],
	[20,30,10,3],
	[7,15,3,477],
	[5,40,30,10]
]

Proceso(matriz)