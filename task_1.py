def odd_nums(nam):
    n = 1
    while n <= nam:
        yield n
        n += 2


result_gen = odd_nums(21)
print(next(result_gen))
print(next(result_gen))
print(next(result_gen))
