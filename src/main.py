from hangman import Hangman, HangmanBackend, HangmanFrontend, TextFileReader

if __name__ == "__main__":
    words = TextFileReader.read("data/words_case.txt")

    app = Hangman(frontend=HangmanFrontend(), backend=HangmanBackend(), words=words)

    app.start_loop()
