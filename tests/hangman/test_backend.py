from hangman import GameStatus, HangmanBackend, State


def test_right_answers():
    hangman_backend = HangmanBackend(["дерево"])
    selected_word = "дерево"
    hangman_backend.set_state(
        State(
            game_status=GameStatus.IN_PROGRESS,
            wrong_letters_count=0,
            wrong_letters=[],
            chosen_word=selected_word,
            word_lst=list(selected_word),
        )
    )

    for letter in selected_word:
        hangman_backend.guess(letter)

    state = hangman_backend.get_state()

    assert state.game_status == GameStatus.WIN
    assert state.wrong_letters_count == 1
    assert state.word_lst == ["+", "+", "+", "+", "+", "+"]


def test_wrong_anserts():
    hangman_backend = HangmanBackend(["дерево"])

    selected_word = "дерево"
    hangman_backend.set_state(
        State(
            game_status=GameStatus.IN_PROGRESS,
            wrong_letters_count=0,
            wrong_letters=[],
            chosen_word=selected_word,
            word_lst=list(selected_word),
        )
    )

    for _ in selected_word:
        hangman_backend.guess("a")

    state = hangman_backend.get_state()

    assert state.game_status == GameStatus.LOSE
    assert state.wrong_letters_count == len(selected_word)
    assert state.word_lst == ["д", "е", "р", "е", "в", "о"]
