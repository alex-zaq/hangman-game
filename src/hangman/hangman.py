from hangman.backend import GameStatus


class Hangman:
    def __init__(self, *, backend, frontend) -> None:
        self._backend = backend
        self._frontend = frontend

    def start_loop(self):
        while True:
            quit_flag = False
            if not quit_flag:
                strart_key = input("n - New Game, q - Quit: ").lower()
                if strart_key not in ("n", "q"):
                    continue
                if strart_key == "q":
                    break
                self._backend.reset()
                backend_state = self._backend.get_state()
                self._frontend.set_state(backend_state)
                self._frontend.draw()
            else:
                break

            while True:
                key = input("Enter: ")
                if key == "q":
                    quit_flag = True
                    break
                if key == "n":
                    self._backend.reset()
                    backend_state = self._backend.get_state()
                    self._frontend.set_state(backend_state)
                    self._frontend.draw()
                    continue
                self._backend.guess(key)
                backend_state = self._backend.get_state()
                self._frontend.set_state(backend_state)
                self._frontend.draw()
                if backend_state.game_status in (GameStatus.LOSE, GameStatus.WIN):
                    break
