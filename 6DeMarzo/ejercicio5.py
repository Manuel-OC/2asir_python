def CrearSuperlista(m,n,s,d):
	m.append(n)
	m.append(s)
	m.append(d)

	print(m)

def CrearDiccionario(dic,n,s,d):
	for i in range(0,len(n)):
		dic[n[i]] = {}
		dic[n[i]]['departamento'] = d[i]
		dic[n[i]]['sueldo'] = s[i]

def Visualizar(dic):
	for i in dic.keys():
		print(f"El empleado {i} del departamento {dic[i]['departamento']} cobra {dic[i]['sueldo']}")

nombres=['Manuel','Miguel','Ale']
departamentos=['Programacion','Redes','Programacion']
sueldos=[1200,1500,3000]

matriz=[]
diccionario={}

CrearSuperlista(matriz,nombres,sueldos,departamentos)
CrearDiccionario(diccionario,nombres,sueldos,departamentos)
Visualizar(diccionario)