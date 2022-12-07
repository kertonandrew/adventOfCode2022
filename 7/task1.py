import sys


def task():
    file1 = open("input.txt", "r")
    lines = file1.readlines()
    path = ["/"]
    fileSystem = {}
    index = 0

    while index < len(lines):
        print("start index: ", index)

        parts = lines[index].split()

        if parts[0] == "$":
            if parts[1] == "cd":
                if parts[2] == "/":
                    path = ["/"]
                    # print(f"reset path: {path}")
                elif parts[2] == "..":
                    if len(path) > 1:
                        # print(f"move up path: {path}")
                        path.pop()
                else:
                    path.append(parts[2])
                    # print(f"down path: {path}")

            if parts[1] == "ls":
                index += 1
                nextLineParts = lines[index].split()

                while index < len(lines) and nextLineParts[0] != "$":
                    nextLineParts = lines[index].split()

                    if nextLineParts[0].isnumeric():
                        print("found file")
                        if path[len(path) - 1] in fileSystem:
                            fileSystem[path[len(path) - 1]] += nextLineParts[0]
                        else:
                            fileSystem[path[len(path) - 1]] = nextLineParts[0]

                    index += 1
                    print(index)

                continue

            print("end index: ", index)
            index += 1

    return fileSystem


def main():
    print("task 1: ", task())


if __name__ == "__main__":
    sys.exit(main())
