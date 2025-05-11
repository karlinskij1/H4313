menu_list =[
    "1) Додати клієнта",
    "2) Видалити клієнта",
    "3) Показати всіх клієнтів",
]

client_list = []

def addClient():
    global client_list
    name = input("Введіть ім'я: ")
    surname = input("Введіть прізвище: ")
    result = f"Ім'я: {name}\nПрізвище: {surname}"
    client_list.append(result)

def showClients():
    global client_list
    for i in range(0, len(client_list)):
        print(f"{i+1})\n{client_list[i]}\n")


while True:
    for element in menu_list:
        print(element)
    choice = input("Напешить номер бажаної операції: ")
    if choice == '1':
        addClient()
    elif choice == '3':
        showClients()
    else:
        print("Такої операції нема")


