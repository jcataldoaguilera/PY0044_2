# Info
# Autor: Juan Cataldo [jcataldoaguilera@gmail.com]
# Fecha: 2024-04-05
# RLAB-23-02-09-0044-2
#

# Librerias
from te import Te

# Desarrollo
print(
    '''
    Seleccione el valor númerico del sabor del Té
    1 - Té Negro 
    2 - Té Verde
    3 - Agua de hierbas
    '''
)
sabor = int(input('Sabor: '))

print(
    '''
    Seleccione el formato del té (sólo numeros)
    300 - 300ml
    500 - 500ml
    '''
)
formato = int(input('Formato: '))

precio = Te.precio(formato)
tiempo, recomendacion = Te.tiempo_preparacion(sabor)

# Imprimir pedido
if sabor == 1:
    sabor = 'Té Negro'
elif sabor == 2:
    sabor = 'Té Verde'
elif sabor == 3:
    sabor = 'Agua de hierbas'

print(
    f'''
    Resumen del pedido:
    {sabor}
    {formato}ml
    ${precio}
    {tiempo} minutos
    {recomendacion}
    '''
)