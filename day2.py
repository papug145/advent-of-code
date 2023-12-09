import re
from collections import defaultdict

FILE_NAME = 'input2.txt'
gamePattern = re.compile(r'\b(\d+)\s+([a-zA-Z]+)\b')


def part1():
    allowedValues = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    idsSum = 0
    with open(FILE_NAME) as games:
        for gameNumber, game in enumerate(games, 1):
            print(f'Game number: {gameNumber}')
            gameResults = gamePattern.findall(game)
            print(gameResults)
            for gameResult in gameResults:
                number, color = gameResult
                if allowedValues[color] < int(number):
                    print(f'Impossible result {number} {color}')
                    idsSum += gameNumber
                    break
    return sum(range(1, 101)) - idsSum


def part2():
    finalResult = 0
    with open(FILE_NAME) as games:
        for game in games:
            gameResults = gamePattern.findall(game)
            print(gameResults)
            helper = defaultdict(list)
            for number, color in gameResults:
                helper[color].append(int(number))
            print(helper)
            power = 1
            for res in helper.values():
                power *= max(res)
            print(f'Power {power}')
            finalResult += power
    return finalResult





if __name__ == '__main__':
    print(part2())

