# input_file = open("Day 03/input_test.txt", "r")
input_file = open("Day 03/input.txt", "r")
from enum import Enum

class Submarine:
    def __init__(self):
        self.numbers = list()
    
    def addNumber(self, number):
        self.numbers.append(number)

    def OxigenGeneratorRating(self):
        copyOfNumbers = self.numbers.copy()
        iteration_max = len(copyOfNumbers[0])
        for iteration in range(iteration_max):
            one_countings = 0
            zero_countings = 0
            for number in copyOfNumbers:
                if number[iteration] == '1':
                    one_countings += 1
                else:
                    zero_countings += 1
            if one_countings >= zero_countings:
                copyOfNumbers = list(filter(lambda listElement: listElement[iteration] == '1', copyOfNumbers))
            else:
                copyOfNumbers = list(filter(lambda listElement: listElement[iteration] == '0', copyOfNumbers))
        return int(copyOfNumbers[0] , 2)

    def CO2ScrubberRating(self):
        copyOfNumbers = self.numbers.copy()
        iteration_max = len(copyOfNumbers[0])
        for iteration in range(iteration_max):
            one_countings = 0
            zero_countings = 0
            for number in copyOfNumbers:
                if number[iteration] == '1':
                    one_countings += 1
                else:
                    zero_countings += 1
            if one_countings < zero_countings:
                copyOfNumbers = list(filter(lambda listElement: listElement[iteration] == '1', copyOfNumbers))
            else:
                copyOfNumbers = list(filter(lambda listElement: listElement[iteration] == '0', copyOfNumbers))
            if len(copyOfNumbers) == 1:
                return int(copyOfNumbers[0] , 2)
        return int(copyOfNumbers[0] , 2)
    
    def getResult(self):
        return self.OxigenGeneratorRating() * self.CO2ScrubberRating()

class Reader:
    def __init__(self, input_file):
        self.input_file = input_file
        self.submarine = Submarine()

    def read(self):
        for line in self.input_file:
            self.submarine.addNumber(line.strip())
        return self.submarine.getResult()

reader = Reader(input_file)
print(reader.read())
