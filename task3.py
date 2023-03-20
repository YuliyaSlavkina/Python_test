products = []
n = int(input('Введите количество товаров о которых хотите заполнить информацию: '))
i = 0
while i < n:
    for i in range(1, n + 1):
        name = input("Введите название товара: ")
        price = int(input("Введите цену товара: "))
        count = int(input("Введите количество товара: "))
        measure = input("Введите единицу измерения товара: ")
        products.append(
            (i, {'название': name, 'цена': price, 'количество': count, 'единицы': measure}))
        i += 1
print(products)

subject_name = []
subject_price = []
subject_count = []
subject_measure = []
for i in products:
    subject_name.append(i[1].get('название'))
    subject_price.append(i[1].get('цена'))
    subject_count.append(i[1].get('количество'))
    subject_measure.append(i[1].get('единицы'))
print(subject_name)
print(subject_price)
print(subject_count)
print(subject_measure)
analytics = ({'название': subject_name, 'цена': subject_price, 'количество': subject_count, 'единицы': subject_measure})
print(analytics)

# не смогла понять в чем ошибка, в той части где делается аналитика в список с единицами измерения записывается NONE (((