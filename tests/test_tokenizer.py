from textutils.tokenizer import tokenize


def test_tokenize_splits_cleaned_text_into_words() -> None:
    result = tokenize("Hello, world! Python is fun.")

    assert result == ["hello", "world", "python", "is", "fun"]


def test_tokenize_preserves_contractions() -> None:
    result = tokenize("Don't worry, you'll learn Python.")

    assert result == ["don't", "worry", "you'll", "learn", "python"]


def test_tokenize_returns_empty_list_for_empty_text() -> None:
    assert tokenize("") == []


def test_tokenize_returns_empty_list_for_punctuation_only() -> None:
    assert tokenize("!!! ??? ...") == []
