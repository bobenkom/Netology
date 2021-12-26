documents = [
{'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
{'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
{'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
'1': ['2207 876234', '11-2'],
'2': ['10006'],
'3': []
}


def p_function(number):
    for block in documents:
        for value in block.values():
            if value == number:
                return block['name']
    return None

def s_function(number):
    for k,v in directories.items():
        for x in v:
            if x == number:
                return k
    return None

def l_function():
    for block in documents :
        print (f"№: {block['number']} тип: {block['type']}, владелец: {block['name']},полка хранения: {s_function(block['number'])}")

def ads_function(number):
    for key in directories.keys():
        if key == number:
            return None
        else:
            directories[number] = []
            return True

def ds_function(number):
    for k, v in directories.items():
        if number == k:
            if v == []:
                directories.pop(k)
                return True
            return False
    return None

def count_directories():
    new_directories = []
    for key in directories:
        new_directories.append(key)
    output_directories = ", ".join(new_directories)
    return output_directories


def main(documents):
    while True:
        litera = input('Введите команду: ')
        if litera == 'p':
            number = input('Введите номер документа: ')
            if p_function(number) is None:
                print('Документ не найден в базе')
            else:
                print("Владелец документа: " +  p_function(number))
        elif litera == 's':
            number = input('Введите номер документа: ')
            if s_function(number) is None:
                print('Документ не найден в базе')
            else:
                print('Документ хранится на полке: ' + s_function(number))
        elif litera == 'l':
            l_function()
        elif litera == 'ads':
            number = input('Введите номер полки: ')
            if ads_function(number) is None:
                print('Такая полка уже существует.', end=' ')
            else:
                print('Полка добавлена.', end=' ')
            print(f'Текущий перечень полок: {count_directories()}.')
        elif litera == 'ds':
            number = input('Введите номер полки: ')
            if ds_function(number) is True:
                print(f'Полка удалена. Текущий перечень полок: {count_directories()}.')
            elif ds_function(number) is False:
                print(f'На полке есть документы, удалите их перед удалением полки. Текущий перечень полок: {count_directories()}.')
            elif ds_function(number) is None:
                print(f'Такой полки не существует. Текущий перечень полок: {count_directories()}.')
        elif litera == 'q':
            break


main(documents)