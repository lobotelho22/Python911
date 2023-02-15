PI = 3.14


def square(side):
    "Calculate Area of a square"
    return side ** 2


def rectangle(length, wide):
    "Calculate Area of a rectangle"
    return length * wide


def circle(radius):
    "Calculate Area of a circle"
    return PI * (radius ** 2)


print("Área de um quadrado de lado 10:", square(10))
print("Área de um retângulo de lados 10 e 5:", rectangle(10, 5))
print("Área de um círculo de raio 20:", circle(20))
