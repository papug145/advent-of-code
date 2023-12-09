import re

INPUT_FILE = 'inputs/input1.txt'


def problem1_1():
    calibrationsSum = 0
    with open(INPUT_FILE) as calibrations:
        for calibration in calibrations:
            digits = ''.join(c for c in calibration if c.isdigit())
            calibrationsSum += int(digits[0] + digits[-1])
    return calibrationsSum


def getDigit(digit) -> str:
    if digit.isdigit():
        return digit
    else:
        return {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9'
        }[digit]


def problem1_2():
    calibrationSum = 0
    with open(INPUT_FILE) as calibrations:
        for calibration in calibrations:
            digitsExtracted = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', calibration)
            correctCalibration = int(getDigit(digitsExtracted[0]) + getDigit(digitsExtracted[-1]))
            calibrationSum += correctCalibration
    return calibrationSum


if __name__ == '__main__':
    print(problem1_1())
    print(problem1_2())
