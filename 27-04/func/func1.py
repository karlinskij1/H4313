def func1():
    print("func1 works!")


def func2(a, b):
    print("a:", a, "b:", b)
    return a + b


print(func1)
func1()

first = int(input("first: "))
second = int(input("second: "))

print(func2(first, second))
