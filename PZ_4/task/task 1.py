i = 0
num1 =int(input("Введите 1 число: "))
num2 =int(input("Введите 2 число: "))
num3 =int(input("Введите 3 число: "))
num4 =int(input("Введите 4 число: "))

sum =num1+num2+num3+num4

if num1 > 0:
    i += 1
if num2 > 0:
    i += 1
if num3 > 0:
    i += 1
if num4 > 0:
    i += 1

print(f"Сумма чисел равна {sum}. Количество отрицательных чисел равна {i}")