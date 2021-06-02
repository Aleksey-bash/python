def thesaurus(*name_tuple):
    name_dict = {}
    for elem in name_tuple:
        name_dict.setdefault(elem[0], [])
        name_dict[elem[0]].append(elem)
    return name_dict


print(thesaurus('Алла', 'Дима', 'Петя', 'Диана', 'Костя', 'Кирилл', 'Света'))
