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

friend, question, your_name, place = (
    "Gabriele",
    "how are you?",
    "Dear student",
    "Val di Sole",
)

# TY GhatGPT
logging.critical(f"Hey {your_name}, I wanted to ask: {question}")
logging.info(f"{your_name}, have you been to the {place}?")
logging.warning(f"Hey {your_name}, I wanted to ask: {question}")
logging.debug(f"{friend} was asking if you are going to the {place}.")
logging.critical(f"Do you know my friend {friend}?")
logging.info(f"Do you know my friend {friend}?")
logging.info(f"How do you feel about {friend} joining the {place}?")
logging.error(f"Hi, {your_name}, {question}")
logging.critical(f"Do you know my friend {friend}?")
logging.warning(f"Do you know my friend {friend}?")
logging.warning(f"{your_name}, have you been to the {place}?")
logging.info(f"How do you feel about {friend} joining the {place}?")
logging.warning(f"Do you know my friend {friend}?")
logging.error(f"{friend} was asking if you are going to the {place}.")
logging.error(f"How do you feel about {friend} joining the {place}?")
logging.warning(f"Hey {your_name}, I wanted to ask: {question}")
logging.error(f"Hi, {your_name}, {question}")
logging.critical(f"Do you know my friend {friend}?")
logging.error(f"Do you know my friend {friend}?")
logging.warning(f"{friend} was asking if you are going to the {place}.")
logging.warning(f"How do you feel about {friend} joining the {place}?")
logging.error(f"{friend} was asking if you are going to the {place}.")
logging.warning(f"How do you feel about {friend} joining the {place}?")
logging.debug(f"Hi, {your_name}, {question}")
logging.info(f"Hey {your_name}, I wanted to ask: {question}")
logging.debug(f"How do you feel about {friend} joining the {place}?")
# when will this log messages end...
logging.error(f"Hey {your_name}, I wanted to ask: {question}")
logging.info(f"Hey {your_name}, I wanted to ask: {question}")
logging.info(f"Hi, {your_name}, {question}")
logging.error(f"How do you feel about {friend} joining the {place}?")
logging.warning(f"Hi, {your_name}, {question}")
logging.info(f"Do you know my friend {friend}?")
logging.warning(f"Do you know my friend {friend}?")
logging.warning(f"Hi, {your_name}, {question}")
logging.debug(f"{your_name}, have you been to the {place}?")
logging.info(f"{your_name}, have you been to the {place}?")
logging.warning(f"{friend} was asking if you are going to the {place}.")
logging.error(f"Hey {your_name}, I wanted to ask: {question}")
logging.error(f"How do you feel about {friend} joining the {place}?")
logging.critical(f"How do you feel about {friend} joining the {place}?")
logging.warning(f"Hey {your_name}, I wanted to ask: {question}")
logging.debug(f"How do you feel about {friend} joining the {place}?")
logging.error(f"Hey {your_name}, I wanted to ask: {question}")
logging.error(f"{your_name}, have you been to the {place}?")
logging.debug(f"Hi, {your_name}, {question}")
logging.info(f"How do you feel about {friend} joining the {place}?")
logging.error(f"{your_name}, have you been to the {place}?")
logging.warning(f"Do you know my friend {friend}?")
logging.info(f"{your_name}, have you been to the {place}?")
logging.warning(f"How do you feel about {friend} joining the {place}?")
# hopefully soon...
logging.debug(f"Hi, {your_name}, {question}")
logging.error(f"Hi, {your_name}, {question}")
logging.info(f"How do you feel about {friend} joining the {place}?")
logging.critical(f"Hi, {your_name}, {question}")
logging.error(f"{your_name}, have you been to the {place}?")
logging.debug(f"{your_name}, have you been to the {place}?")
logging.info(f"Do you know my friend {friend}?")
logging.info(f"Do you know my friend {friend}?")
logging.info(f"{your_name}, have you been to the {place}?")
logging.error(f"How do you feel about {friend} joining the {place}?")
logging.debug(f"How do you feel about {friend} joining the {place}?")
logging.warning(f"{friend} was asking if you are going to the {place}.")
logging.critical(f"{friend} was asking if you are going to the {place}.")
logging.critical(f"Hi, {your_name}, {question}")
logging.warning(f"{your_name}, have you been to the {place}?")
logging.warning(f"Hey {your_name}, I wanted to ask: {question}")
logging.debug(f"Hey {your_name}, I wanted to ask: {question}")
logging.info(f"Hi, {your_name}, {question}")
logging.debug(f"Hi, {your_name}, {question}")
logging.warning(f"Hi, {your_name}, {question}")
logging.info(f"{your_name}, have you been to the {place}?")
logging.info(f"Hi, {your_name}, {question}")
# almost there
logging.critical(f"How do you feel about {friend} joining the {place}?")
logging.error(f"Hey {your_name}, I wanted to ask: {question}")
logging.info(f"How do you feel about {friend} joining the {place}?")
logging.error(f"How do you feel about {friend} joining the {place}?")
logging.critical(f"Do you know my friend {friend}?")
logging.debug(f"How do you feel about {friend} joining the {place}?")
logging.warning(f"Hi, {your_name}, {question}")
logging.error(f"Hi, {your_name}, {question}")
logging.warning(f"{your_name}, have you been to the {place}?")
logging.error(f"{your_name}, have you been to the {place}?")
logging.debug(f"Hey {your_name}, I wanted to ask: {question}")
logging.warning(f"Do you know my friend {friend}?")
logging.warning(f"Do you know my friend {friend}?")
logging.info(f"{your_name}, have you been to the {place}?")
logging.debug(f"How do you feel about {friend} joining the {place}?")
logging.critical(f"Do you know my friend {friend}?")
logging.critical(f"{friend} was asking if you are going to the {place}.")
logging.info(f"{your_name}, have you been to the {place}?")
logging.debug(f"Hey {your_name}, I wanted to ask: {question}")
logging.error(f"Hey {your_name}, I wanted to ask: {question}")
logging.info(f"{your_name}, have you been to the {place}?")
logging.critical(f"{friend} was asking if you are going to the {place}.")
logging.critical(f"Do you know my friend {friend}?")
logging.debug(f"How do you feel about {friend} joining the {place}?")
logging.critical(f"Hey {your_name}, I wanted to ask: {question}")
logging.debug(f"Hey {your_name}, I wanted to ask: {question}")
logging.debug(f"Do you know my friend {friend}?")
logging.critical(f"{friend} was asking if you are going to the {place}.")
# luckly I'm using Vim
