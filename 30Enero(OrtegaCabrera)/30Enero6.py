def Visualizar(p):
	print(p["nombre"],p["edad"],p["contacto"]["email"],p["contacto"]["telefono"],p["direcciones"][0]["calle"],p["direcciones"][1]["ciudad"])

persona = {
	"nombre":"lolo",
	"edad":30,
	"contacto":{
		"email":"mortcab191@g.educaand.es",
		"telefono":666666666
	},
	"direcciones":[
		{
			"calle":"soroya 18"
		},
		{
			"ciudad":"Cádiz"
		}
	]
}

Visualizar(persona)