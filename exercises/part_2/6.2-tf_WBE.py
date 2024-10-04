#!/usr/bin/env python3
"""
Author: Lorenzo Bevilacqua
Description: Discover the speed of `t` and `f` motions in Vim. Also try out the wbe variants `W`, `B`, `E`.
    t: move the cursor on the character before the next occurrence of a character
    f: move the cursor on the character itself

    W: move the cursor to the beginning of the next word (punctuation included)
    B: move the cursor to the beginning of the previous word (punctuation included)
    E: move the cursor to the end of the next word (punctuation included)
Objective: This is a snippet from my bot that sends everyday the price of the gas and current,
    src: https://github.com/ardubev16/punbot

    Remove the `to_float`, `to_smc`, `to_kwh` functions and put the implemantation directly
    where they are used (:83, :84).

    `Prices.__str__` and `Prices.str_with_diff` are missing the gas value, can you add it?
"""

from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.mercatoelettrico.org/it/{}"


def icon(avg: float, new_value: float) -> str:
    MAX_DIFF = 0.00001  # noqa: N806

    diff = new_value - avg
    if abs(diff) < MAX_DIFF:
        return "🔷"
    if diff > 0:
        return "📈"
    # diff < 0
    return "📉"


@dataclass
class Prices:
    pun: float
    mgp: float

    def __str__(self):
        return f"""\
<b>PUN</b>: {self.pun:.5f} €/kWh"""

    def str_with_diff(self, new_prices: "Prices") -> str:
        return f"""\
<b>PUN</b>: {self.pun:.5f} €/kWh {icon(self.pun, new_prices.pun)}"""


def to_float(value: str) -> float:
    return float(value.strip().replace(",", "."))


def to_kwh(value: str) -> float:
    return to_float(value) / 1000


def to_smc(value: str) -> float:
    return to_float(value) * 0.0105833


def get_prices() -> Prices:
    response = requests.get(BASE_URL.format("tools/AccessoDati.aspx"), timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")
    inputs = {i["name"]: i.get("value") for i in soup.find_all("input")}
    data = {
        "__VIEWSTATE": inputs["__VIEWSTATE"],
        "__EVENTVALIDATION": inputs["__EVENTVALIDATION"],
        "ctl00$ContentPlaceHolder1$CBAccetto1": "on",
        "ctl00$ContentPlaceHolder1$CBAccetto2": "on",
        "ctl00$ContentPlaceHolder1$Button1": "Accetto",
    }

    s = requests.Session()
    s.post(BASE_URL.format("tools/AccessoDati.aspx"), data=data)
    response = s.get(BASE_URL.format("default.aspx"))
    soup = BeautifulSoup(response.text, "html.parser")
    pun = to_kwh(soup.find("span", {"id": "ContentPlaceHolder1_lblMedia"}).text)
    mgp = to_smc(
        soup.find("table", {"id": "ContentPlaceHolder1_gvMGPGas"})
        .find_all("table")[3]
        .text
    )

    return Prices(pun=pun, mgp=mgp)


if __name__ == "__main__":
    print(get_prices())  # noqa: T201
