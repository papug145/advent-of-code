import functools
from collections import Counter, defaultdict


def findHandCategoryNoJokers(hand):
    counter = Counter(hand)
    values = list(counter.values())
    if 5 in values:
        return 7
    if 4 in values:
        return 6
    if 3 in values and 2 in values:
        return 5
    if 3 in values:
        return 4
    if values.count(2) == 2:
        return 3
    if 2 in values:
        return 2
    return 1


def findHandCategoryWithJokers(hand):
    numberOfJokers = list(hand).count('J')
    if numberOfJokers == 0:
        return findHandCategoryNoJokers(hand)
    if numberOfJokers == 5:
        return 7

    noJokes = hand.replace('J', '')
    mostFrequent = max(noJokes, key=noJokes.count)
    newHand = hand.replace('J', mostFrequent)
    category = findHandCategoryNoJokers(newHand)
    print(f'old hand: {hand}, new hand {newHand} category: {category}')
    return category


def comparatorNoJokers(hand1, hand2):
    cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    cards.reverse()
    cardsRank = {card: i for i, card in enumerate(cards)}
    for h1, h2 in zip(hand1[0], hand2[0]):
        if h1 == h2:
            continue
        if cardsRank[h1] > cardsRank[h2]:
            return 1
        else:
            return -1


def comparatorWithJokers(hand1, hand2):
    cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    cards.reverse()
    cardsRank = {card: i for i, card in enumerate(cards)}
    for h1, h2 in zip(hand1[0], hand2[0]):
        if h1 == h2:
            continue
        if cardsRank[h1] > cardsRank[h2]:
            return 1
        else:
            return -1


def solveAdvent13():
    handByCategory = defaultdict(list)
    totalWin = 0
    with open('input7.txt') as games:
        for game in games:
            hand, bid = game[:-1].split(' ')
            handCategory = findHandCategoryNoJokers(hand)
            handByCategory[handCategory].append((hand, bid))
        print(handByCategory)
        winningRate = 1
        for category in range(1, 8):
            hands = handByCategory.get(category)
            if hands:
                sortedHands = sorted(hands, key=functools.cmp_to_key(comparatorNoJokers))
                print(sortedHands)
                for h in sortedHands:
                    print(f'winning rate {winningRate} with bid {int(h[1])}')
                    totalWin += winningRate * int(h[1])
                    print(f'total win {totalWin}')
                    winningRate += 1


def solveAdvent14():
    handByCategory = defaultdict(list)
    totalWin = 0
    with open('input7.txt') as games:
        for game in games:
            hand, bid = game[:-1].split(' ')
            handCategory = findHandCategoryWithJokers(hand)
            handByCategory[handCategory].append((hand, bid))
        print(f'hands by category: {handByCategory}')
        winningRate = 1
        for category in range(1, 8):
            hands = handByCategory.get(category)
            if hands:
                sortedHands = sorted(hands, key=functools.cmp_to_key(comparatorWithJokers))
                print(f'sorted hands for category {category}: {sortedHands}')
                for h in sortedHands:
                    # print(f'winning rate {winningRate} with bid {int(h[1])}')
                    totalWin += winningRate * int(h[1])
                    print(f'total win {totalWin}')
                    winningRate += 1


if __name__ == '__main__':
    print(solveAdvent14())
