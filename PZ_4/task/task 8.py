print("A < B")
A = int(input("Введите число А: "))
B = int(input("Введите число B: "))
B += 1
S = 0

while A < B:
    B -= 1
    print(B)
    S += B

print("Сумма чисел = ", S)