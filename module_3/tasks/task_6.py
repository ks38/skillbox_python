print('Задача 6. Проверяем бухгалтера')

# Реализуйте программу,
# которая запрашивает два числа у пользователя.
# После этого у каждого числа возьмите две последние цифры.
# Получившиеся два числа сложите и выведите на экран.

# Пример:
# Введите первое число: 456
# Введите второе число: 123
# Сумма: 79
first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))
sum = first_num % 100 + second_num % 100
print("sum =", sum)
