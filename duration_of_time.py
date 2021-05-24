minute = 60
hour = 3600
day = 86400

get_duration = int(input('Укажите количество секунд: '))
print('duration = ', get_duration)

if get_duration < minute:
    print(get_duration, ' сек')
elif hour > get_duration >= minute:
    minutes = get_duration // minute
    seconds = get_duration % minute
    print(minutes, 'min', seconds, 'sec')
elif day > get_duration >= hour:
    hours = get_duration // hour
    part_hour = get_duration % hour
    minutes = part_hour // minute
    seconds = get_duration % minute
    print(hours, 'h', minutes, 'min', seconds, 'sec')
else:
    days = get_duration // day
    part_day = get_duration % day
    hours = part_day // hour
    part_hour = part_day % hour
    minutes = part_hour // minute
    seconds = get_duration % minute
    print(days, 'd', hours, 'h', minutes, "min", seconds, 'sec')
