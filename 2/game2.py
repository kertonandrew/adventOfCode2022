opMap = {
    "A": "R",
    "B": "P",
    "C": "S",
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

outcomeMap = {
    "X": "L",
    "Y": "D",
    "Z": "W",
}

file1 = open("input2.txt", "r")
Lines = file1.readlines()

runningScore = 0

for line in Lines:
    roundScore = 0

    arr = line.split()
    op = opMap[arr[0]]
    outcome = outcomeMap[arr[1]]

    if outcome == "D":
        roundScore = 3 + score[op]
    elif outcome == "W":
        # Key from value
        roundScore = 6 + score[[k for k, v in win.items() if v == op][0]]
    else:
        roundScore = score[win[op]]

    print(f"roundScore: {roundScore}")

    runningScore += roundScore


print(runningScore)
