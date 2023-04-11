print('Задача 5. Отрезок')

# Напишите программу,
# которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль среднее арифметическое всех чисел из отрезка [a; b], которые кратны числу 3.

# (среднее арифметическое можно посчитать поделив сумму подходящих чисел на их количество)

number_a = int(input("Enter a: "))
number_b = int(input("Enter b: "))
number_count = 0
relevant_number = 0

for i in range(number_a, number_b + 1):
    if i % 3 == 0:
        relevant_number += i
        number_count += 1
print(relevant_number / number_count)
