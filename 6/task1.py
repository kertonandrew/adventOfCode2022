import re
import sys
import copy


def task(length):
    message = open("input.txt", "r").readline()
    messageArray = [*message]

    for i, char in enumerate(messageArray):
        snippet = messageArray[i : i + length]

        if len(snippet) == length and len(set(snippet)) == len(snippet):
            return i + length


def main():
    print("task 1: ", task(4))
    print("task 2: ", task(14))


if __name__ == "__main__":
    sys.exit(main())
