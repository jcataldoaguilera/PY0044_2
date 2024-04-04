""" 
import getpass
password = getpass.getpass("Ingresa el password: ")
#print(f"el password capturado {password}")
#hola
while password != "hola mundo":
    password = getpass.getpass("Error, Ingresa el password nuevamente: ")
    
print("Fin del programa")

numero = int(input("Ingrese un numero entero del 1 al 100\n"))

while numero < 1 or numero > 100: ]1,100[
    numero = int(input("Ingrese un numero entero del 1 al 100\n"))


while numero != 33:
    numero = int(input("Reingrese un numero entero del 1 al 100\n"))
    
print("Fin del programa")

"""

inicio = 0
fin = 6

while inicio < fin:
    print(f" inicio {inicio} , fin {fin}")
    inicio = inicio + 1
    
print("fin del while")