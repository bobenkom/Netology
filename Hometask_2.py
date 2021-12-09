# Задание 1
# Дана переменная, в которой хранится слово из латинских букв. Напишите код, который выводит на экран:
# среднюю букву, если число букв в слове нечетное;
# две средних буквы, если число букв четное.

word = input('Введите слово: ')
if len(word) % 2 == 0:
    print(word[len(word) // 2 - 1] + word[len(word) // 2])
if len(word) % 2 != 0:
    print(word[len(word) // 2])

# Задание 2
# Напишите программу, которая последовательно запрашивает у пользователя числа (по одному за раз)
# и после первого нуля выводит сумму всех ранее введенных чисел.

number = int(input('Введите число: '))
summa = 0
while number != 0:
    summa = number + summa
    number = int(input('Введите число: '))
print(f'Результат: {summa}')

# Задание 3
# Мы делаем MVP dating-сервиса, и у нас есть список парней и девушек.
# Выдвигаем гипотезу: лучшие рекомендации мы получим, если просто отсортируем имена по алфавиту и познакомим людей
# с одинаковыми индексами после сортировки! Но мы не будем никого знакомить, если кто-то может остаться без пары:

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys) == len(girls):
    boys.sort()
    girls.sort()
    x = 0
    print('Идеальные пары:')
    for name in boys:
        print(f'{name} и {girls[x]}')
        x += 1
else:
    print('Внимание, кто - то может остаться беp пары!')

# Задание 4
# У нас есть список, содержащий информацию о среднедневной температуре в Фаренгейтах за произвольный период по странам
# (структура данных в примере). Необходимо написать код, который рассчитает среднюю температуру за период в Цельсиях(!)
# для каждой страны.

countries_temperature = [
['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
['Germany', [57.2, 55.4, 59, 59, 53.6]],
['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]
print('Средняя температура в странах: ')
string = 0
for block in countries_temperature:
    temperature = 0
    sum_temperature = 0
    for a in countries_temperature[string][1]:
        temperature += 1
        sum_temperature += a
    avarage_temperature = sum_temperature / len(countries_temperature[string][1])
    cel = (avarage_temperature - 32) * 5 / 9
    print(f'{countries_temperature[string][0]} - {round(cel,1)} C')
    string += 1

