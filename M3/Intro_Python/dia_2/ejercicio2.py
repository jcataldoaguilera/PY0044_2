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
