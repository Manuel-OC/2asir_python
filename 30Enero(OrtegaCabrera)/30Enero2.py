def Media(m):
    return (sum(m) / len(m))

vectorindexado = [400,35,60,450]
vectorasociativo = {"nombre": "Juan",
        "edad": 25,
        "ciudad": "Madrid"}
        
vectorasociativo["mediaventas"] = Media(vectorindexado)
print (vectorasociativo)
