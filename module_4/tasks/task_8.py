print('Задача 8. Максимальное число (по желанию)')

# Пользователь вводит три числа.
# Напишите программу,
# которая выводит на экран максимальное из этих трёх чисел (все числа разные).
# Можно использовать дополнительные переменные, если нужно

number_first = int(input("Enter first number "))
number_second = int(input("Enter second number "))
number_third = int(input("Enter third number "))
max = number_first

if number_second > max and number_second > number_third:
    max = number_second
elif number_third > max and number_third > number_second:
    max = number_third
print("max = ", max)
