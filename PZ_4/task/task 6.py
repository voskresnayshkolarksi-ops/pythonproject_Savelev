N = int(input("Введите количество чисел: "))
k = 0

for i in range(N):
    num = int(input(f"Введите число {i + 1}: "))
    if num == 0:
        k += 1

print("Количество чисел равных нулю = ", k)