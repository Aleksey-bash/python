dict_numerals = {
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'семь',
    'nine': 'девять',
    'ten': 'десять'
}


def num_translate_adv(num):
    if num[:1].isupper():
        num_low = num.lower()
        meaning_dict = dict_numerals.get(num_low)
        if meaning_dict is not None:
            print(meaning_dict.capitalize())
        else:
            print(meaning_dict)
    else:
        print(dict_numerals.get(num))


numerals = input('Введите числительное на английском от одного до десяти: ')
num_translate_adv(numerals)




