num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

num = num1 * num2

if num < 0:
    print(num * 8)
else:
    print(num * 1.5)