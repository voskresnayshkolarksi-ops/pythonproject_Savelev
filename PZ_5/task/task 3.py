# Написать программу, подсчитывающую количество цифр числа, используя для этого функцию.

def digits(number):
    count = 0
    if number == 0:
        return 1

    while number > 0:
        number //= 10
        count += 1
    return count

num = int(input("Введите число: "))
print("Цифр в числе:", digits(num))

