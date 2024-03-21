"""
Listas
Son mutabes; pueden cambiar ; pueden contener distintos tipos de datos
lista = [elemento1, elemento2, elemento3, elementoN]

"""

lista1 = [1,2,3,4]
print(f"La lista es {lista1}")

colores = ["verde", "rojo", "rosa", "azul"]

print(colores[0])
print(colores[1])
print(colores[2])
print(colores[3])
print(colores[-1])
print(colores[-2])

# METODOS
print(colores.__dir__()) # muestra todos los metodos que contiene la lista

# append(elemento)
colores.append("amarillo")
print(colores)

# insert(indice,elemento)
colores.insert(0,"blanco")
print(colores)
colores.insert(6,"negro")
print(colores)
colores.insert(-1,"cafe")
print(colores)

# pop(indice)
colores.pop(0)
print(colores)
colores.pop(3)
print(colores)

# remove(elemento)
colores.remove("cafe") # elimina la primera coincidencia que encuentra
print(colores)

# reverse
colores.reverse() # invierte el orden de los elementos de forma permanente
print(colores)

# sort
colores.sort() # organiza los elementos de manera ascendente
print(colores)

# Respaldo de datos
lista2 = lista1.copy