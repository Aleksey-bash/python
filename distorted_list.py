dis_list = ['инженер-конструктор ИгоРь', 'главный бухгалтер МАРИНА',
            'токарь высшего разряда нИКОЛАЙ', 'директор аэлита']

for elem in dis_list:
    elem_parts = elem.split()
    print('Привет, ', elem_parts.pop().capitalize(), '!')
