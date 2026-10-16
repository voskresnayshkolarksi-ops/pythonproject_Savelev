N = int(input("Введите количество чисел: "))
Sum = 0

for i in range(N):
    num = int(input(f"Введите число {i + 1}: "))
    Sum += num

if Sum > 0:
    arif_znach = Sum / N
    print(arif_znach)
else:
    print("Введите количество чисел больше 0")