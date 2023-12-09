import re
from typing import List, Dict

FILE_NAME = 'input5.txt'
NUMBER_PATTERN = re.compile(r'(\d+)')


def sendMeLocation(seed: int, mappings: List[Dict[range, range]]):
    for mapping in mappings:
        for key in mapping.keys():
            if seed in key:
                value = mapping[key]
                #print(f'seed {seed} in range {key} mapped to {value}')
                valueStart = value.start
                keyStart = key.start
                seedPos = seed - keyStart
                temp = valueStart + seedPos
                #print(f'key start at {keyStart}, value start at {valueStart}, seed in position: {seedPos} mapping to {temp}')
                seed = temp
                break
    return seed


def findSeedMappings(seedNumbers):
    seedToSoil = {}
    seedToSoilLines = range(4, 7)
    soilToFertilizer = {}
    soilToFertilizerLines = range(9, 38)
    fertilizerToWater = {}
    fertilizerToWaterLines = range(40, 83)
    waterToLight = {}
    waterToLightLines = range(85, 126)
    lightToTemp = {}
    lightToTempLines = range(128, 159)
    tempToHumidity = {}
    tempToHumidityLines = range(161, 208)
    humidityToLocation = {}
    humidityToLocationLines = range(210, 251)
    with open(FILE_NAME, 'r') as file:
        lines = file.readlines()

        for i in seedToSoilLines:
            destination, source, length = list(map(int, NUMBER_PATTERN.findall(lines[i - 1])))
            seedToSoil[range(source, source + length)] = range(destination, destination + length)
        print(seedToSoil)

        for i in soilToFertilizerLines:
            destination, source, length = list(map(int, NUMBER_PATTERN.findall(lines[i - 1])))
            soilToFertilizer[range(source, source + length)] = range(destination, destination + length)
        print(soilToFertilizer)

        for i in fertilizerToWaterLines:
            destination, source, length = list(map(int, NUMBER_PATTERN.findall(lines[i - 1])))
            fertilizerToWater[range(source, source + length)] = range(destination, destination + length)
        print(fertilizerToWater)

        for i in waterToLightLines:
            destination, source, length = list(map(int, NUMBER_PATTERN.findall(lines[i - 1])))
            waterToLight[range(source, source + length)] = range(destination, destination + length)
        print(waterToLight)

        for i in lightToTempLines:
            destination, source, length = list(map(int, NUMBER_PATTERN.findall(lines[i - 1])))
            lightToTemp[range(source, source + length)] = range(destination, destination + length)
        print(lightToTemp)

        for i in tempToHumidityLines:
            destination, source, length = list(map(int, NUMBER_PATTERN.findall(lines[i - 1])))
            tempToHumidity[range(source, source + length)] = range(destination, destination + length)
        print(tempToHumidity)

        for i in humidityToLocationLines:
            destination, source, length = list(map(int, NUMBER_PATTERN.findall(lines[i - 1])))
            humidityToLocation[range(source, source + length)] = range(destination, destination + length)
        print(humidityToLocation)

        result = set()
        for seed in seedNumbers:
            result.add(sendMeLocation(seed, [
                seedToSoil,
                soilToFertilizer,
                fertilizerToWater,
                waterToLight,
                lightToTemp,
                tempToHumidity,
                humidityToLocation
            ]))
        #print(f'Result set: {result} with min: {min(result)}')
        return min(result)


def solveAdvent9():
    with open(FILE_NAME, 'r') as file:
        lines = file.readlines()
        seedsNumbers = [int(num) for num in NUMBER_PATTERN.findall(lines[0])]
        print(seedsNumbers)
        return findSeedMappings(seedsNumbers)

def solveAdvent10() :
    seeds, *mappings = open('input5-test.txt').read().split('\n\n')
    seeds = list(map(int, seeds.split(':')[1].split()))
    seeds = [(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, len(seeds), 2)]
    print(seeds)
    mappings = [mapping.split(':\n')[1].split('\n') for mapping in mappings]
    print(mappings)

    for mapping in mappings:
        print(mapping)
        new = []
        for interval in mapping:
            dest, sourceStart, length = interval.split()
            sourceEnd = sourceStart + length


if __name__ == '__main__':
    print(solveAdvent10())
