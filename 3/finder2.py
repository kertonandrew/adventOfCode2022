from itertools import islice


def next_n_lines(file_opened, N):
    return [x.strip() for x in islice(file_opened, N)]


def getScore(char):
    if char.isupper():
        return ord(char) - ord("@") + 26
    return ord(char) - ord("`")


totalProrityScore = 0

file = open("input.txt", "r")

while file:
    lines = next_n_lines(file, 3)

    if len(lines) < 1:
        break

    arr1 = set([*lines[0]])
    arr2 = set([*lines[1]])
    arr3 = set([*lines[2]])

    for char in arr1 & arr2 & arr3:
        score = getScore(char)
        print(f"{char}: {score}")
        totalProrityScore += score

file.close()

print(totalProrityScore)
