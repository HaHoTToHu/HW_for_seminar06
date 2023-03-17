# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. не 
# меньше заданного минимума и не больше заданного максимума)
import random

list = [random.randint(-10, 10) for i in range(10)]
min = int(input("Введите минимальную границу диапазона: "))
max = int(input("Введите максимальную границу диапазона: "))
print(list)

list_2 = []
for i in range(len(list)):
    if list[i] >= min and list[i] <= max:
        list_2.append(i)

print(list_2)