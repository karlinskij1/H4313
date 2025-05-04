import random

def My_sum(*args):
    sum = 0
    for element in args:
        sum += element
    return sum


def My_mult(a, b):
    return a * b


def My_div(a, b):
    return a / b


def My_sub(*args):
    sub = args[0]
    for i in range(1, len(args)):
        sub -= args[i]
    return sub


def calc(operation, *values):
    if operation == '+':
        return My_sum(*values)
    elif operation == '-':
        return My_sub(*values)
    elif operation == '*':
        return My_mult(*values)
    elif operation == '/':
        return My_div(*values)


operations = ['+', '-', '*', '/']

amount = int(input("Виберіть кількість чисел: "))
values = list()

for i in range(amount):
    value = float(input(str(i + 1) + ') '))
    values.append(value)

print("Виберіть операцію ", operations, ": ", end="")
operation = input()

# якщо operation дорівню одному з символів списку operations
if operation in operations:
    print(calc(operation, *values))
else:
    print("Нема такої операції")


