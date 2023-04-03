print('Задача 6. Вклады')

# Вклад в банке составляет X рублей.
# Ежегодно он увеличивается на P процентов,
# после чего дробная часть копеек отбрасывается.

# Определите, через сколько лет вклад составит не менее Y рублей.

# Напишите программу,
# которая по данным числам X, Y, P определяет,
# сколько лет пройдёт, прежде чем сумма достигнет значения Y.

deposit = int(input("Enter your deposit: "))
percent = int(input("Enter percent: "))
needed_money = int(input("Enter how much you need to get: "))
year = 0

while deposit <= needed_money:
    deposit = int(deposit + deposit * percent / 100)
    year += 1
print(year)
