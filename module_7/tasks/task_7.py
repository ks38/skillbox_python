print('Задача 7. Пропавшая карточка')

# Для настольной игры используются карточки с номерами от 1 до N.
# Одна карточка потерялась. Найдите ее, зная номера оставшихся карточек.
#
# Вводится число N, далее еще N − 1 чисел:
# номера оставшихся карточек (различные числа от 1 до N).
# Программа должна вывести номер потерянной карточки.

# Пример:
# Введите количество карточек: 5
# Введите номер оставшейся карточки: 1
# Введите номер оставшейся карточки: 4
# Введите номер оставшейся карточки: 5
# Введите номер оставшейся карточки: 3

# Номер пропавшей карточки: 2

cards_amount = int(input("Enter cards amount: "))

card = 0
difference = 0

cards_summ = (cards_amount + 1) * cards_amount // 2

for cards in range(1, cards_amount):
    card += int(input("Enter card number: "))

missing_card = cards_summ - card

print("Missing card is", missing_card)
