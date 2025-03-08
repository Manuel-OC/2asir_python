def Entrada(alumnos):
	n=int(input("Introduzca el numero de alumnos"))
	cont=0
	while cont < n:
		nom=str(input("Introduzca nombre"))
		notas=[]
		claves=alumnos.keys()
		if nom in claves:
			print("ERROR el alumno {nom} ya existe")
		else:
			nota = 0
			while nota >= 0:
				nota=int(input(f"Introduca una nota para {nom} (negativo para salir)"))
				notas.append(nota)
			alumnos[nom]=notas
			cont+=1

def Medias(alumnos):
	for clave,valor in alumnos.items():
		media = sum(valor)/(len(valor)-1)
		print (f"La media de {clave} es {media}")

alumnos = {}

Entrada(alumnos)
Medias(alumnos)