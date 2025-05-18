clients = []


def print_menu():
    global clients
    print("\n МЕНЮ ")
    print("1. Додати клієнта")
    print("2. Видалити клієнта")
    print("3. Показати всіх клієнтів")
    print("4. Показати конкретного клієнта")
    print("5. Вихід")


def add_client():
    global clients
    surname = input("Введіть прізвище: ")
    name = input("Введіть ім’я: ")
    age = int(input("Введіть вік: "))
    phone = int(input("Введіть номер телефону: "))
    client = {"Прізвище": surname, "Ім’я": name, "Вік": age, "Телефон": phone}
    clients.append(client)
    print(f"Клієнта {surname} додано.")


def delete_client():
    global clients
    number = input("Введіть номер клієнта для видалення: ")
    if not number.isdigit():
        print("Це не число!")
        return
    index = int(number) - 1
    if 0 <= index < len(clients):
        removed = clients.pop(index)
        print(f"Клієнта {removed['Прізвище']} видалено.")
    else:
        print("Клієнта з таким номером не існує.")


def show_all_clients():
    global clients
    if not clients:
        print("Список клієнтів порожній.")
        return
    print("\n=== СПИСОК КЛІЄНТІВ ===")
    for i, client in enumerate(clients, 1):
        print(f"{i}. {client['Прізвище']:<10} {client['Ім’я']:<10} Вік: {client['Вік']:<3} Тел: {client['Телефон']}")


def show_client_by_number():
    global clients
    index = input("Введіть номер клієнта: ")
    if not index.isdigit():
        print("Це не число!")
        return
    index = int(index) - 1
    if 0 <= index < len(clients):
        client = clients[index]
        print(f"\nКлієнт №{index + 1}")
        print(f"Прізвище: {client['Прізвище']}")
        print(f"Ім’я: {client['Ім’я']}")
        print(f"Вік: {client['Вік']}")
        print(f"Телефон: {client['Телефон']}")
    else:
        print("Клієнта з таким номером не існує.")


while True:
    print_menu()
    choice = input("Оберіть опцію: ")
    if choice == "1":
        add_client()
    elif choice == "2":
        delete_client()
    elif choice == "3":
        show_all_clients()
    elif choice == "4":
        show_client_by_number()
    elif choice == "5":
        print("До побачення!")
        break
    else:
        print("Невідома опція, спробуйте ще раз.")

clients.pop(0)