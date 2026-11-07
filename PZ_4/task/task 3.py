#  Найти и вывести на экран квадраты и кубы чисел от 2 до 5.

num = 2
i = 0
k = 0

while k <= 4:
    i += 1
    k += 1
    kvadrat = num ** 2
    num += 1
    print(f"Числа в {i + 1} в квадрате {kvadrat}")

num = 2
k = 0
i = 0

while k <= 4:
    i += 1
    k += 1
    kybe = num ** 3
    num += 1
    print(f"Числа в {i + 1} в кубе {kybe}")

