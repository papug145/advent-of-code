from collections import defaultdict


def problem9_1():
    lines = [[int(elem) for elem in line.split()] for line in open('inputs/input9.txt').read().splitlines()]
    levels = defaultdict(list)
    results = list()
    for index, line in enumerate(lines):
        currentLevel = line
        levels[index].append(currentLevel)
        while not all(e == 0 for e in currentLevel):
            newLevel = list()
            for i in range(1, len(currentLevel)):
                diff = currentLevel[i] - currentLevel[i - 1]
                newLevel.append(diff)
            levels[index].append(newLevel)
            currentLevel = newLevel

        level = levels[index]
        for i in range(len(level) - 1, 0, -1):
            lastElemBelow = level[i][-1]
            lastElemAbove = level[i - 1][-1]
            newElem = lastElemBelow + lastElemAbove
            level[i - 1].append(newElem)
        results.append(level[0][-1])
    return sum(results)


def problem9_2():
    lines = [[int(elem) for elem in line.split()] for line in open('inputs/input9.txt').read().splitlines()]
    levels = defaultdict(list)
    results = list()
    for index, line in enumerate(lines):
        currentLevel = line
        levels[index].append(currentLevel)
        while not all(e == 0 for e in currentLevel):
            newLevel = list()
            for i in range(1, len(currentLevel)):
                diff = currentLevel[i] - currentLevel[i - 1]
                newLevel.append(diff)
            levels[index].append(newLevel)
            currentLevel = newLevel

        level = levels[index]
        for i in range(len(level) - 1, 0, -1):
            firstElemBelow = level[i][0]
            firstElemAbove = level[i - 1][0]
            newElem = firstElemAbove - firstElemBelow
            level[i - 1] = [newElem]
        results.append(level[0][0])
    return sum(results)


if __name__ == '__main__':
    print(problem9_1())
    print(problem9_2())
