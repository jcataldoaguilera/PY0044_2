# Info
# Autor: Juan Cataldo [jcataldoaguilera@gmail.com]
# Fecha: 2024-04-05
# RLAB-23-02-09-0044-2
#

class Te():
    formato_300 = 3000
    formato_500 = 5000
    duracion = 365
    
    @staticmethod
    def tiempo_preparacion(sabor):
        if sabor == 1:
            return 3, 'Se recomienda consumir al desayuno.'
        elif sabor == 2:
            return 5, 'Se recomienda consumir al medio día.'
        elif sabor == 3:
            return 6, 'Se recomienda consumir al atardecer.'
    
    @staticmethod
    def precio(formato):
        if formato == 300:
            return Te.formato_300
        elif formato == 500:
            return Te.formato_500
        else:
            return 'Formato invalido'
        