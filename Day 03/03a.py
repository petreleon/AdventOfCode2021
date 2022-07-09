# input_file = open("Day 03/input_test.txt", "r")
input_file = open("Day 03/input.txt", "r")
from enum import Enum

class Submarine:
    def __init__(self):
        self.zeros = dict()
        self.ones = dict()
        self.commands = {
            '0': self.addZero,
            '1': self.addOne
        }

    def addZero(self, pozition):
        self.zeros[pozition] = self.zeros.get(pozition, 0) + 1

    def addOne(self, pozition):
        self.ones[pozition] = self.ones.get(pozition, 0) + 1

    def addStringNumber(self, string):
        for position in range(len(string)):
            self.commands[string[position]](position)
    
    def getZerosfromPosition(self, position):
        return self.zeros.get(position, 0)

    def getOnesfromPosition(self, position):
        return self.ones.get(position, 0)

    def getTotalFromPosition(self, position):
        return self.getZerosfromPosition(position) + self.getOnesfromPosition(position)

    def getGamma(self):
        number = 0
        index = 0
        while True:
            if self.getTotalFromPosition(index) == 0:
                return number
            number *= 2
            if self.getOnesfromPosition(index) > self.getZerosfromPosition(index):
                number += 1
            index += 1
            

    def getEpsilon(self):
        number = 0
        index = 0
        while True:
            if self.getTotalFromPosition(index) == 0:
                return number
            number *= 2
            if self.getZerosfromPosition(index) > self.getOnesfromPosition(index):
                number += 1
            index += 1

    def getResult(self):
        return self.getGamma() * self.getEpsilon()


submarine = Submarine()
for line in input_file:
    submarine.addStringNumber(line.strip())
print(submarine.getResult())
