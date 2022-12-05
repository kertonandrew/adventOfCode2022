import re
import sys
import copy


def getStacks():
    file1 = open("input.txt", "r")
    lines = file1.readlines()
    stacks = []

    for line in lines:
        if line.split()[0].isnumeric():
            return stacks

        # Create the stacks
        slots = [line[i : i + 4].strip(" ][\n") for i in range(0, len(line), 4)]

        for slotIndex, slot in enumerate(slots):

            if not stacks:
                stacks.append([slot])
            elif len(stacks) == slotIndex:
                stacks.append([slot])
            else:
                stacks[slotIndex].insert(0, slot)
            slotIndex += 1

        # Clean the stacks
        for i, stack in enumerate(stacks):
            if "" in stack:
                stacks[i] = list(filter(("").__ne__, stacks[i]))

    return "Error"


def processStacks9000(stacks):
    file1 = open("input.txt", "r")
    lines = file1.readlines()

    for line in lines:
        if line == "\n" or line.split()[0] != "move":
            continue

        command = re.findall(r"\d+", line)
        command = [int(x) for x in command]

        for i in range(command[0]):
            stacks[command[2] - 1].append(stacks[command[1] - 1].pop())

    final = []

    for stack in stacks:
        final.append(stack.pop())

    return final


def processStacks9001(stacks):
    file1 = open("input.txt", "r")
    lines = file1.readlines()

    for line in lines:
        if line == "\n" or line.split()[0] != "move":
            continue

        command = re.findall(r"\d+", line)
        command = [int(x) for x in command]
        n = command[0]

        stacks[command[2] - 1] += stacks[command[1] - 1][-n:]
        stacks[command[1] - 1] = stacks[command[1] - 1][:-n]

    final = []

    for stack in stacks:
        final.append(stack.pop())

    return final


def main():
    stacks = getStacks()
    print("init stacks: \n", stacks)

    stacks1 = processStacks9000(copy.deepcopy(stacks))
    print("CrateMover 9000: ", "".join(stacks1))

    stacks2 = processStacks9001(copy.deepcopy(stacks))
    print("CrateMover 9001: ", "".join(stacks2))


if __name__ == "__main__":
    sys.exit(main())
