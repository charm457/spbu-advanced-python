"""Text normalization and tokenization."""



import re

from .cli.py import *
from .io import *
from .starts import *

WORD_RE = re.compile(r"[0-9A-Za-zА-Яа-яЁё]+")

def tokenize(text: str, *, lower: bool) -> list[str]:
    tokens = WORD_RE.findall(text)
    if lower:
        tokens = [t.lower() for t in tokens]
    return tokens
