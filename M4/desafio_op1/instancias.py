# Info
# Autor: Juan Cataldo [jcataldoaguilera@gmail.com]
# Fecha: 2024-04-05
# RLAB-23-02-09-0044-2
#

# Librerias
from te import Te

# Cree dos instancias
t1 = Te()
t2 = Te()

# Almacene el tipo de dato de cada instancia creada en una variable 
t1_type = type(t1)
t2_type = type(t2)

# Muestre por pantalla, usando print(), el valor de cada tipo de dato
# almacenado.
print(t1_type)
print(t2_type)

# En caso de que ambos tipos almacenados sean iguales, muestre por pantalla,
# usando print(), el mensaje “Ambos objetos son del mismo tipo”. En caso
# contrario, mostrar mensaje “Los objetos no son del mismo tipo”.
if t1_type == t2_type:
    print('Ambos objetos son del mismo tipo')
else:
    print('Los objetos no son del mismo tipo')