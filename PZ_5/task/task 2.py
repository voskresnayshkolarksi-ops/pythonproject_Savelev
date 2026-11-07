# Рассчитать и вывести периметр и площадь прямоугольника. Расчеты оформить в функции.

def get_P(a, b):
    return 2 * (a + b)

def get_S(a, b):
    return a * b

width = float(input("Введите ширину прямоугольника: "))
height = float(input("Введите высоту прямоугольника: "))

print("Периметр:", get_P(width, height))
print("Площадь:", get_S(width, height))
