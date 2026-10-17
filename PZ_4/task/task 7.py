print("A < B")
A = int(input("Введите число А: "))
B = int(input("Введите число B: "))
B += 1
i = 0

while A < B:
    B -= 1
    print(B)
    i += 1

print("Количество чисел = ", i)