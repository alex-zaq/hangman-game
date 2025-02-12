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
    def __init__(self, words):
        self._words_lst = words

    def reset(self):
        self._chosen_word = self.choose_random_word()
        self._word_lst = list(self._chosen_word)
        self._wrong_letters_count = 0
        self._game_status = GameStatus.IN_PROGRESS

    def choose_random_word(self) -> None:
        chosen_word = random.choice(self._words_lst)
        return chosen_word

    def increase_wrong_letters_count(self) -> None:
        self._wrong_letters_count += 1
        if self._wrong_letters_count >= MAX_WRONG_LETTERS_COUNT:
            self.game_status = GameStatus.LOSE

    def guess(self, letter: str) -> bool:
        if self._game_status in (GameStatus.WIN, GameStatus.LOSE):
            raise Exception(f"Game over {self.game_status}")

        if letter not in self._word_lst:
            self.increase_wrong_letters_count()
            return False

        self._word_lst = [x if x != letter else "+" for x in self._word_lst]

        if all(x == "+" for x in self._word_lst):
            self._game_status = GameStatus.WIN

        return True

    def get_status(self):
        return self._game_status

    def get_state(self) -> State:
        state = State(
            game_status=self._game_status,
            wrong_letters_count=self._wrong_letters_count,
            chosen_word=self._chosen_word,
            word_lst=self._word_lst,
        )
        return state

    def set_state(self, state: State):
        self._game_status = state.game_status
        self._wrong_letters_count = state.wrong_letters_count
        self._chosen_word = state.chosen_word
        self._word_lst = state.word_lst
