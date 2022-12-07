import sys


def task1():
    file1 = open("input.txt", "r")
    # file1 = open("input.txt", "r")
    lines = file1.readlines()
    path = ["/"]
    fileSystem = {}
    index = 0

    while index < len(lines):
        parts = lines[index].split()

        print(f"==========")

        if parts[0] == "$":
            if parts[1] == "cd":
                if parts[2] == "/":
                    path = ["/"]
                    print(f"reset path: {path}")
                elif parts[2] == "..":
                    if len(path) > 1:
                        print(f"move up path: {path}")
                        path.pop()
                else:
                    path.append(parts[2])
                    print(f"down path: {path}")

            if parts[1] == "ls":
                index += 1
                nextLineParts = lines[index].split()

                while index < len(lines) and nextLineParts[0] != "$":
                    print("line: ", nextLineParts[:2])

                    if nextLineParts[0].isnumeric():
                        print("found file")
                        print(nextLineParts[0])
                        print(path)
                        print("path:", path)

                        for i in range(len(path)):

                            d = path[i] if i < 1 else "".join(path[: i + 1])
                            print("d: ", d)
                            print("i: ", i)
                            if d in fileSystem:
                                fileSystem[d] += int(nextLineParts[0])
                                print("in fileSystem", fileSystem)
                            else:
                                fileSystem[d] = int(nextLineParts[0])
                                print("else fileSystem", fileSystem)
                    else:
                        print("skipped dir ", nextLineParts[1])

                    print("fileSystem", fileSystem)
                    print(f"----------")

                    index += 1
                    if index < len(lines):
                        nextLineParts = lines[index].split()

                continue

            index += 1

    print(fileSystem)

    totalSize = 0
    for folderSize in fileSystem.values():
        if folderSize <= 100000:
            totalSize += int(folderSize)

    return totalSize


def task2():
    file1 = open("input.txt", "r")
    lines = file1.readlines()
    path = ["/"]
    fileSystem = {}
    index = 0

    while index < len(lines):
        parts = lines[index].split()

        if parts[0] == "$":
            if parts[1] == "cd":
                if parts[2] == "/":
                    path = ["/"]
                elif parts[2] == "..":
                    if len(path) > 1:
                        path.pop()
                else:
                    path.append(parts[2])

            if parts[1] == "ls":
                index += 1
                nextLineParts = lines[index].split()

                while index < len(lines) and nextLineParts[0] != "$":
                    if nextLineParts[0].isnumeric():
                        for i in range(len(path)):
                            d = path[i] if i < 1 else "".join(path[: i + 1])
                            if d in fileSystem:
                                fileSystem[d] += int(nextLineParts[0])
                            else:
                                fileSystem[d] = int(nextLineParts[0])
                    index += 1
                    if index < len(lines):
                        nextLineParts = lines[index].split()
                continue

            index += 1

    fileSystemSorted = dict(sorted(fileSystem.items(), key=lambda kv: kv[1]))
    fileSystemCurrentSize = fileSystem["/"]
    print(fileSystemCurrentSize)

    maxSize = 70000000
    requiredSpace = 30000000
    availableSize = maxSize - fileSystemCurrentSize
    print(availableSize)
    spaceToDelete = requiredSpace - availableSize
    print(spaceToDelete)

    for dir, size in fileSystemSorted.items():
        if size > spaceToDelete:
            return size

    return fileSystemSorted


def main():
    # print("task 1: ", task1())
    print("task 2: ", task2())


if __name__ == "__main__":
    sys.exit(main())
