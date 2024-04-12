def find_change(coins, amount):
    change = []

    for coin in coins:
        while amount >= coin:
            amount -= coin
            change.append(coin)
    return change


products = {
    'молоко': 23,
    'хлеб': 14,
    'яйца': 21,
    'сок': 34,
    'печенье': 12,
    'сыр': 41,
    'масло': 37,
    'колбаса': 54,
    'вода': 3,
    'макароны': 18
}

print('Продукты:')
for product, price in products.items():
    print(f'{product}: {price}р')

while True:
    product_choice = input('Выберите продукт из списка выше: ')
    product_price = products.get(product_choice)

    if product_price:
        payment = int(input(f'Введите сумму, которую вы даете за {product_choice}: '))
        change_due = payment - product_price

        coin_values = [15, 10, 7, 5, 1]

        change_coins = find_change(coin_values, change_due)

        print(f'Выбранный продукт: {product_choice}')
        print(f'Цена продукта: {product_price} р')
        print(f'Полученная сумма: {payment} р')
        print(f'Сдача: {change_due} р')
        print('Монеты для сдачи:')
        for coin in change_coins:
            print(coin, 'р', end=' ')
        break
    else:
        print('Такого продукта нет в списке. Пожалуйста, выберите продукт из представленного списка.')


