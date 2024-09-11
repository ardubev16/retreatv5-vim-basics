#!/usr/bin/env python3
"""
Author: Lorenzo Bevilacqua
Description: There is a Linting rule that forbids the use of format strings inside
    log messages, for more infos see https://docs.astral.sh/ruff/rules/logging-f-string/
Objective: Modify the following code in a way that satisfies the described rule, i.e.
    `logging.info(f"{user} - Something happened")`
    becomes
    `logging.info("%s - Something happened", user)`
"""

import logging

friend, question, your_name = "Gabriele", "how are you?", "Dear student"

logging.info(f"Hi, {your_name}, {question}")
logging.info(f"Do you know my friend {friend}?")
