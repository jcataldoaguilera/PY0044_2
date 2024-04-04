def dividir(dividendo, divisor):
    return dividendo/divisor

if __name__ == '__main__':
    print("name ",__name__,__file__,__package__)
    resultado = dividir(14,2)#7.0
    print(f"El resultado de la division es {resultado}")