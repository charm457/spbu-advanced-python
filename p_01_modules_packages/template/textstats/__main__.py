"""Module entrypoint.

Enables running:

python -m p_01_modules_packages.template.textstats ...
"""
from .cli import main


if __name__ == "__main__":
    raise SystemExit(main())