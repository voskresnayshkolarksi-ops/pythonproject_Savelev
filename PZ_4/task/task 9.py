# 9. Посчитать и вывести количество элементов арифметической прогрессии,
# удовлетворяющих условию 10<ai<30.

a1 = 1
d = 3
current_element = a1
count = 0


while current_element < 30:
    if current_element > 10:
        count += 1
        print(f"Элемент подходит: {current_element}")
    current_element += d

print(f"Количество элементов: {count}")
