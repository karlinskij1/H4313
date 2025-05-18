import datetime

# дата та час у одному об'єкті
dt = datetime.datetime(2000, 1, 2, minute=20)

print(f'object datetime - {dt}')
print(f'type - {type(dt)}')

# отримання часу з об'єкту  дати та часу
t = dt.time()

print(f'object time - {t}')
print(f'type - {type(t)}')

# отримання дати з об'єкту  дати та часу
d = dt.date()

print(f'object date - {d}')
print(f'type - {type(d)}')

# лише час
t2 = datetime.time(0, 0, 30)
print(f'object time2 - {t2}')
print(f'type - {type(t2)}')

# лише дата
d2 = datetime.date(2000, 1, 30)
print(f'object date2 - {d2}')
print(f'type - {type(d2)}')
