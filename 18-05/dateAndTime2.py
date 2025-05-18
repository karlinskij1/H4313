import datetime

d_n = datetime.datetime.now()
d_t = datetime.datetime.today()
d_d = datetime.date.today()

print(f'date now - {d_n}')
print(f'date today - {d_t}')
print(f'date with date - {d_d}')

print(d_d.weekday())

# https://docs.python.org/uk/3.9/library/datetime.html#strftime-and-strptime-behavior

format_date = d_d.strftime("%m/%d/%Y %a %A")
print(format_date)

birthday_str = input("Введіть день народження (мм/дд/рррр): ")
format = "%m/%d/%Y"

birthday_date = datetime.datetime.strptime(birthday_str, format).date()
print(f'{type(birthday_date)} - {birthday_date}')

dif = datetime.date.today() - birthday_date

print(f'{type(dif)} - {int(dif.days / 365)}')