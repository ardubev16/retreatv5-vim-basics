#!/usr/bin/env python3
"""
Author: Lorenzo Bevilacqua
Description: Here you will learn more advanced vim combinations, with the help of:
    <action>i<motion>: do something inside a certain range
    <action>a<motion>: do something inside a certain range including extremes
Objective: Copy the strings passed as argument to the print in the first function and
    paste them as comments at the end of the file

    Copy the parameter definition of the second function and paste it also in the third,
    copy the strings passed as argument to the print in the second function and paste them
    in the prints in the third function, visual mode can help.
"""


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


def say_something():
    print()
    print()
    print()
    print()


if __name__ == "__main__":
    say_hello("John")
    say_goodbye("John")
