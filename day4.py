import re

FILE_NAME = 'input4.txt'
WINNING_NUMBERS_PATTERN = re.compile(r':(.*)\|')
MY_NUMBERS_PATTERN = re.compile(r'\|(.*)$')
NUMBER_PATTERN = re.compile(r'(\d+)')


def solveAdvent7():
    result = 0
    with open(FILE_NAME) as games:
        for index, game in enumerate(games, 1):
            winningNumbers = NUMBER_PATTERN.findall(WINNING_NUMBERS_PATTERN.search(game).group(1))
            print(f'Winning numbers for game {index} : {winningNumbers}')
            myNumbers = NUMBER_PATTERN.findall(MY_NUMBERS_PATTERN.search(game).group(1))
            print(f'My cards for game {index} : {myNumbers}')
            myWinningNumbers = set(winningNumbers).intersection(myNumbers)
            print(f'My winning numbers: {myWinningNumbers}')
            if len(myWinningNumbers) > 0:
                result += 2 ** (len(myWinningNumbers) - 1)
    return result


def solveAdvent8():
    cardsStack = {i: 1 for i in range(1, 215)}
    with open(FILE_NAME) as games:
        for index, game in enumerate(games, 1):
            winningNumbers = NUMBER_PATTERN.findall(WINNING_NUMBERS_PATTERN.search(game).group(1))
            print(f'Winning numbers for game {index} : {winningNumbers}')
            myNumbers = NUMBER_PATTERN.findall(MY_NUMBERS_PATTERN.search(game).group(1))
            print(f'My cards for game {index} : {myNumbers}')
            myWinningNumbers = set(winningNumbers).intersection(myNumbers)
            print(f'My winning numbers: {myWinningNumbers}')
            for i in range(1, len(myWinningNumbers)+1):
                cardsStack[index+i] += 1 * cardsStack[index]
            print(cardsStack)
    return sum(cardsStack.values())



if __name__ == '__main__':
    print(solveAdvent8())