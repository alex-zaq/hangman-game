from src.hangman import Hangman, HangmanBackend, ConsoleFrontend

if __name__ == "__main__":
    
    words = [
        "Программист",
        "Врач",
        "Учитель",
        "Инженер",
        "Дизайнер",
        "Менеджер",
        "Журналист",
    ]

    app = Hangman(frontend=ConsoleFrontend(), backend=HangmanBackend(words))

    app.start_loop()
