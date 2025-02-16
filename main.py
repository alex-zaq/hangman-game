from src.hangman import GuiFrontend, Hangman, HangmanBackend

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

    # console_app = Hangman(frontend=ConsoleFrontend(), backend=HangmanBackend(words))
    # console_app.start_loop()


    gui_app = Hangman(frontend=GuiFrontend(), backend=HangmanBackend(words))
    gui_app.start_loop()
