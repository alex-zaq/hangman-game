from hangman import GameStatus, HangmanBackend, State


def test_right_answers():
    hangman_backend = HangmanBackend(["корова", "дерево"])

    hangman_backend.set_state(
        State(
            game_status=GameStatus.IN_PROGRESS,
            wrong_letters_count=0,
            chosen_word="корова",
            word_lst=list("корова"),
        )
    )

    assert hangman_backend.guess("к")

    state = hangman_backend.get_state()

    assert state.word_lst == ["+", "о", "р", "о", "в", "а"]

    assert hangman_backend.guess("о")

    state = hangman_backend.get_state()

    assert state.word_lst == ["+", "+", "р", "+", "в", "а"]

    assert hangman_backend.guess("р")
    assert hangman_backend.guess("в")
    assert hangman_backend.guess("а")

    state = hangman_backend.get_state()

    assert state.word_lst == ["+", "+", "+", "+", "+", "+"]

    assert state.game_status == GameStatus.WIN
