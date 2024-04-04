class Pelota(): # definicion de clase
    posiciones = [3, 0, 2, 1, 0] # atributos de clase
    
    @staticmethod # decorador para metodos estáticos
    def crear_rebote(): # definicion de método estático
        return [5, 0, 4, 0, 3, 0, 2, 0, 1, 0]
    
    @staticmethod
    def imprimir_posiciones():
        Pelota.crear_rebote()
        print(Pelota.posiciones)