#Напишите функцию square, принимающую один аргумент — сторону квадрата —
# и возвращающую площадь квадрата, округлить вверх до целого числа

import math

def squre(side):
    return math.ceil(math.pow(side,2))

n_side = int(input("Введите длину стороны квадрата: "))
print(f"Площадь квадрата: {squre(n_side)}")
