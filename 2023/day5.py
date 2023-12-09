import re
from typing import List, Dict

FILE_NAME = 'inputs/input5.txt'
NUMBER_PATTERN = re.compile(r'(\d+)')


def sendMeLocation(seed: int, mappings: List[Dict[range, range]]):
    for mapping in mappings:
        for key in mapping.keys():
            if seed in key:
                value = mapping[key]
                valueStart = value.start
                keyStart = key.start
                seedPos = seed - keyStart
                temp = valueStart + seedPos
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

        for i in soilToFertilizerLines:
            destination, source, length = list(map(int, NUMBER_PATTERN.findall(lines[i - 1])))
            soilToFertilizer[range(source, source + length)] = range(destination, destination + length)

        for i in fertilizerToWaterLines:
            destination, source, length = list(map(int, NUMBER_PATTERN.findall(lines[i - 1])))
            fertilizerToWater[range(source, source + length)] = range(destination, destination + length)

        for i in waterToLightLines:
            destination, source, length = list(map(int, NUMBER_PATTERN.findall(lines[i - 1])))
            waterToLight[range(source, source + length)] = range(destination, destination + length)

        for i in lightToTempLines:
            destination, source, length = list(map(int, NUMBER_PATTERN.findall(lines[i - 1])))
            lightToTemp[range(source, source + length)] = range(destination, destination + length)

        for i in tempToHumidityLines:
            destination, source, length = list(map(int, NUMBER_PATTERN.findall(lines[i - 1])))
            tempToHumidity[range(source, source + length)] = range(destination, destination + length)

        for i in humidityToLocationLines:
            destination, source, length = list(map(int, NUMBER_PATTERN.findall(lines[i - 1])))
            humidityToLocation[range(source, source + length)] = range(destination, destination + length)

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
        return min(result)


def problem5_1():
    with open(FILE_NAME, 'r') as file:
        lines = file.readlines()
        seedsNumbers = [int(num) for num in NUMBER_PATTERN.findall(lines[0])]
        return findSeedMappings(seedsNumbers)


def problem5_2():
    pass


if __name__ == '__main__':
    print(problem5_1())
    print(problem5_2())
