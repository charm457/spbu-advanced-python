"""Command-line interface."""
import argparse

from .normalize import tokenize
from .starts import count_words, top_n
from .io import read_text


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="textstats")
    parser.add_argument("paths", nargs="+", help="Input text files")
    parser.add_argument("--top", type=int, default=10, help="How many items to show")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("--lower", dest="lower", action="store_true", default=True)
    group.add_argument("--no-lower", dest="lower", action="store_false")

    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    all_tokens: list[str] = []
    for p in args.paths:
        all_tokens.extend(tokenize(read_text(p), lower=args.lower))

    freqs = count_words(all_tokens)
    for word, count in top_n(freqs, args.top):
        print(f"{word}\t{count}")

    return 0