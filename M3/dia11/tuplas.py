from os import system
###Tuplas => similar a las litas pero son inmutables (valor1,valor2...valorn)
tupla1 = 12,24,36,48,59
print(tupla1[0])
print(tupla1[1])
#tupla1[1]= "Mishi"

tupla_eje = ("Marzo", "2024")
print(tupla_eje)
print(type(tupla_eje))#<class 'tuple'>

#desempaquetamiento
mes, anio = tupla_eje
print(mes)
print(anio)

tupla2= 3,5,(1,11),7,9
print(type(tupla2))#<class 'tuple'>
print(tupla2)
system("clear")
lista_vocales = ["a","e","i","o","u","a","a","a"]
print(lista_vocales)#['a', 'e', 'i', 'o', 'u']
tupla_vocales = tuple(lista_vocales)
print(tupla_vocales)#('a', 'e', 'i', 'o', 'u')

#Iterar una tupla
for tv in tupla_vocales:
    print(tv)
    #
#count, cuenta la veces que se encuentra un elemento en la tupla
print(tupla_vocales.count("a"))

system("clear")
lista_dicc=list({"k1": 5, "k2": 7}.items()) 
print(lista_dicc)# [('k1', 5), ('k2', 7)]
print("")
print(lista_dicc[0])#accediendo a la tupla enla posicion cero
print(lista_dicc[0][0])#k1
print(lista_dicc[0][1])#5

print(lista_dicc[1])
print(lista_dicc[1][0])#k2
print(lista_dicc[1][1])#7

system("clear")

print(dir(lista_dicc))
system("clear")
print(dir(tupla_vocales))



