cube_number = []

for number in range(1, 1001):
    if number % 2 != 0:
        cube = number ** 3
        cube_number.append(cube)
print(cube_number)

number_multiple_7 = []

for number in cube_number:
    amount_number = 0
    num = number
    while num != 0:
        amount_number += num % 10
        num = num // 10
    if amount_number % 7 == 0:
        number_multiple_7.append(number)

print('Сумма чисел списка, сумма цифр которых кратны 7: ', sum(number_multiple_7))

for idx in range(len(cube_number)):
    cube_number[idx] += 17
print(cube_number)

number_multiple_7_change = []

for number in cube_number:
    amount_number = 0
    num = number
    while num != 0:
        amount_number += num % 10
        num = num // 10
    if amount_number % 7 == 0:
        number_multiple_7_change.append(number)

print('Сумма чисел, списка увеличенного на 17, сумма цифр которых кратны 7: ', sum(number_multiple_7_change))

