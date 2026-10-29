# Дано вещественное число X (X|<1) и целое число N (>0). Найти значение выражения
# X - X3/3 + X5/5 - ... + (-1)NX2N+1/(2N +1). Полученное число является приближенным
# значением функции arctg в точке Х.

while True:
    try:
        X = float(input("Введите вещественное число по модулю меньше 1:  "))
        N = int(input("Введите целое число больше 0: "))
        if abs(X) < 1 and N > 0:
            break
        else:
            print("Вы неправильно ввели числа!!! ")
            X = float(input("Введите вещественное число по модулю меньше 1:  "))
            N = int(input("Введите целое число больше 0: "))

    except ValueError:
        print("Вы ввели не число!!!")

num = 0.0
current_pow = X
znak = 1

i = 0
while i <= N:
    denominator = 2 * i + 1
    term = znak * current_pow / denominator
    num += term
    current_pow *= X * X
    znak = -znak
    i += 1

print("приближенным значением функции arctg в точке Х = ",num)
