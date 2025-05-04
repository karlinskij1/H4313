import random

def black_hole(*args):
    print(type(args))
    for element in args:
        print(element)

amount = random.randint(5, 20)
my_garbage = list()

for _ in range(amount):
    my_garbage.append(random.randint(10, 2000))

# print(my_garbage)
# print("Length:", len(my_garbage))
black_hole(*my_garbage)
