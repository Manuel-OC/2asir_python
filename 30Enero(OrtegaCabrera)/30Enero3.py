def VisualizarNoPrestados(l):
	for i in l:
		if i["prestado"]==False:
			print(i)

def ISBNPrestados(l):
	mistring=""

	for i in l:
		if i["prestado"]==True:
			mistring+=str(i["isbn"])
	
	return mistring

def Visualizar(r):
	print(r)

libros = [
	{
	"titulo" : "Así es la puta vida",
	"isbn" : 1234,
	"prestado" : True
	},
	{
	"titulo" : "El capitán Alatriste",
	"isbn" : 1235,
	"prestado" : False
	},
	{
	"titulo" : "No todo sobre el autismo",
	"isbn" : 1236,
	"prestado" : True
	},
	{
	"titulo" : "El libro Troll",
	"isbn" : 1234,
	"prestado" : False
	},
]

VisualizarNoPrestados(libros)
Visualizar(ISBNPrestados(libros))