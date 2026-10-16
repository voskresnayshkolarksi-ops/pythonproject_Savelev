i = 0
num1 =int(input("Введите 1 число: "))
num2 =int(input("Введите 2 число: "))
num3 =int(input("Введите 3 число: "))
num4 =int(input("Введите 4 число: "))

if num1 % 2 == 0:
    i += 1
if num2 % 2 == 0:
    i += 1
if num3 % 2 == 0:
    i += 1
if num4 % 2 == 0:
    i += 1

print(f"Количество четных чисел равна {i}")