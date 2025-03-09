# Напишите функцию min_boxes, которая принимает одно число — количество предметов —
# и возвращает минимальное количество коробок, необходимых для упаковки этих предметов,
# если в одну коробку помещается не более пяти предметов.
# Используйте функцию ceil из модуля math, чтобы округлить количество коробок до ближайшего целого числа вверх.

import math

def min_boxes(items):
    return math.ceil(items / 5)

n_items = int(input("Введите количество предметов: "))
print(f"Минимальное количество коробок: {min_boxes(n_items)}")