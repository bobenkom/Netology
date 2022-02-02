import pandas as pd



"""
Задание 1 Скачайте с сайта https://grouplens.org/datasets/movielens/ датасет любого размера. Определите какому фильму
было выставлено больше всего оценок 5.0.
- Так как сайт не работал, я взяла файл ratings.csv и определила какой пользователь поставил больше всех отметок 5.0 -
"""
# df = pd.read_csv('ratings.csv')
# df_five = df.loc[df["rating"] == 5.0]
# print(df_five["userId"].value_counts()[0:1])


"""
Задание 2 По данным файла power.csv посчитайте суммарное потребление стран Прибалтики (Латвия, Литва и Эстония) 
категорий 4, 12 и 21 за период с 2005 по 2010 года. Не учитывайте в расчетах отрицательные значения quantity.
"""
data = pd.read_csv('power.csv')
filtered_countries = data[ (data['country']=='Estonia') | (data['country']=='Lithuania') | (data['country']=='Latvia') ]
filtered_categories = filtered_countries[ (filtered_countries['category']==4) | (filtered_countries['category']==12) | (filtered_countries['category']==21) ]
years = filtered_categories[ (filtered_categories['year'] > 2005) | (filtered_categories['year'] < 2011) ]
# data_values = years.loc[ ['quantity'] > 0]


"""
Задание 3 Выберите страницу любого сайта с табличными данными. Импортируйте таблицы в pandas dataframe. Примеры 
страниц (необязательно брать именно эти): https://fortrader.org/quotes https://www.finanz.ru/valyuty/v-realnom-vremeni
"""

# page_url = 'https://www.finanz.ru/valyuty/v-realnom-vremeni'
# df = pd.read_html(page_url, attrs = {'class': 'quote_list'}, encoding='utf-8')
# print(df)