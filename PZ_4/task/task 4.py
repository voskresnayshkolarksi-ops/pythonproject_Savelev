#  Найти и вывести на экран S=1!+2!+3!+4!+...+n! (n>1).
n = int(input("Введите число больше 1: "))

S = 0
factorial = 1

for i in range(1, n + 1):
    factorial *= i
    S += factorial

print("Сумма S = ", S)
