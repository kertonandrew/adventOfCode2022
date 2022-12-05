opMap = {
    "A": "R",
    "B": "P",
    "C": "S",
}

myMap = {
    "X": "R",
    "Y": "P",
    "Z": "S",
}

win = {
    "R": "S",
    "P": "R",
    "S": "P",
}

score = {
    "R": 1,
    "P": 2,
    "S": 3,
}

file1 = open("input2.txt", "r")
Lines = file1.readlines()

runningScore = 0

for line in Lines:
    roundScore = 0

    try:
        arr = line.split()
        op = opMap[arr[0]]
        me = myMap[arr[1]]

        if win[me] == op:
            roundScore = 6
        elif op == me:
            roundScore = 3

        roundScore += score[me]

        print(f"{me} -> {op}")
        print(f"winner?: {win[me] == op}")
        print(f"roundScore: {roundScore}")

        runningScore += roundScore

    except:
        print("error")
        break

print(runningScore)
