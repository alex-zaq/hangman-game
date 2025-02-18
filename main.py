from src.hangman import ConsoleFrontend, GuiFrontend, Hangman, HangmanBackend

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

    # frontend_type = "console"
    frontend_type = "gui"

    match frontend_type:
        case "console":
            frontend = ConsoleFrontend()
        case "gui":
            frontend = GuiFrontend()

    app = Hangman(frontend=frontend, backend=HangmanBackend(words))
    app.start_loop()
