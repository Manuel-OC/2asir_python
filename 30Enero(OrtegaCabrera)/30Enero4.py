def Funcion(v1,v2):

	v2.append(v1[0])

	for i in range(1,len(v1)):
		if v1[i] >= v2[len(v2)-1]:
			v2.append(v1[i])

	return v2

def Visualizar(r):
	print(r)

vector1 = [4,6,9,10,2,4,8,16,9,3,1,20]
vector2 = []

Visualizar(Funcion(vector1,vector2))