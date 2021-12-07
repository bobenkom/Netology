# Задание 1

phrase_1 = input()
phrase_2 = input()
if len(phrase_1) > len(phrase_2):
    print('Фраза 1 длиннне фразы 2')
elif len(phrase_2) > len(phrase_1):
    print('Фраза 2 длиннее фразы 1')
else:
    print('Фразы равной длины')

# Задание 2

year = int(input())
if (year % 4 == 0 and not year % 100 == 0) or year % 400 == 0:
  print('Високосный год')
else:
  print('Обычный год')

# Задание 3

date = int(input('Введите день: '))
month = input('Введите месяц: ')
month = month.lower()
if (date >= 21 and date <= 31 and month == 'март') or(month == 'апрель' and date >= 1 and date <= 19):
    print("Ваш знак зодиака: Овен")
elif (date >= 20 and date <= 30 and month == 'апрель') or(month == 'май' and date >= 1 and date <= 20):
    print("Ваш знак зодиака: Телец")
elif (date >= 21 and date <= 31 and month == 'май') or (month == 'июнь' and date >=1 and date <= 21):
    print("Ваш знак зодиака: Близнецы")
elif (date >= 22 and date <= 30 and month == 'июнь') or (month == 'июль' and date >= 1 and date <= 22):
    print("Ваш знак зодиака: Рак")
elif (date >= 23 and date <= 31 and month == 'июль') or (month == 'август' and date >= 1 and date <= 22):
    print("Ваш знак зодиака: Лев")
elif (date >= 23 and date <= 1 and month == 'август') or (month == 'сентябрь' and date >= 1 and date <= 22):
    print("Ваш знак зодиака: Дева")
elif (date >= 23 and date <= 30 and month == 'сентябрь') or (month == 'октябрь' and date >= 1 and date <= 23):
    print("Ваш знак зодиака: Весы")
elif (date >= 24 and date <= 31 and month == 'октябрь') or (month == 'ноябрь' and date >= 1 and date <= 22):
    print("Ваш знак зодиака: Скорпион")
elif (date >= 23 and date <= 30 and month == 'ноябрь') or (month == 'декабрь' and date >= 1 and date <= 21):
    print("Ваш знак зодиака: Стрелец")
elif (date >= 22 and date <= 31 and month == 'декабрь') or ( month == 'январь' and date >= 1 and date <= 20):
    print("Ваш знак зодиака: Козерог")
elif (date >= 21 and date <= 31 and month == 'январь') or (month == 'февраль' and date >= 1 and date <= 18):
    print("Ваш знак зодиака: Водолей")
elif (date >= 19 and date <= 29 and month == 'февраль') or (month == 'март' and date>=1 and date<=20):
    print("Ваш знак зодиака: Рыбы")
else:
    print('Введите правильные значения')

# Задание 4

width = int(input('Введите в см ширину товара: '))
length = int(input('Введите в см длину товара: '))
height = int(input('Введите в см высоту товара: '))
if width <= 15 and length <= 15 and height <= 15:
    print('Коробка №1')
elif 15 <= width < 50 and 15 <= length < 50 and 15 <= height < 50:
    print('Коробка №2')
elif length > 200:
    print('Упаковка для лыж')
else:
    print('Стандартная коробка №3')

# Задание 5
number = input('Введите номер билет: ')
if len(number) == 6:
    if int(number[0]) + int(number[1]) + int(number[2]) == int(number[3]) + int(number[4]) + int(number[5]):
        print('Счастливый билет')
    else:
        print('Несчастливый билет')
else:
    print('Введите шестизначное значение')

# Задание 6
type_figure = input('Введите тип фигуры: ')
type_figure = type_figure.lower()
if type_figure == 'круг':
    radius = int(input('Введите радиус круга: '))
    S = radius ** 2 * 3.14159
    print('Площадь круга: ', int(S * 100) / 100)
elif type_figure == 'треугольник':
    a = int(input('ведите длину стороны A: '))
    b = int(input('ведите длину стороны B: '))
    c = int(input('ведите длину стороны C: '))
    p = (a + b + c) / 2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('Площадь треугольника: ', int(S * 100) / 100)
elif type_figure == 'прямоугольник':
    a = int(input('ведите длину стороны A: '))
    b = int(input('ведите длину стороны B: '))
    S = a * b
    print('Площадь прямоугольника: ', int(S * 100) / 100)
else:
    print('Введите правильное значение')





