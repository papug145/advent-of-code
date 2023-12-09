FILE_TEST = 'input6-test.txt'
FILE_ADVENT = 'input6.txt'


def solveAdvent11():
    times, distances = open(FILE_ADVENT).read().split('\n')
    times = list(map(int, times.split(":")[1].split()))
    print(times)
    distances = list(map(int, distances.split(":")[1].split()))
    print(distances)
    result = 1
    for time, recordDistance in zip(times, distances):
        count = 0
        for i in range(1, time):
            distance = i * (time-i)
            if distance > recordDistance:
                count += 1
        result *= count
    return result


def solveAdvent12():
    time, recordDistance = open(FILE_ADVENT).read().split('\n')
    time = int(time.split(':')[1].replace(' ', ''))
    print(time)
    recordDistance = int(recordDistance.split(":")[1].replace(' ', ''))
    print(recordDistance)
    for i in range(1, time):
        distance = i * (time - i)
        if recordDistance < distance:
            return (time-i) - i + 1


if __name__ == '__main__':
    print(solveAdvent12())