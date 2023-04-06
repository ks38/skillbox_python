print('Задача 8. Игра «Компьютер угадывает число»')

# Поменяйте мальчика и компьютер из прошлой задачи местами.
# Теперь мальчик загадывает число между 1 и 100 (включительно).
# Компьютер может спросить у мальчика:
# «Твое число равно, меньше или больше, чем число N?»,
# где N — число, которое хочет проверить компьютер.
# Мальчик отвечает одним из трёх чисел:
# 1 — равно,
# 2 — больше,
# 3 — меньше.

# Напишите программу,
# которая с помощью цепочки таких вопросов и ответов мальчика угадывает число.

# Дополнительно: сделайте так, чтобы можно было гарантированно угадать число за семь попыток.

# Подсказка: используйте бинарный поиск, а не конкатенацию.

guessed_number = int(input("Enter number, boy: "))

left_border = 1
right_border = 100
tries = 0

while True:
    diff = (left_border + right_border) // 2
    tries += 1
    print(diff)
    number = int(input("Your number equals (enter 1), less (enter 2) or more (enter 3): "))
    if number == 1:
        break
    elif number == 2:
        print("more")
        right_border = diff
    elif number == 3:
        print("less")
        left_border = diff
print("You win with", tries, "tries")