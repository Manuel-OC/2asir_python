class Persona:
  def __init__(self, n, e):
    self.nombre = n
    self.edad = e

  def imprimirNombre(self):
    print(f"Hola mi nombre es {self.nombre} y mi edad es {self.edad}")

  def __str__(self):
    return f"{self.nombre} {self.edad}"

#Crear objetos
p1 = Persona("John", 36)
p2 = Persona("Lolo",29)

#Llamar a función
p1.imprimirNombre()
p2.imprimirNombre()

#Imprimir objetos mediante método string
print(p1)
print(p2)