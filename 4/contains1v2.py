file1 = open("input.txt", "r")
Lines = file1.readlines()

totalContainingPairs = 0


for line in Lines:

    elves = line.split(",")

    elf1 = elves[0].split("-")
    elf2 = elves[1].split("-")

    elf1Range = range(int(elf1[0]), int(elf1[1]) + 1)
    elf2Range = range(int(elf2[0]), int(elf2[1]) + 1)

    print(elf1Range)
    print(elf2Range)

    # make sets of the ranges
    e1s = set(elf1Range)
    e2s = set(elf2Range)

    smallSet = e1s if len(e1s) <= len(e2s) else e2s
    print(smallSet)

    # is the intersection equal to the smaller range
    if e1s.issubset(e2s) or e2s.issubset(e1s):
        totalContainingPairs += 1

    print("--------")


print(totalContainingPairs)
