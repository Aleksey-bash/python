from itertools import zip_longest

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей',
          'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

gen_tuple = ((tutor, klass) for tutor, klass in zip_longest(tutors, klasses))
print(next(gen_tuple))
print(next(gen_tuple))
print(next(gen_tuple))
print(next(gen_tuple))
print(next(gen_tuple))
print(next(gen_tuple))
print(next(gen_tuple))
print(next(gen_tuple))





