"""
DICCIONARIOS
PAR -> {CLAVE:VALOR}
la clave debe ser UNICA=> si existe duplicidad, retorna solo la ultima referencia de valor
"""
#diccionario vacio
notas = {}
#creacion de un diccionario
notas = {#
    "Camila": 7, 
    "Antonio": 7, 
    "Felipe": 6, 
    "Antonia": 7,
    "Antonia": 6,
    }

print(notas)#{'Camila': 7, 'Antonio': 7, 'Felipe': 6, 'Antonia': 6}

#Acceder a los valores del diccionario
print(notas["Camila"]) # 7
print(notas["Antonio"])# 7
print(notas["Felipe"]) # 6
print(notas["Antonia"])# 6; 7
#print(notas["Mijail"]) # KeyError: 'Mijail'
#print(notas["felipe"]) # KeyError: 'felipe'

#Agregar par clave:valor al diccionario 
#diccionario[clave]= valor
notas["Mijail"]= 7
print(notas)#{'Camila': 7, 'Antonio': 7, 'Felipe': 6, 'Antonia': 6, 'Mijail': 7}
notas["Julio"]= 7
print(notas)#{'Camila': 7, 'Antonio': 7, 'Felipe': 6, 'Antonia': 6, 'Mijail': 7, 'Julio': 7}

#Cambiar el valor a una clave
notas["Felipe"]= 7
print(notas)#{'Camila': 7, 'Antonio': 7, 'Felipe': 7, 'Antonia': 6, 'Mijail': 7, 'Julio': 7}

#Eliminar elementos
del notas["Antonia"]
print(notas)#{'Camila': 7, 'Antonio': 7, 'Felipe': 7, 'Mijail': 7, 'Julio': 7}

#pop-> al eliminar, permite capturar el elemento
eliminado = notas.pop("Antonio")
print(eliminado) #7
print(notas)#{'Camila': 7, 'Felipe': 7, 'Mijail': 7, 'Julio': 7}

notas2 ={
    "Alexis": 6,
    "Yasna": 6,
    "Camila": 3,
}

#Union de dos diccionarios-> 
#notas.update(notas2)
#print(notas)
#{'Camila': 7, 'Felipe': 7, 'Mijail': 7, 'Julio': 7, 'Alexis': 6, 'Yasna': 6}
#CUDADO colision de igualdad de llaves
#{'Camila': 3, 'Felipe': 7, 'Mijail': 7, 'Julio': 7, 'Alexis': 6, 'Yasna': 6}

notas2.update(notas)
print(notas2)#{'Alexis': 6, 'Yasna': 6, 'Camila': 7, 'Felipe': 7, 'Mijail': 7, 'Julio': 7}

