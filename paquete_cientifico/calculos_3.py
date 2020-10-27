# calculadora de porcentajes de una cantidad
def porcentaje_cantidad(porcentaje, cantidad):
    porcentaje_cantidad = porcentaje*cantidad/100
    return porcentaje_cantidad


# calcula la cantidad total dado un porcentaje
def cantidad_porcentaje(porcentaje, cantidad):
    total = porcentaje*cantidad/10
    return total


if __name__ == "__main__":
    porcentaje = 10
    cantidad = 100
    print(str(porcentaje_cantidad(porcentaje, cantidad))+'%')
    print(cantidad_porcentaje(porcentaje, cantidad))
