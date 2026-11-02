from textutils.cleaner import clean_text


def tokenize(text: str) -> list[str]:
    """Clean text and split it into tokens.

    Apostrophes within contractions are preserved, such as "don't".
    """
    cleaned_text = clean_text(text)

    if not cleaned_text:
        return []

    return cleaned_text.split()
