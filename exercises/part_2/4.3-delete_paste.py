#!/usr/bin/env python3
"""
Author: Lorenzo Bevilacqua
Description: When you delete a line in Vim, it is copied to a register. If you want
    to learn more about registers, check out: https://stackoverflow.com/questions/1497958/how-do-i-use-vim-registers
    Remember:

    dd: delete current line
    yy: yank current line
    D: delete from cursor to end of line
    p: paste text after cursor
    P: paste text before cursor
Objective: Delete the commented lines and paste them at the end of the file.
    If a line contains a comment at the end, delete that comment as well.
"""

# ignore the random code, I'm too lazy to write something meaningful, this is the
# best Copilot can do for me, I guess


def say_hello(name: str):
    # print("Hello hello stranger!")
    print(f"How are you doing {name}?")  # This is a comment at the end of the line
    # print("Are you enjoing this workshop?")
    print("Hopefully you are having fun!")
    # print("Goodbye stranger!")
    # print(f"Hope to see you soon {name}!")
    print("Take care!")  # This is a comment at the end of the line


def say_goodbye(name: str):
    # print("Goodbye stranger!")
    print(f"Hope to see you soon {name}!")
    # print("Take care!")
    print("Bye bye!")  # This is a comment at the end of the line
