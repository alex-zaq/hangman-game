from ..backend import MAX_WRONG_LETTERS_COUNT, GameStatus
from .stages import hangman_stages as stages


class ConsoleFrontend:
    def __init__(self):
        self.stages_dict = {i: elem for i, elem in enumerate(stages)}


    def show_start_menu(self):
        print("Hangman")

        
    def stop(self):
        ...


    def read_keys_menu(self):
        return input("n - New Game, q - Quit:").lower()

    def read_keys(self):
        return input("Enter a letter: ").lower()
        

    def set_state(self, state):
        self.state = state

    def draw(self):
        hangman_figure_str = self._get_str_hangman_by_stage()
        words_str = self._get_str_words()
        wrong_guesses_str = self._get_str_wrong_guesses()
        message = self._get_str_game_over()
        result = "\n".join([hangman_figure_str, words_str, wrong_guesses_str, message])
        print(result)

    def _get_str_words(self):
        orig_word = self.state.chosen_word

        if self.state.game_status == GameStatus.IN_PROGRESS:
            res = [
                orig_letter if letter == "+" else "_"
                for orig_letter, letter in zip(orig_word, self.state.word_lst)
            ]
        elif self.state.game_status in (GameStatus.LOSE, GameStatus.WIN):
            res = [orig_letter for orig_letter in orig_word]
        return " ".join(res)

    def _get_str_hangman_by_stage(self):
        stage = self.state.wrong_letters_count
        return self.stages_dict[stage]

    def _get_str_wrong_guesses(self):
        return f"Wrong guesses: {self.state.wrong_letters_count} / {MAX_WRONG_LETTERS_COUNT}"

    def _get_str_game_over(self):
        match self.state.game_status:
            case GameStatus.LOSE:
                return "You lose! (Press n - New Game, q - Quit)"
            case GameStatus.IN_PROGRESS:
                return ""
            case GameStatus.WIN:
                return "You win! (Press n - New Game, q - Quit)"
