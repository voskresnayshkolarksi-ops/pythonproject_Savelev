N = int(input("Введите количество элементов прогрессии (N): "))

current_a = 1
i = 1

print("\nРезультаты обработки элементов:")

while i <= N:
    divided = current_a / 2
    rounded = round(divided)

    print(f"a{i} = {current_a}  =>  округлили: {rounded}")

    current_a += 3
    i += 1