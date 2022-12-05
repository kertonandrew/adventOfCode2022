file1 = open("input.txt", "r")
Lines = file1.readlines()

totalProrityScore = 0


def getScore(char):
    if char.isupper():
        return ord(char) - ord("@") + 26
    return ord(char) - ord("`")


for line in Lines:
    s1, s2 = line[: len(line) // 2], line[len(line) // 2 :]

    arr1 = set([*s1])
    arr2 = set([*s2])

    for char in arr1 & arr2:
        score = getScore(char)
        print(f"{char}: {score}")
        totalProrityScore += score

print(totalProrityScore)
