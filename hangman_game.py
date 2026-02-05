import random
import sys


HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===""",
    """
     +---+
     O   |
         |
         |
        ===""",
    """
     +---+
     O   |
     |   |
         |
        ===""",
    """
     +---+
     O   |
    /|   |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ==="""
]

MAX_WRONG = len(HANGMAN_PICS) - 1

WORDS = [
    "python", "игра", "код", "программа", "книга", "робот", "мир", "солнце",
    "компьютер", "алгоритм", "переменная", "разработка", "искусственный",
    "интеллект", "интерфейс", "моделирование", "архитектура", "функция",
    "библиотека", "информатика", "проектирование", "взаимодействие", "платформа",
    "приложение", "эксперимент", "оптимизация", "технология", "программирование"
]

def choose_difficulty():
    print("Выберите уровень сложности:")
    print("1 — Лёгкий (слова до 5 букв)")
    print("2 — Средний (слова до 8 букв)")
    print("3 — Сложный (слова от 12 букв)")
    while True:
        choice = input("Введите 1, 2 или 3: ").strip()
        if choice in ["1", "2", "3"]:
            return int(choice)
        else:
            print("Некорректный выбор. Попробуйте снова.")

def filter_words_by_difficulty(level):
    if level == 1:
        return [w for w in WORDS if len(w) <= 5]
    elif level == 2:
        return [w for w in WORDS if 6 <= len(w) <= 8]
    else:
        return [w for w in WORDS if len(w) >= 12]

def choose_word(word_list):
    return random.choice(word_list).lower()

def display_state(wrong_guesses, correct_letters, secret_word):
    print(HANGMAN_PICS[len(wrong_guesses)])
    print()
    blanks = [ch if ch in correct_letters else "_" for ch in secret_word]
    print("Слово:", " ".join(blanks))
    print()
    print("Ошибочные буквы:", " ".join(sorted(wrong_guesses)) if wrong_guesses else "—")
    print(f"Осталось попыток: {MAX_WRONG - len(wrong_guesses)}")
    print()

def get_player_guess(already_guessed):
    while True:
        guess = input("Введи букву (или слово целиком): ").strip().lower()
        if not guess:
            print("Пустой ввод. Попробуй снова.")
        elif not guess.isalpha():
            print("Можно вводить только буквы.")
        elif guess in already_guessed:
            print("Ты уже пробовал эту букву/слово.")
        else:
            return guess

def play_once():
    difficulty = choose_difficulty()
    words = filter_words_by_difficulty(difficulty)

    if not words:
        print("Нет слов подходящей длины! Добавь больше слов в список.")
        return False

    secret = choose_word(words)
    wrong = set()
    correct = set()

    print(f"\nСлово выбрано! Его длина: {len(secret)} букв(ы). Удачи!\n")

    while True:
        display_state(wrong, correct, secret)
        guess = get_player_guess(wrong.union(correct))

        if len(guess) > 1:
            if guess == secret:
                print(f"Поздравляю! Ты угадал слово: {secret}")
                return True
            else:
                print("Неверно! Это не то слово.")
                wrong.add(guess)
        else:
            if guess in secret:
                correct.add(guess)
                print(f"Буква '{guess}' есть в слове!")
                if all(ch in correct for ch in secret):
                    print(f"\nПобеда! Слово: {secret}")
                    return True
            else:
                wrong.add(guess)
                print(f"Буквы '{guess}' нет в слове.")
                if len(wrong) >= MAX_WRONG:
                    display_state(wrong, correct, secret)
                    print(f"Ты проиграл! Загаданное слово: {secret}")
                    return False


def main():
    print("ВИСЕЛИЦА")
    print("Угадывай слово по буквам. Можно вводить всё слово целиком.\n")

    wins = 0
    losses = 0

    while True:
        result = play_once()
        if result:
            wins += 1
        else:
            losses += 1

        print(f"\nТвой счёт: Победы — {wins}, Поражения — {losses}")
        again = input("Сыграть ещё раз? (д/н): ").strip().lower()
        if again not in ["д", "y", "yes"]:
            print("Спасибо за игру! До встречи")
            break
        print("\n" + "-" * 40 + "\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nИгра прервана. Пока!")
        sys.exit(0)
