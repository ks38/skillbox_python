print('Задача 4. Успеваемость в классе')

# В классе N человек.
# Каждый из них получил за урок по информатике оценку: 3, 4 или 5, двоек сегодня не было.
#
# Напишите программу,
# которая получает список оценок - N чисел - и выводит на экран сообщение о том,
# кого сегодня больше: отличников, хорошистов или троечников.

# Замечание: можно предположить, что количество отличников, хорошистов, троечников различно.

smart = 0
middle = 0
stupid = 0

students = int(input("Enter students amount: "))

for student_number in range(1, students + 1):
    print("Student", student_number)
    grades = int(input("Enter school grade: "))
    if grades == 5:
        smart += 1
    elif grades == 4:
        middle += 1
    elif grades == 3:
        stupid += 1
if stupid > middle > smart:
    print("Today is a stupids day")
elif stupid < middle > smart:
    print("Today is a middles day")
else:
    print("Today is a smarts day")
