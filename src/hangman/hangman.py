class Hangman:
    def __init__(self, *, backend, frontend, words) -> None:
        self._backend = backend
        self._backend.set_words(words)
        self._frontend = frontend

    def start_loop(self):
        while True:
            key = input("Enter: ")
            if key == "q":
                break  # noqa: E701
            self._backend.guess(key)
            backend_state = self._backend.get_state()
            self._frontend.draw(backend_state)
