from collections import Counter
from collections.abc import Iterable


def word_frequencies(tokens: Iterable[str]) -> Counter[str]:
    """Count tokens without considering letter case."""
    return Counter(token.casefold() for token in tokens)
