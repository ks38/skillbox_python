print('Задача 1. Датчик погоды')

# За окном квартиры стоит датчик погоды, который определяет, идёт ли дождь. Если идёт, датчик оповещает сообщением:
# «Пошёл дождь. Возьмите зонтик!»

# Напишите программу, которая получает на вход число 0 или 1. Единица означает, что дождь идёт. В таком случае выводите
# на экран сообщение: «Пошёл дождь. Возьмите зонтик!». Ноль означает, что дождя нет, в этом случае надо вывести
# сообщение «Дождя нет!»

# Пример 1:
# На улице идёт дождь? 1
# Пошёл дождь. Возьмите зонтик!

# Пример 2:
# На улице идёт дождь? 0
# Дождя нет!

sensor = int(input("Is it raining now? Enter 1 or 0: "))
if sensor == 1:
    print("It's raining man, hallelujah. Take an umbrella!")  # "Это мужицкий дожщщь, алилуйя
elif sensor == 0:
    print("There is no spoon, Neo. Ups. There's no rain outside!")
else:
    print("ERROR! You have to enter 1 or 0!")
