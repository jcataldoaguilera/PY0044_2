# Crear diccionario

paises = {
    "Alemania": "Berlin",
    "Paises Bajos": "Amsterdam",
    "Perú": "Lima"
}

print(paises)

# Agregar elementos

paises["Chile"] = "Santiago"
paises["Egipto"] = "El Cairo"
paises["Irak"] = "Teherán" # dato erroneo

print(paises)

# Modificar elemento
paises["Irak"] = "Bagdad"

print(paises)

# Eliminar elemento
deleted = paises.pop("Chile")

print(deleted)
print(paises)
