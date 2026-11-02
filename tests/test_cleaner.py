from textutils.cleaner import clean_text


def test_clean_text_lowercases_and_removes_punctuation() -> None:
    result = clean_text("  Hello, World!!  ")

    assert result == "hello world"


def test_clean_text_preserves_contractions() -> None:
    result = clean_text("Don't worry, you'll succeed.")

    assert result == "don't worry you'll succeed"


def test_clean_text_handles_curly_apostrophes() -> None:
    result = clean_text("Don’t stop. You’ll do well!")

    assert result == "don't stop you'll do well"


def test_clean_text_removes_extra_whitespace() -> None:
    result = clean_text("Hello\t\tworld\n\nPython")

    assert result == "hello world python"


def test_clean_text_handles_empty_input() -> None:
    assert clean_text("") == ""
