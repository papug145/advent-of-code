import re

FILE_NAME = 'inputs/input4.txt'
WINNING_NUMBERS_PATTERN = re.compile(r':(.*)\|')
MY_NUMBERS_PATTERN = re.compile(r'\|(.*)$')
NUMBER_PATTERN = re.compile(r'(\d+)')


def problem4_1():
    result = 0
    with open(FILE_NAME) as games:
        for index, game in enumerate(games, 1):
            winningNumbers = NUMBER_PATTERN.findall(WINNING_NUMBERS_PATTERN.search(game).group(1))
            myNumbers = NUMBER_PATTERN.findall(MY_NUMBERS_PATTERN.search(game).group(1))
            myWinningNumbers = set(winningNumbers).intersection(myNumbers)
            if len(myWinningNumbers) > 0:
                result += 2 ** (len(myWinningNumbers) - 1)
    return result


def problem4_2():
    cardsStack = {i: 1 for i in range(1, 215)}
    with open(FILE_NAME) as games:
        for index, game in enumerate(games, 1):
            winningNumbers = NUMBER_PATTERN.findall(WINNING_NUMBERS_PATTERN.search(game).group(1))
            myNumbers = NUMBER_PATTERN.findall(MY_NUMBERS_PATTERN.search(game).group(1))
            myWinningNumbers = set(winningNumbers).intersection(myNumbers)
            for i in range(1, len(myWinningNumbers) + 1):
                cardsStack[index + i] += 1 * cardsStack[index]
            print(cardsStack)
    return sum(cardsStack.values())


if __name__ == '__main__':
    print(problem4_1())
    print(problem4_2())
