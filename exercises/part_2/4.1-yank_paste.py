#!/usr/bin/env python3
"""
Author: Gabriele Bocchi
Description: This exercise is about copying and pasting code with vim visual mode. Remember:
    v: enter visual mode
    V: enter visual line mode
    y: yank selected text
    yy: yank current line
    p: paste text after cursor
    P: paste text before cursor
Objective: Add the missing functions to the code below using Visual mode, Yank and Paste.
    Try experimenting with different visual modes and pasting options.
    If you make a mistake, remember that you can undo with `u` and redo with `C-r`.
"""

import logging


def add_one(n: int) -> int:
    logging.info("Something very long that I don't want to write again")
    logging.info("n: %s", n)
    return n + 1


def main() -> None:
    n = 10

    assert add_one(n) == 11
    assert add_two(n) == 12
    assert add_three(n) == 13
    assert add_four(n) == 14
    assert add_five(n) == 15


if __name__ == "__main__":
    main()
