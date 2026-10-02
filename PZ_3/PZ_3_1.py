# Дано трехзначное число. Проверить истинность высказывания:
# «Цифры данного числа образуют возрастающую последовательность»

num = input("Введите трехзначное число: ")

while True:
    try:
        num = int(num)
        break
    except ValueError:
        print("Вы ввели не число!!!")
        num = input("Введите трехзначное число: ")

num1 = num // 100
num2 = (num // 10) % 10
num3 = num  % 10

if num1 < num2 < num3:
    print("True")
else:
    print("False")