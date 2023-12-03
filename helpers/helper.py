#!/usr/bin/python3

import os
import requests
import sys
import datetime

COOKIE_PATH = os.path.join(os.path.dirname(__file__), "cookie.txt")
COOKIE = open(COOKIE_PATH).read()


def getInput(day, year):
    URL = f"https://adventofcode.com/{year}/day/{day}/input"
    return requests.get(url=URL, cookies={"session": COOKIE}).text.rstrip()


def saveCustomDay(day, year):
    print(f"Parsing day {day} of {year}")
    f = open("input.txt", "w")
    f.write(getInput(day, year))
    f.close()
    print("Parsing done.")


def saveToday():
    year = int(datetime.date.today().year)
    day = int(datetime.date.today().day)
    saveCustomDay(day, year)


# Post request to send answer, not used because in practice it doesn't save that much time.
def sendAnswer(day, year, output, firstlevel):
    URL = f"https://adventofcode.com/{year}/day/{day}/answer"
    txt = requests.post(
        url=URL,
        data={"level": {True: 1, False: 2}[firstlevel], "answer": output},
        cookies={"session": COOKIE},
    ).text
    return "That's the right answer!" in txt


def main():
    args = sys.argv[1:]
    arglen = len(args)

    if arglen == 0:
        usageExit()

    if args[0].lower() == "today":
        saveToday()
        return

    if args[0].lower() == "custom":
        year, day = int(args[1]), int(args[2])
        saveCustomDay(day, year)
        return

    usageExit()


def usageExit():
    print("Usage:")
    print("1) ./helper today - parse today into input.txt")
    print("2) ./helper custom YEAR DAY - parse a custom date into input.txt")
    exit(0)


if __name__ == "__main__":
    main()
