# Задание 1
# Дана переменная, в которой хранится словарь, содержащий гео-метки для каждого пользователя (пример структуры данных
# приведен ниже). Вам необходимо написать программу, которая выведет на экран множество уникальных гео-меток всех
# пользователей.
#
# Пример работы программы:

ids = {'user1': [213, 213, 213, 15, 213],
'user2': [54, 54, 119, 119, 119],
'user3': [213, 98, 98, 35]}
# Результат: {98, 35, 15, 213, 54, 119}

ids_set = set()
for key in ids:
    for a in ids[key]:
        ids_set.add(a)
print(ids_set)

# Задание 2
# Дана переменная, в которой хранится список поисковых запросов пользователя (пример структуры данных приведен ниже).
# Вам необходимо написать программу, которая выведет на экран распределение количества слов в запросах в требуемом виде.
#
# Пример работы программы:
#
queries = [
'смотреть сериалы онлайн',
'новости спорта',
'афиша кино',
'курс доллара',
'сериалы этим летом',
'курс по питону',
'сериалы про спорт'
]
# Результат:
# Поисковых запросов, содержащих 2 слов(а): 42.86%
# Поисковых запросов, содержащих 3 слов(а): 57.14%

count_words_in_queries = []
count_queries = len(queries)
print('Результат: ')
for words in queries:
    count_words_in_queries.append(words.count(' ') + 1)
    count_words_in_queries.sort()
dict_queries = {i:count_words_in_queries.count(i) for i in count_words_in_queries}
for i in dict_queries:
    print(f'Поисковых запросов, содержащих {i} слов(а): {round(dict_queries[i] / count_queries * 100, 2)}%')

# Задание 3
# Дана переменная, в которой хранится информация о затратах и доходе рекламных кампаний по различным источникам.
# Необходимо дополнить исходную структуру показателем ROI, который рассчитаем по формуле: (revenue / cost - 1) * 100
#
# Пример работы программы:

results = {
'vk': {'revenue': 103, 'cost': 98},
"yandex": {'revenue': 179, 'cost': 153},
'facebook': {'revenue': 103, 'cost': 110},
'adwords': {'revenue': 35, 'cost': 34},
'twitter': {'revenue': 11, 'cost': 24},}

for i in results:
    for line in results[i]:
        revenue = results[i]['revenue']
        cost = results[i]['cost']
        roi = round((revenue / cost - 1) * 100,2)
        results[i]['ROI'] = roi
        break
print(results)

# Результат:
#
# {‘adwords’: {‘revenue’: 35, ‘cost’: 34, ‘ROI’: 2.94},
# ‘facebook’: {‘revenue’: 103, ‘cost’: 110, ‘ROI’: -6.36},
# ‘twitter’: {‘revenue’: 11, ‘cost’: 24, ‘ROI’: -54.17},
# ‘vk’: {‘revenue’: 103, ‘cost’: 98, ‘ROI’: 5.1},
# ‘yandex’: {‘revenue’: 179, ‘cost’: 153, ‘ROI’: 16.99}}
#
# Задание 4
# Дана переменная, в которой хранится статистика рекламных каналов по объемам продаж (пример структуры данных приведен ниже).
# Напишите программу, которая возвращает название канала с максимальным объемом продаж.
#
# Пример работы программы:
#
stats = {'facebook': 55, 'yandex': 115, 'vk': 120, 'google': 99, 'email': 42, 'ok': 98}
print(f'Результат: Максимальный объем продаж на рекламном канале: {max(stats, key=stats.get)}')

# Результат: Максимальный объем продаж на рекламном канале: vk



