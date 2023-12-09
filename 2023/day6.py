FILE_TEST = 'inputs/input6-test.txt'
FILE_ADVENT = 'inputs/input6.txt'


def problem6_1():
    times, distances = open(FILE_ADVENT).read().split('\n')
    times = list(map(int, times.split(":")[1].split()))
    distances = list(map(int, distances.split(":")[1].split()))
    result = 1
    for time, recordDistance in zip(times, distances):
        count = 0
        for i in range(1, time):
            distance = i * (time - i)
            if distance > recordDistance:
                count += 1
        result *= count
    return result


def problem6_2():
    time, recordDistance = open(FILE_ADVENT).read().split('\n')
    time = int(time.split(':')[1].replace(' ', ''))
    recordDistance = int(recordDistance.split(":")[1].replace(' ', ''))
    for i in range(1, time):
        distance = i * (time - i)
        if recordDistance < distance:
            return (time - i) - i + 1


if __name__ == '__main__':
    print(problem6_1())
    print(problem6_2())
