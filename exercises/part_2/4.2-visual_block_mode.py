#!/usr/bin/env python3
"""
Author: Lorenzo Bevilacqua
Description: Here you will learn the power of Visual Block mode while trying to fix
    ruff rule T201 (https://docs.astral.sh/ruff/rules/print/). Remember:

    C-v: visual block mode
    c: delete selected text and enter insert mode
Objective: Fix the mentioned rule substituting `print` with `logging.info`.
    Try writing the new function name the least times possible.
"""

import logging


def say_hello(name: str):
    print("Hello hello stranger!")
    print(f"How are you doing {name}?")
    print("Are you enjoing this workshop?")
    print("Hopefully you are having fun!")


def say_goodbye(name: str):
    print("Goodbye stranger!")
    print(f"Hope to see you soon {name}!")
    print("Take care!")
    print("Bye bye!")


if __name__ == "__main__":
    say_hello("John")
    say_goodbye("John")
