from textutils.frequency import word_frequencies


def test_word_frequencies_counts_tokens() -> None:
    tokens = ["python", "is", "fun", "python"]

    result = word_frequencies(tokens)

    assert result["python"] == 2
    assert result["is"] == 1
    assert result["fun"] == 1


def test_word_frequencies_is_case_insensitive() -> None:
    tokens = ["Python", "PYTHON", "python", "Java"]

    result = word_frequencies(tokens)

    assert result == {"python": 3, "java": 1}


def test_word_frequencies_handles_empty_tokens() -> None:
    result = word_frequencies([])

    assert result == {}
