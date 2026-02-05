import random

def play_game():
    options = ["камень", "ножницы", "бумага"]
    score = 0

    print("Добро пожаловать в игру 'Камень, Ножницы, Бумага'!")
    print("Играем 20 раундов")

    for round_num in range(1, 20): 
        print(f"Раунд {round_num}")
        player_choice = input("Выбери (камень, ножницы, бумага): ").lower()
        
        if player_choice not in options:
            print("Неверный выбор! Раунд пропускается.")
            continue

        computer_choice = random.choice(options)
        print(f"Компьютер выбрал: {computer_choice}")

        if player_choice == computer_choice:
            print("Ничья!")
        elif (
            (player_choice == "камень" and computer_choice == "ножницы") or
            (player_choice == "ножницы" and computer_choice == "бумага") or
            (player_choice == "бумага" and computer_choice == "камень")
        ):
            print("Ты выиграл этот раунд!")
            score += 1
        else:
            print("Компьютер выиграл этот раунд!")

    print("Игра окончена!")
    print(f"Твой счёт побед: {score} из 20")
play_game()