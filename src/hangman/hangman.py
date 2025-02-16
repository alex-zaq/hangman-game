from .backend import GameStatus


class Hangman:
    def __init__(self, *, backend, frontend) -> None:
        self._backend = backend
        self._frontend = frontend
        
        
        
    def start_loop(self):
        
        
        runnning = True
        
        self._frontend.show_start_menu()

        while ((key := self._frontend.read_keys_menu()) not in ("n", "q")):
            ...
            
        if key == "n":
            self._backend.reset()
            self._frontend.set_state(self._backend.get_state())
            self._frontend.draw()
            runnning = True

        if key == "q":
            self._frontend.stop()
            runnning = False


        while runnning:
            key = self._frontend.read_keys()

            if key == "n":
                self._backend.reset()
                self._frontend.set_state(self._backend.get_state())
                self._frontend.draw()
                continue

            if key == "q":
                self._frontend.stop()
                break

            self._backend.guess(key)
            self._frontend.set_state(self._backend.get_state())
            self._frontend.draw()

            if self._backend.get_state().game_status in (
                GameStatus.LOSE,
                GameStatus.WIN,
            ):
                while (key := self._frontend.read_keys_menu()) not in ("n", "q"):
                    ...
                    
                if key == "n":
                    self._backend.reset()
                    self._frontend.set_state(self._backend.get_state())
                    self._frontend.draw()
                if key == "q":
                    self._frontend.stop()
                    runnning = False
                
        

    # def start_loop(self):
    #     while True:
    #         quit_flag = False
    #         if not quit_flag:
    #             start_key = input("n - New Game, q - Quit: ").lower()
    #             if start_key not in ("n", "q"):
    #                 continue
    #             if start_key == "q":
    #                 break
    #             self._backend.reset()
    #             backend_state = self._backend.get_state()
    #             self._frontend.set_state(backend_state)
    #             self._frontend.draw()
    #         else:
    #             break

    #         while True:
    #             key = input("Enter: ")
    #             if key == "q":
    #                 quit_flag = True
    #                 break
    #             if key == "n":
    #                 self._backend.reset()
    #                 backend_state = self._backend.get_state()
    #                 self._frontend.set_state(backend_state)
    #                 self._frontend.draw()
    #                 continue
    #             self._backend.guess(key)
    #             backend_state = self._backend.get_state()
    #             self._frontend.set_state(backend_state)
    #             self._frontend.draw()
    #             if backend_state.game_status in (GameStatus.LOSE, GameStatus.WIN):
    #                 break
