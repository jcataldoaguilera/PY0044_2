from os import system



""" 
Funciones

Si una funcion no se invoca, NUNCA se ejecutara el código en su interior
es imperativo utilizar (), en el llamado a la función

def nombre_de_la_funcion(variable):
    #codigo a ejecutar
    
nombre_de_la_funcion(3)

parametro, variable a utilizar en la funcion
argumento, valor que sera pasado en el llamado de la función

cuando hacemos un retorno multiple, se retorna una tupla

"""
print("Inicio")
#imprimir_menu() #no se puede llamar a una funcion que no este definida previamente

#definicion de la funcion
def imprimir_menu():
    print("Opciones: ")
    print("1). De acuerdo")
    print("2). En desacuerdo")
    print("3). No me interesa")

#llamado a la funcion (invocación)
imprimir_menu()
imprimir_menu()
imprimir_menu()
print("Fin")

system("clear")
def suma(valor1,valor2):#valor1=3 ; valor2=5
    suma = valor1 + valor2 # suma= 3 + 5; suma = 8
    return suma #return 8

def suma2(valor1,valor2):
    return valor1 + valor2
    print("qwerty123456")#nunca se ejecutara

suma(3,5)

print("valor de respuesta",suma2(1,9))#se imprime el valor de retorno

resultado = suma2(6,7)#capturando el valor de retorno
print("valor respuesta capturado",resultado)#imprimiendo el valor de retorno


system("clear")
#RETORNO MULTIPLE
def cuadrado_cubo(base):
    cuadrado = base ** 2
    cubo = base  ** 3
    return cuadrado, cubo

print(cuadrado_cubo(2))#retorno de una tupla (4, 8)

valor_cuadrado,valor_cubo = cuadrado_cubo(3)#(9,27)
print(valor_cuadrado,valor_cubo)



def filtrar(diccionario, umbral):#diccionario = precios
    filtro = {k:v for k,v in diccionario.items() if v > umbral}
    return filtro


precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
}

print(filtrar(precios, 25000))
system("clear")

#PARAMETROS OBLIGATORIOS
def extremo_multiplicado(lista,factor):
    minimo = min(lista)
    maximo = max(lista)
    return factor*minimo, factor*maximo

#print(extremo_multiplicado(4,[1,2,3,4]))#error de elementos

print(extremo_multiplicado([1,2,3,4], 4))

# se entregan en orden
print(extremo_multiplicado(factor = 4, lista = [1,2,3,4]))


#PARAMETROS OPCIONALES O POR DEFAULT
def elevar(base, exponente, redondear = False):
    if redondear:
        valor = round(base**exponente,2)
    else:
        valor = base**exponente
    return valor

print(elevar(2, 3))#19.241905543136184

print(elevar(2, 3, redondear = True))#19.24

system("clear")

# **KWARGS -> se recibe un diccionario  
def parametros(**kwargs):
    print(kwargs)
    print(kwargs["lista1"])

parametros(numero1= 23, texto ="Hola", lista1 = [2,3,4,5,6])

print("")
# *ARGS -> se recibe una tupla
def argumentos(*args):
    print(args)
    print(args[0])#23
    print(args[2])#[2,3,4,5,6]
    
argumentos(23,"hola",[2,3,4,5,6])

system("clear")

#VARIABLES LOCALES Y VARIABLES GLOBALES

pais = "Chile"#variable global
#constantes
G = 9.8
PI = 3.14
IVA = 19

def ciudades():
    #scope de la variable "capital" es solo en el metodo ciudades()
    capital = "Santiago"
    print(pais, capital)
    #pais= "Peru" # no se puede/recomiendo modificar el valor de una variable global

    return capital # return "Santiago"
    
print(pais)
ciudades()
#print(capital)#variable no definida
print(pais)