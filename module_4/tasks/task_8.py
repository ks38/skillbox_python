print('Задача 8. Максимальное число (по желанию)')

# Пользователь вводит три числа.
# Напишите программу,
# которая выводит на экран максимальное из этих трёх чисел (все числа разные).
# Можно использовать дополнительные переменные, если нужно

number_first = int(input("Enter first number "))
number_second = int(input("Enter second number "))
number_third = int(input("Enter third number "))

# TODO: не стоит затенять системные имена, например, max, min, time, sum
max = number_first

if number_second > max:
    max = number_second

if number_third > max:
    max = number_third
print("max = ", max)
