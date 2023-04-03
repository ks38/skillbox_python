print('Задача 2. Коллекторы')

# Напишите робота для коллекторов.
# В самом начале он спрашивает имя должника и сумму долга,
# а затем начинает требовать у него погашения до тех пор,
# пока он не введёт нужную сумму (равную сумме долга или больше).
# После погашения долга сообщите об этом пользователю и поблагодарите его.

# Пример:
# Василий, ваша задолженность составляет 100 рублей.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 50

# Маловато, Василий. Давайте ещё раз.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 90
# Маловато, Василий. Давайте ещё раз.

# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 110
# Отлично, Василий! Вы погасили долг. Спасибо!

owe_name = input("Enter your name: ")
debt = int(input("Enter debt: "))

print(owe_name, "Your debt is", debt)

pay = int(input("Enter money amount you want to pay for debt: "))

if debt >= pay:
    while debt >= pay:
        print(owe_name, "It is not enough to pay debt")
        pay = int(input("Enter money amount you want to pay for debt: "))
        if pay >= debt:
            print(owe_name, "thanks, you're free now")
            break
else:
    print("Well done!")
