import re
import sys
import copy


def all_unique(item):
    return len(set(item)) == len(item)


length = 14


def task1():
    file1 = open("input.txt", "r")
    lines = file1.readlines()

    message = lines[0]
    messageArray = [*message]

    for i, char in enumerate(messageArray):
        snippet = messageArray[i : i + length]

        if len(snippet) == length and len(set(snippet)) == len(snippet):
            print("found")
            print(snippet)

            # index of first + size of block + get next
            print(i + length)

            break


def main():
    task1()


if __name__ == "__main__":
    sys.exit(main())
