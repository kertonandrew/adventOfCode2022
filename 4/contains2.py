file1 = open("input.txt", "r")
Lines = file1.readlines()

totalContainingPairs = 0


for line in Lines:

    elves = line.split(",")

    elf1 = elves[0].split("-")
    elf2 = elves[1].split("-")

    elf1Range = range(int(elf1[0]), int(elf1[1]) + 1)
    elf2Range = range(int(elf2[0]), int(elf2[1]) + 1)

    # make sets of the ranges
    e1s = set(elf1Range)
    e2s = set(elf2Range)

    print(e1s)
    print(e2s)

    # create an intersection
    intersection = e1s & e2s
    print(intersection)

    # is the intersection equal to the smaller range
    if len(intersection) > 0:
        totalContainingPairs += 1

    print("--------")


print(totalContainingPairs)
