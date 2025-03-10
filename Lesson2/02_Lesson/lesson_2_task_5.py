# Напишите функцию month_to_season(), которая принимает один аргумент — номер месяца —
# и возвращает название сезона, к которому относится этот месяц.
# Например, передаем 2, на выходе получаем «Зима»

month = int(input("Введите номер месяца:"))

def month_to_season(month):
    if month in [12, 1, 2]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    elif month in [9, 10, 11]:
        return "Осень"

season = month_to_season(month)
print(f"Месяц {month}: {season}")