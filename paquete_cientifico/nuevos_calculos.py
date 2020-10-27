def area_circulo(radio):
    area = radio**2*3.14
    return area


def perimetro_circulo(radio):
    perimetro = radio*2*3.14
    return perimetro


def area_triangulo(base, altura):
    area = base*altura/2
    return area


def perimetro_triangulo(base, altura):
    # se debe sacar la raiz cuadrada de la base y altura elevadas a dos
    lado = ((base*base)+(altura*altura))**(0.5)
    perimetro = lado+base+altura
    return perimetro


def area_rectangulo(base, altura):
    area = base*altura
    return area


def perimetro_rectangulo(base, altura):
    perimetro = (base+altura)*2
    return perimetro


def distancia(tiempo, velocidad):
    distancia = tiempo*(velocidad/3.6)
    return distancia


if __name__ == "__main__":
    # area y perimeto de un circulo
    radio = 7
    print('El area del circulo: ')
    print(area_circulo(radio))
    print('El perimetro del circulo: ')
    print(perimetro_circulo(radio))

    # ·area y perimetro de un triangulo dados su base y altura
    baseT = 9
    alturaT = 12
    print('El area del triangulo es: ')
    print(area_triangulo(baseT, alturaT))
    print('El perimetro del triangulo es: ')
    print(perimetro_triangulo(baseT, alturaT))

    # area y perimetro de un rectangulo dados sus lados
    baseR = 10
    alturaR = 5
    print('El area del rectangulo es: ')
    print(area_rectangulo(baseR, alturaR))
    print('El perimetro del rectangulo es: ')
    print(perimetro_rectangulo(baseR, alturaR))

    """
    Distancia cdados el tiempo y velocidad, 
    para este ejemplo se mide el tiempo en segundos y la velocidad en km/h
    dando como resultado la distancia en mts.
    """
    tiempo = 10
    velocidad = 180
    print("La distancia recorrida es : ")
    print(str(distancia(tiempo, velocidad))+' metros')
