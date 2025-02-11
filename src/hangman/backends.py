import random
from dataclasses import dataclass
from enum import Enum

MAX_WRONG_LETTERS_COUNT = 6
DEFAULT_MIN_LEN = 5


class GameStatus(Enum):
    WIN = 1
    LOSE = 2
    IN_PROGRESS = 3


@dataclass
class State:
    game_status: GameStatus
    wrong_letters_count: int
    chosen_word: str
    word_lst: list


class HangmanBackend:
    def __init__(self, words_db: list, min_len: int = DEFAULT_MIN_LEN):
        self._words_db = words_db
        self._reset(min_len)

    def _reset(self, min_len: int):
        self._chosen_word = self._choose_random_word(self.min_len)
        self._wrong_letters_count = 0
        self._word_lst = list(self._chosen_word)
        self._game_status = GameStatus.IN_PROGRESS

    def _choose_random_word(self, min_len: int) -> None:
        filterd_words = [word for word in self._words_db if len(word) >= min_len]
        if not filterd_words:
            raise Exception(f"No words with length >= {min_len}")
        chosen_word = random.choice(self._words_db)
        return chosen_word

    def _increase_wrong_letters_count(self) -> None:
        self.wrong_letters_count += 1
        if self.wrong_letters_count == MAX_WRONG_LETTERS_COUNT:
            self.game_status = GameStatus.LOSE

    def guess(self, letter: str) -> bool:
        if self._game_status in (GameStatus.WIN, GameStatus.LOSE):
            raise Exception(f"Game over {self.game_status}")

        if letter not in self._word_lst:
            self._increase_wrong_letters_count()
            return False

        self._word_lst = [x if x != letter else "+" for x in self._word_lst]

        if all(x == "+" for x in self._word_lst):
            self.state.game_status = GameStatus.WIN

        return True

    def get_state(self) -> State:
        state = State()
        state.game_status = self._game_status
        state.wrong_letters_count = self._wrong_letters_count
        state.chosen_word = self._chosen_word
        state.word_lst = self._word_lst
        return state
