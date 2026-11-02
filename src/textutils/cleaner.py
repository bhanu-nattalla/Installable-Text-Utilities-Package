import re


def clean_text(text: str) -> str:
    """Normalize text while preserving apostrophes inside contractions."""
    normalized_text = text.casefold().replace("’", "'")

    # Keep letters, numbers, whitespace, and apostrophes.
    cleaned_text = re.sub(r"[^\w\s']|_", " ", normalized_text)

    # Remove apostrophes that are not between word characters.
    cleaned_text = re.sub(r"(?<!\w)'|'(?!\w)", " ", cleaned_text)

    return " ".join(cleaned_text.split())
