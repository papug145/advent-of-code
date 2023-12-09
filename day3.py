import re

FILE_NAME = 'input3.txt'
SPECIAL_CHAR_PATTERN = re.compile(r'[^0-9.]')
GEAR_PATTERN = re.compile(r'\*')
NUMBER_PATTERN = re.compile(r'\d+')


def solveAdvent5():
    overallSum = 0
    matrix = []
    specialCharsPositions = [[] for _ in range(142)]
    specialCharsPositions[0] = []
    specialCharsPositions[141] = []
    with open(FILE_NAME) as engineSchematic:
        for index, engineLine in enumerate(engineSchematic, 1):
            # remove new line character at the end of each line
            engineLine = engineLine[:-1]
            matrix.append(engineLine)
            specialChars = SPECIAL_CHAR_PATTERN.finditer(engineLine)
            for specialChar in specialChars:
                startIndex = specialChar.start()
                endIndex = specialChar.end()
                for i in range(startIndex, endIndex):
                    specialCharsPositions[index].append(i)

    for index, line in enumerate(matrix, 1):
        numbers = NUMBER_PATTERN.finditer(line)
        for number in numbers:
            startIndex = number.start()
            endIndex = number.end()
            value = number.group()
            print(line)
            print(specialCharsPositions[index - 1])
            print(specialCharsPositions[index])
            print(specialCharsPositions[index + 1])
            print(f'Checking: {value} in line {index} and position from {startIndex} to {endIndex}...')
            if hasAdjacentSymbols(specialCharsPositions, index, startIndex, endIndex):
                print('Confirmed engine part')
                overallSum += int(value)
            else:
                print('Not part of engine!')
    return overallSum


def hasAdjacentSymbols(specialCharsPositions, lineNumber, x, y):
    for i in range(x - 1, y + 1):
        if i in specialCharsPositions[lineNumber] \
                or i in specialCharsPositions[lineNumber - 1] \
                or i in specialCharsPositions[lineNumber + 1]:
            return True
    return False


def solveAdvent6():
    finalResult = 0
    engineLines = ['.' * 140]
    gearPositions = [[] for _ in range(140)]
    with open(FILE_NAME) as engineSchematic:
        for index, engineLine in enumerate(engineSchematic):
            engineLine = engineLine[:-1]
            engineLines.append(engineLine)
            gears = GEAR_PATTERN.finditer(engineLine)
            for gear in gears:
                startIndex = gear.start()
                endIndex = gear.end()
                for i in range(startIndex, endIndex):
                    gearPositions[index].append(i)
        engineLines.append('.' * 140)

    for index, gearPosition in enumerate(gearPositions, 1):
        print(f'positions for {index}: {gearPosition}')
        for g in gearPosition:
            validNumbers = []
            startSearching = g - 3 if g - 3 >= 0 else 0
            endSearching = g + 4 if g + 3 < 140 else 140
            lineAbove = engineLines[index - 1][startSearching:endSearching]
            lineWithGear = engineLines[index][startSearching:endSearching]
            lineBelow = engineLines[index + 1][startSearching:endSearching]
            print(f'fragment above {g}: {lineAbove}')
            print(f'fragment with {g}:  {lineWithGear}')
            print(f'fragment below {g}: {lineBelow}')
            numbersAbove = NUMBER_PATTERN.finditer(lineAbove)
            for numAbove in numbersAbove:
                if startSearching + numAbove.start() > g+1 or startSearching + numAbove.end() < g:
                    print(f'Num above invalid!: {numAbove.group()}')
                    continue
                else:
                    validNumbers.append(int(numAbove.group()))
                    print(f'Num above valid!: {numAbove.group()}')
            numbersInLine = NUMBER_PATTERN.finditer(lineWithGear)
            for numInLine in numbersInLine:
                if startSearching + numInLine.start() > g+1 or startSearching + numInLine.end() < g:
                    print(f'Num in line invalid!: {numInLine.group()}')
                    continue
                else:
                    validNumbers.append(int(numInLine.group()))
                    print(f'Num in line valid!: {numInLine.group()}')
            numbersBelow = NUMBER_PATTERN.finditer(lineBelow)
            for numBelow in numbersBelow:
                if startSearching + numBelow.start() > g+1 or startSearching + numBelow.end() < g:
                    print(f'Num below invalid!: {numBelow.group()}')
                    continue
                else:
                    validNumbers.append(int(numBelow.group()))
                    print(f'Num below valid!: {numBelow.group()}')
            if len(validNumbers) == 2:
                ratio = validNumbers[0] * validNumbers[1]
                print(f'Adding gear ratio for {validNumbers[0]} and {validNumbers[1]} equal to {ratio}')
                finalResult += ratio
    return finalResult



if __name__ == '__main__':
    print(solveAdvent6())
