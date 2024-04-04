from os import system
notas = {
    "Camila": 7, 
    "Antonio": 7, 
    "Felipe": 6, 
    "felipe":7,
    "Antonia": 6,
    }

print(notas)#{'Camila': 7, 'Antonio': 7, 'Felipe': 6, 'Antonia': 6}
print(len(notas))#4

#print(notas[2])#KeyError: 2
#print(notas["FELIPE"])#KeyError: 'FElipe'
print(notas.get("FELIPE")) #None
print(notas["Felipe"])#6
print(notas.get("Camila"))# 7
print(notas.get("Mijail","valor no encontrado"))# valor no encontrado

prueba = notas.get("Julio")
print(prueba)#None
print(type(prueba))#<class 'NoneType'>

#agregar
notas["Israel"]= "FullStack Python"
print(notas)
#{'Camila': 7, 'Antonio': 7, 'Felipe': 6, 'felipe': 7, 'Antonia': 6, 'Israel': 'FullStack Python'}
notas["Israel"]= 4
print(notas)
print("")
notas.setdefault("Juan",10)
print(notas)
#{'Camila': 7, 'Antonio': 7, 'Felipe': 6, 'felipe': 7, 'Antonia': 6, 'Israel': 4, 'Juan': 10}
print("")
notas.setdefault("Juan",2)
#si la clave existe, retorna el valor actual, NO LO REEMPLAZA
print(notas.setdefault("Juan",2))
print(notas)

print("")
notas.setdefault("Valeria")
print(notas)
#{'Camila': 7, 'Antonio': 7, 'Felipe': 6, 'felipe': 7, 'Antonia': 6, 'Israel': 4, 'Juan': 10, 'Valeria': None}

print("")
del notas["felipe"]
print(notas)
print("")
eliminado = notas.pop("Antonio")
print(eliminado,notas)
eliminados={}
#eliminados = eliminados.setdefault(notas.pop("Camila"))
eliminados["Camila"]=notas.pop("Camila")
print(notas)#{'Felipe': 6, 'Antonia': 6, 'Israel': 4, 'Juan': 10, 'Valeria': None}
print(eliminados)#{'Camila': 7}

print("")
tupla1=notas.popitem()#elimina y devuelve la tupla(clave:valor)
print(tupla1)
print(notas)#
###Tuplas => similar a las litas pero son inmutables (valor1,valor2...valorn)
print(tupla1[0])
print(tupla1[1])
#tupla1[1]= "Mishi"

notas.clear()#elimina los elementos, dejando un diccionario vacio
print(notas)#

###Comparar diccionarios
dic1 = {1:"uno",2:"dos"}
dic2 = {2:"dos",1:"uno"}
dic3 = {2:"dos",3:"tres"}
dic4 = {2:"dos",3:"cuatro"}
print(dic1==dic2) #True
print(dic1==dic3) #False
print(dic4==dic3) #False

##Diccionarios Anidados
system("clear")#system("cls")

pares_impares ={
    "pares":{
        2:"dos",
        4:"cuatro",
        6:"seis",
        8:"ocho",
        10:"diez",
    },
    "impar":{"uno":1,"tres":3,"cinco":5,"siete":7,"nueve":9},
} 
print(pares_impares)
#imprimir el valor "seis"
print(pares_impares["pares"])#{2: 'dos', 4: 'cuatro', 6: 'seis', 8: 'ocho', 10: 'diez'}
print(pares_impares["pares"][6])#'seis'
#imprimir el valor 5
print(pares_impares["impar"])#{'uno': 1, 'tres': 3, 'cinco': 5, 'siete': 7, 'nueve': 9}
print(pares_impares["impar"]["cinco"])#5