input_file = open("Day 02/input.txt", "r")
from enum import Enum

class Submarine:
    def __init__(self):
        self.horizontal_position = 0
        self.deepth = 0
        self.aim = 0
        self.commands = {
            "forward": self.move_foward,
            "down": self.move_down,
            "up": self.move_up
        }

    def move_foward(self, distance):
        self.horizontal_position += distance
        self.deepth += distance * self.aim

    def move_down(self, distance):
        self.aim += distance
    
    def move_up(self, distance):
        self.aim -= distance

    def execute_command(self, command, distance):
        self.commands[command](distance)
    
    def get_position(self):
        class Result(Enum):
            horizontal = self.horizontal_position
            deepth = self.deepth
        return Result


submarine = Submarine()

for line in input_file.readlines():
    command, distance = line.strip().split(" ")
    submarine.execute_command(command, int(distance))

position = submarine.get_position()

print(position.horizontal.value * position.deepth.value)
