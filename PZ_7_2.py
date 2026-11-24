#Дана строка, состоящая из русских слов, разделенных пробелами (одним или несколькими). Найти длину самого длинного слова.

text = "один два четыре абоба "
words = text.split()
max_len = max(len(word) for word in words) if words else 0
print(max_len)