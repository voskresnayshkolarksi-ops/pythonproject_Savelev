#Даны два числа. Вывести большее из них.
num1 = input("Введи первое число: ")
num2 = input("Введи второе число: ")

while True:
    try:
        num1 = float(num1)
        num2 = float(num2)
        break
    except ValueError:
        print("Вы ввели не число!!!!")
        num1 = input("Введи первое число: ")
        num2 = input("Введи второе число: ")

if num1 > num2:
    print(num1)
else:
    print(num2)