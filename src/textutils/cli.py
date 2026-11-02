import argparse
from collections.abc import Sequence

from textutils.cleaner import clean_text
from textutils.frequency import word_frequencies
from textutils.tokenizer import tokenize


def create_parser() -> argparse.ArgumentParser:
    """Create the command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="Clean text, tokenize it, and count word frequencies."
    )
    parser.add_argument(
        "text",
        help="Text to analyze. Enclose it in quotes when it contains spaces.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Run the text-utils command."""
    parser = create_parser()
    arguments = parser.parse_args(argv)

    cleaned_text = clean_text(arguments.text)
    tokens = tokenize(arguments.text)
    frequencies = word_frequencies(tokens)

    print("Cleaned text")
    print("-" * 12)
    print(cleaned_text or "No text found.")

    print("\nTokens")
    print("-" * 6)
    print(", ".join(tokens) if tokens else "No tokens found.")

    print("\nWord frequencies")
    print("-" * 16)
    if frequencies:
        for word, count in frequencies.most_common():
            print(f"{word}: {count}")
    else:
        print("No words found.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
