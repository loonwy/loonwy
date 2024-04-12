def find_change(coins, amount):
    change = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            change.append(coin)
    return change


def buy_product(product_price, coins_count):
    payment = 0
    while payment < product_price:
        coin_values = map(int, input("Введите монеты номиналом 15, 10, 7, 5, 1 через пробел: ").split())
        for coin in coin_values:
            if coin in [15, 10, 7, 5, 1]:
                payment += coin
            else:
                print('Неподходящий номинал монеты. Попробуйте еще раз.')
    change_due = payment - product_price
    change_coins = find_change([15, 10, 7, 5, 1], change_due)

    print(f'Полученная сумма: {payment} р')
    print(f'Сдача: {change_due} р')
    print('Монеты для сдачи:')
    for coin in change_coins:
        if coins_count.get(coin, 0) > 0:
            coins_count[coin] -= 1
            print(coin, 'р', end=' ')
        else:
            print(f'Недостаточно монет номиналом {coin} для сдачи.')


coins_count = {1: 10, 5: 15, 7: 8, 10: 5, 15: 6}
products = {
    'молоко': 23, 'хлеб': 14,
    'яйца': 21, 'сок': 34,
    'печенье': 12, 'сыр': 41,
    'масло': 37, 'колбаса': 54,
    'вода': 3, 'макароны': 18
}

print('Продукты:')
for product, price in products.items():
    print(f'{product}: {price}р')

chosen_products = {}
total_price = 0

while True:
    product_choice = input('Выберите продукт из списка или нажмите "q" для завершения покупок: ')
    if product_choice.lower() == 'q':
        break
    product_price = products.get(product_choice)
    if product_price:
        chosen_products[product_choice] = product_price
        total_price += product_price
    else:
        print('Такого продукта нет в списке. Пожалуйста, выберите продукт из представленного списка.')

if chosen_products:
    print('Выбранные продукты и их цены:')
    for product, price in chosen_products.items():
        print(f'{product}: {price}р')
    print(f'Общая стоимость продуктов: {total_price} р')

    buy_product(total_price, coins_count)
else:
    print('Вы не выбрали ни одного продукта.')

