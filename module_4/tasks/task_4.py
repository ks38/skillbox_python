print('Задача 4. Калькулятор скидки')

# Васин друг переехал в новую квартиру, и ему нужно купить три стула в разные комнаты. Цены на стулья разные, а в
# некоторых магазинах есть скидки. Друг хочет заказать у Васи калькулятор скидки, чтобы проще ориентироваться в ценах.

# Напишите программу, которая запрашивает три стоимости товара и вычисляет сумму чека. Если сумма чека превышает
# 10 000 руб., нужно вычесть из этой суммы скидку 10% (умножить на 10, разделить на 100). Итоговая сумма должна
# выводиться на экран.

check = 10_000
chair_1_price = int(input("Enter 1st chair cost: "))
chair_2_price = int(input("Enter 2nd chair cost: "))
chair_3_price = int(input("Enter 3rd chair cost: "))

chair_cost_sum = chair_1_price + chair_2_price + chair_3_price

if chair_cost_sum > check:
    discount = chair_cost_sum * 0.1
    print("Discount is ", discount, "rub")
    chair_cost_sum -= discount
    print("You will pay: ", chair_cost_sum, "rub")
else:
    print("You will pay: ", chair_cost_sum, "rub")
