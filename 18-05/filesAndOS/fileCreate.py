file = open('test_file.txt', 'w')
file.write("Тестовий запис українською!")
file.close()

with open('test_file.txt', 'r') as file:
    print(file.read())

with open('test_file.txt', 'w') as file:
    file.write("Тестовий запис через with!")

with open('test_file.txt', 'r') as file:
    print(file.read())


my_list = ["Влад", "Карлінський", 35]

with open('myInfo.txt', 'w') as file:
    for element in my_list:
        file.write(str(element) + '\n')

with open('myInfo.txt', 'r') as file:
    print(file.read())