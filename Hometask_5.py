# Переведите содержимое файла purchase_log.txt в словарь purchases вида:
# {‘1840e0b9d4’: ‘Продукты’, …}
# Для каждого user_id в файле visit_log.csv определите третий столбец с категорией покупки (если покупка была, сам файл visit_log.csv изменять не надо). Запишите в файл funnel.csv визиты из файла visit_log.csv, в которых были покупки с указанием категории.
# Учтите условия на данные:
# содержимое purchase_log.txt помещается в оперативную память компьютера
# содержимое visit_log.csv - нет; используйте только построчную обработку этого файла
import json

with open('purchase_log.txt') as f:
    purchases = {}
    for line in f:
        line = line.strip()
        dic = json.loads(line)
        purchases[dic['user_id']] = dic['category']
    with open('funnel.csv', 'w') as funnel:
        with open('visit_log.csv') as visit:
                for block in visit:
                    block = block.strip().split(',')
                    if block[0] in purchases:
                        funnel.write(f'{block[0]},{block[1]},{purchases[block[0]]}\n')
