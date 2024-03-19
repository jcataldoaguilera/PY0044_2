# Ejercicio Guiado

import sys, random
buscar = int(sys.argv[1]) # número a buscar

lista = [1,2,3,4,5,6,7,8,9,0]
# .shuffle de la librería random permite mezclar
# la lista de dígitos para aumentar un poco la dificultad.
random.shuffle(lista)

# revisaremos cada elemento en la lista
# también llevamos registro de la posición en la que estamos
for position, elemento in enumerate(lista):
# Si el elemento es igual a lo que buscamos terminamos el ciclo
    if elemento == buscar:
        print("¡Elemento encontrado! Se terminará del ciclo")
        break
else:
# Si es que no es el elemento buscado lo reportamos
    print("Elemento no encontrado")