from src.hangman import Hangman, HangmanBackend, HangmanFrontend

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

    app = Hangman(frontend=HangmanFrontend(), backend=HangmanBackend(words))

    app.start_loop()
