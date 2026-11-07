#  Даны три целых числа. Определить у какого числа больше сумма цифр. Вывод
# результата предусмотреть в основной программе. Расчет суммы цифр оформить в
# функции.

def sum_of_digits(number):
    number = abs(number)
    digit_sum = 0
    while number > 0:
        digit_sum += number % 10
        number //= 10
    return digit_sum

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

sum1 = sum_of_digits(num1)
sum2 = sum_of_digits(num2)
sum3 = sum_of_digits(num3)

if sum1 >= sum2 and sum1 >= sum3:
    best_num = num1
    max_sum = sum1
elif sum2 >= sum1 and sum2 >= sum3:
    best_num = num2
    max_sum = sum2
else:
    best_num = num3
    max_sum = sum3

print(f"Наибольшая сумма цифр у числа {best_num} его сумма равна {max_sum}")
