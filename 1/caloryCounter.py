file1 = open("input.txt", "r")
Lines = file1.readlines()

mostCals = 0
currentCals = 0
calArr = []
count = 0

for line in Lines:
    count += 1

    try:
        number = int(line)
        currentCals += number
    except:
        if currentCals > mostCals:
            print(f"CHANGED!!!")
            print(f"{mostCals} < {currentCals}")

            mostCals = currentCals
            print(f"new mostCals: {mostCals}")

        calArr.append(currentCals)
        currentCals = 0

calArr.sort(reverse=True)
topThree = calArr[:3]
topThreeCombined = sum(topThree)

print(f"final mostCals: {mostCals}")
print(f"topThree: {topThree}")
print(f"topThreeCombined: {topThreeCombined}")
