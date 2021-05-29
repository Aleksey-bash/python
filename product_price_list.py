price_list = [54.41, 12, 16.21, 42, 31.7, 14, 9.99, 71.14, 65, 71.44, 102, 77.21]

for price in price_list:
    rub = int(price)
    kopek = (price - rub) * 100
    print(f'{rub} руб {kopek:02.0f} коп')
print('')

print(id(price_list))
price_list.sort()
print(id(price_list))
print('')

for price in price_list:
    rub = int(price)
    kopek = (price - rub) * 100
    print(f'{rub} руб {kopek:02.0f} коп')
print('')

for price in sorted(price_list)[::-1][:5]:
    rub = int(price)
    kopek = (price - rub) * 100
    print(f'{rub} руб {kopek:02.0f} коп')
