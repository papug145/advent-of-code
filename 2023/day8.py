import collections
import math
import re


def problem8_1():
    instructions, dessertMap = open('inputs/input8.txt').read().split('\n\n')
    dessertMap = dessertMap.split('\n')
    instructions = collections.deque(instructions)
    newMappings = {}
    for mapping in dessertMap:
        source, dest = mapping.split(' = ')
        dest = re.findall(r'[A-Z]{3}', dest)
        newMappings[source] = dest

    currentPos = 'AAA'
    numberOfSteps = 0
    while currentPos != 'ZZZ':
        curr = newMappings[currentPos]
        currInstruction = instructions.popleft()
        currentPos = curr[0] if currInstruction == 'L' else curr[1]
        instructions.append(currInstruction)
        numberOfSteps += 1
    return numberOfSteps


def problem8_2():
    instructions, _, *dessertMap = open('inputs/input8.txt').read().splitlines()
    mappings = {}
    for line in dessertMap:
        source, target = line.split(' = ')
        mappings[source] = target[1:-1].split(', ')
    startingPositions = [key for key in mappings if key.endswith('A')]
    numberOfSteps = []
    for position in startingPositions:
        currSteps = 0
        while not position.endswith('Z'):
            currSteps += 1
            position = mappings[position][0 if instructions[0] == 'L' else 1]
            instructions = instructions[1:] + instructions[0]
        numberOfSteps.append(currSteps)
    return math.lcm(*numberOfSteps)


if __name__ == '__main__':
    print(problem8_1())
    print(problem8_2())
