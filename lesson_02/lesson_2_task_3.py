import math


def square(side):
    return math.ceil(side * side)


side = float(input("Длина стороны квадрата: "))
print(f"Площадь квадрата: {square(side)}")
