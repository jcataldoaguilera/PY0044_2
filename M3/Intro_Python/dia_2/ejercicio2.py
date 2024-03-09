# la separacion decimal de los float es un punto (.)
# la division entre int resulta en un float

print(4/2) # 2.0
print(5/2) # 2.5
print(5/3.5) # 1.4285714285714286
print(2.4*4) # 9.6

name = "Mijail"
year = "2024"

print(3*name) # repite 3 veces la variable name: MijailMijailMijail
print(year*2) # 20242024
# print(name/2) # no se puede dividir un str

# interpolacion de cadenas
month = 3
day = 7

print(f"Hola {name}, el año es {year} del mes {month} y el día {day}")

# string.format
print("".format())

print("Hola {}, el año es {} del mes {} y el día {}".format(name, year, month, day))

# interpolacion con % ($s para str y %d para int)
print("Hola %s, el año es %s del mes %d y el día %d" %(name, year, month, day))

# .count sirve para contar cuentas veces se encuentra un caracter en un str
print("Santana".count("a"))
print(name.count("i"))

# upper & lower
print(name.upper()) # devuelve una copia de la str en MAYUSCULAS
print(name.lower()) # devuelve una copia de la str en minusculas

# title
print("saNtANa".title()) # devuelve una copia de la str con la primera letra en Mayuscula (Santana)

# funcion len()
print(len(name)) # devuelve la cantidad de caracteres de una str
#print(len(month)) # no funciona sobre datos int

# join() permite unir muchos elementos separados en un str
print(", ".join(["a", "b", "c"]))

# imprimir en varias lineas (\n)
print("mostrar \nsalto \nde \nlinea")

# tipos de datos
peso = 88.5
verdadero = True

print(type(name))   # str
print(type(month))  # int
print(type(year))   # str
print(type(peso))   # float
print(type(verdadero))   # bool

type(verdadero) # esto no imprime el tipo de dato

# manipulacion de variables
numero = 2
numero = numero + 3 # numero = 2 + 3

# precision de datos
print(f"el resultado de la division: {5/9:.2f}")
print("el resultado de la division:", round(5/9,3))

# ingresando datos
nombre = input("Ingrese su nombre: ")
print("Su nombre es: ", nombre)