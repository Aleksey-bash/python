import random

nouns = ['автомобиль', 'дом', 'телефон', 'шарик', 'собака']
adverbs = ['завтра', 'сегодня', 'вчера', 'c утра', 'вечером']
adjectives = ['весёлый', 'яркий', 'зелёый', 'прозрачный', 'твёрдый']


def get_jokes(num):
    hodgepodge = []
    for i in range(num):
        elem_nouns = random.choice(nouns)
        elem_adverbs = random.choice(adverbs)
        elem_adjectives = random.choice(adjectives)
        hodgepodge.append(f'{elem_nouns} {elem_adverbs} {elem_adjectives}')
    return hodgepodge


print(get_jokes(3))

