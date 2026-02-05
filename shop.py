while True:
    choice = input("\n1. Записать покупки\n2. Выйти\nВыберите действие: ")

    if choice == "1":
        with open("shop.txt", "w") as file:
            while (item := input("Покупка (Enter для выхода): ")):
                file.write(item + "\n")
    elif choice == "2":
        print("Выход...")
        break
    else:
        print("Неверный выбор!")
