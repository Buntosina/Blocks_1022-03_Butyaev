# Блок 1. Задание 1. Сравнить числа
print("Введите число = ")
number = float(input())
print("Введите пограничное число = ")
numberP = float(input())
if number < numberP:
    print("Ваше число меньше пограничного")
elif number > numberP*3:
    print("Ваше число больше пограничного более, чем в 3 раза")
elif number > numberP:
    print("Ваше число больше пограничного")
else:
    print("Числа равны")
