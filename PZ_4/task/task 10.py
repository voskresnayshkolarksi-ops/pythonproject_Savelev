progression = []
current = 1

while len(progression) < 10:
    progression.append(current)
    current += 3

print(f"Исходная прогрессия: {progression}")

results = []
i = 0

while i < len(progression):
    rounded_val = round(progression[i] / 2)
    results.append(rounded_val)
    i += 1

print(f"Результат после деления и округления: {results}")
