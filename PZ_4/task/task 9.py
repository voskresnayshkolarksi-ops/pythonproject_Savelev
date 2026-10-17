a1 = 1  # Первый элемент
d = 3   # Разность прогрессии
current_element = a1
count = 0

# Идем по прогрессии, пока элементы не превысят верхнюю границу
while current_element < 30:
    if current_element > 10:
        count += 1
        print(f"Элемент подходит: {current_element}")
    current_element += d  # Переходим к следующему элементу

print(f"Количество элементов: {count}")
