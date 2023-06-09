print('Задача 5. Обычный день на работе')

# Максим программирует целый день на работе и вечером идёт домой.
# Каждый час начальство кидает ему несколько задач,
# которые нужно решить до следующего рабочего часа.
# И вдобавок каждый час Максиму звонит супруга.
# Он знает, что если он возьмёт трубку, то жена попросит зайти вечером в магазин.

# Напишите программу,
# в которой считается, сколько задач выполнил Максим за день (8 часов).
# Если он хоть раз взял трубку,
# то в конце дополнительно выводите сообщение: «Нужно зайти в магазин».

# Пример:
# Начался 8-часовой рабочий день
# 1 час
# Сколько задач решит Максим? 1
# Звонит жена. Взять трубку? (1-да, 0-нет) 0

# 2 час
# Сколько задач решит Максим? 2
# Звонит жена. Взять трубку? (1-да, 0-нет) 0

# 3 час
# Сколько задач решит Максим? 3
# Звонит жена. Взять трубку? (1-да, 0-нет) 0

# 4 час
# Сколько задач решит Максим? 4
# Звонит жена. Взять трубку? (1-да, 0-нет) 1

# 5 час
# Сколько задач решит Максим? 5
# Звонит жена. Взять трубку? (1-да, 0-нет) 0

# 6 час
# Сколько задач решит Максим? 1
# Звонит жена. Взять трубку? (1-да, 0-нет) 0

# 7 час
# Сколько задач решит Максим? 2
# Звонит жена. Взять трубку? (1-да, 0-нет) 1

# 8 час
# Сколько задач решит Максим? 3
# Звонит жена. Взять трубку? (1-да, 0-нет) 0

# Рабочий день закончился. Всего выполнено задач: 21
# Нужно зайти в магазин

day_time, tasks_count = 0, 0
SHIFT_TIME = 8
wife_calls = 0

print("8-hour day time has began")

while day_time < SHIFT_TIME:
    day_time += 1
    print(day_time, "hour")
    tasks_count += int(input("How much tasks Maxim has to do: "))
    wife_calls += int(input("Wife is calling. Answer? (1- yes, 0 - no) "))
print("Workday os over, tasks done:", tasks_count)
# if wife_calls >= 1:
if wife_calls:
    print("And you must go to the shop!")
