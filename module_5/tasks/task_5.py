print('Задача 5. Вася хочет выигрывать')

# Вася вдохновился фильмом «Двадцать одно» и решил изучить математику игровых автоматов. Для анализа данных ему нужна
# информация о том, как часто в автомате выпадает три или две одинаковых картинки. Для сбора данных нужна программа,
# проверяющая это равенство.

# Даны три целых числа. Определите, сколько среди них совпадающих.
# Программа должна вывести один из вариантов:
# 1) 3 (если все совпадают)
# 2) 2 (если два совпадают)
# 3) 0 (если все числа разные)

number_first = int(input("Enter first number: "))
number_second = int(input("Enter second number: "))
number_third = int(input("Enter third number: "))

first_equals_second_equals_third = number_first == number_second == number_third
first_equals_second = number_first == number_second
first_equals_third = number_first == number_third
second_equals_third = number_second == number_third

if first_equals_second_equals_third:
    print(3)
elif first_equals_second or first_equals_third or second_equals_third:
    print(2)
else:
    print(0)
