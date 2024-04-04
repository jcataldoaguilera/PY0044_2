"""
lista: conjunto de datos, ordenados segun su ingreso, separados por coma, 
el primer elemento, esta en la posicion cero, pueden contener distintos tipos de elementos
son mutables
se usan los [] para definir una variable de tipo lista
**indice => la posicion de los elementos

la primera posicion SIEMPRE es CERO
la ultima posicion esta dada por ultimaPosicion= (cantidad_elementos - 1) o lista[-1]
para acceder a los elementos utilizamos las posiciones; lista[posicion]
no existen indices sin elementos en python
los metodos con __nombre__, se les llama magic built-in o dunders
"""

lista1 =[1,2,3,4]
print(f" la lista es: {lista1}")
print(f" nueva lista {[5,"Hola Mundo",7]}")

colores = ["verde", "rojo", "rosa","azul"]
#cuantos elementos tiene:4 -> el tamaño de la lista
#la ultima posicion = 4-1 -> 3
print(colores[0])#verde
print(colores[1])
print(colores[2])
print(colores[3])
#print(colores[4]) #IndexError: list index out of range
print(colores[-1])#azul
print(colores[-2])#rosa
#print(colores[-5])#IndexError: list index out of range


## METODOS ##
#print(colores.__dir__())#mostrar todos los metodos que contiene la lista

#append() -> agregar un elemento al final de lista
colores.append("amarillo")#agregar un elemento
print(colores)#['verde', 'rojo', 'rosa', 'azul', 'amarillo']

#insert(indice, elemento)-> agregar el elemento en una posicion especifica 
# y si esta utilizada por otro elemento, este es desplazado en una posicion mas
colores.insert(0, "blanco")
print(colores)#['blanco', 'verde', 'rojo', 'rosa', 'azul', 'amarillo']
colores.insert(6, "negro")#agregar en la posicion final
print(colores)#['blanco', 'verde', 'rojo', 'rosa', 'azul', 'amarillo', 'negro']
colores.insert(18, "cafe")# si la indice no existe, le asigna la ultima posicion
print(colores)#['blanco', 'verde', 'rojo', 'rosa', 'azul', 'amarillo', 'negro', 'cafe']
colores.insert(0, "cafe")



#pop([indice])-> elimina un elemento dentro de la lista
colores.pop(3) #elimina el color rosa de la lista
print(colores)#[ 'cafe','blanco', 'verde', 'rojo', 'azul', 'amarillo', 'negro','cafe']

#remove()=> eliminar un elemento especifico, pero el primero que encuentre
colores.remove("cafe")#
print(colores)#['blanco', 'verde', 'rosa', 'azul', 'amarillo', 'negro', 'cafe']
#colores.remove("cafes")#ValueError: list.remove(x): x not in list

#reverse() => invierte el orden de los elementos de la lista,permanente
colores.reverse()
print(colores)#['cafe', 'negro', 'amarillo', 'azul', 'rosa', 'verde', 'blanco']

#sort()-> organiza los elementos de manera ascendente/alfabetico por defecto
colores.sort()
print(colores)#['amarillo', 'azul', 'blanco', 'cafe', 'negro', 'rosa', 'verde']

lista2 = lista1 #ESTO NO ES UN RESPALDO DE LA LISTA 

lista3 = lista1.copy()#SI ES UN RESPALDO DE LOS DATOS
lista4 = lista1[:]    #SI ES UN RESPALDO DE LOS DATOS(slice)
lista5 = list(lista1) #SI ES UN RESPALDO DE LOS DATOS
lista7 = lista1 + []
lista8 = lista1 * 1

print(lista2)
lista2.append(5)
print(f"lista 2 {lista2}")
print(f"lista 1 {lista1}")
print(f"lista 3 {lista3}")
print(f"lista 4 {lista4}")
print(f"lista 5 {lista5}")

#sorted(lista, reverse= True) -> ordena descendentemente, no es permanente
print(sorted(colores,reverse=True))#['verde', 'rosa', 'negro', 'cafe', 'blanco', 'azul', 'amarillo']
print(sorted(colores))#['amarillo', 'azul', 'blanco', 'cafe', 'negro', 'rosa', 'verde']
print(colores)#['amarillo', 'azul', 'blanco', 'cafe', 'negro', 'rosa', 'verde']

#index()-> retorna el indice del elemento existente en le lista
print(colores.index('azul'))#1
print(colores.index('negro'))#4
#print(colores.index('pink'))# ValueError: 'pink' is not in list

#colores.clear() # eliminar TODOS los elementos de la lista
print(colores)#lista vacia 
print(len(colores))#0

## OPERACIONES ##
lista6 = [20,30,40,50]

lista_concatenada = lista1 + lista6
print(lista1)
print(lista6)
print(lista7)
print(lista8)
print(lista_concatenada)
lista6.append(60)
print(lista_concatenada)