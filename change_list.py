some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

change_list = []
for elem in some_list:
    if elem.isdigit():
        change_list.extend(['"', f'{int(elem):02}', '"'])
    elif (elem.startswith('+') or elem.startswith('-')) and elem[1:].isdigit():
        change_list.extend(['"', f'{elem[0]:<2}{int(elem[1:]):02}', '"'])
    else:
        change_list.append(elem)

output_str = ' '.join(change_list)
print(output_str)

