import itertools

# input_file = open("Day 04/input_test.txt", "r")
input_file = open("Day 04/input.txt", "r")

class Bingo:
    def __init__(self, choices, boards):
        self.choices = choices
        self.boards = boards
        self.choisedOnBoards = dict()
    
    def verify(self, board, line, column):
        line_complete = True
        for column_index in range(5):
            if not self.choisedOnBoards.get((board, line, column_index), False):
                line_complete = False
                break
        collumn_complete = True
        for line_index in range(5):
            if not self.choisedOnBoards.get((board, line_index, column), False):
                collumn_complete = False
                break
        if line_complete or collumn_complete:
            return True
        return False

    def addChoice(self, board, line, column):
        self.choisedOnBoards[(board, line, column)] = True
        return self.verify(board, line, column)

    def sumOfUnmarked(self, board_index):
        sum_of_unmarked = 0
        for line_index in range(5):
            for column_index in range(5):
                if not self.choisedOnBoards.get((board_index, line_index, column_index), False):
                    sum_of_unmarked += self.boards[board_index][line_index][column_index]
        return sum_of_unmarked

    def getResult(self):
        list_of_won_boards = []
        for choice in self.choices:
            for board_index in range(len(self.boards)):
                if board_index not in list_of_won_boards:
                    for line_index in range(5):
                        for column_index in range(5):
                            if self.boards[board_index][line_index][column_index] == choice:
                                if self.addChoice(board_index, line_index, column_index):
                                    list_of_won_boards.append(board_index)
                                    if len(list_of_won_boards) == len(self.boards):
                                        return self.sumOfUnmarked(board_index) * choice

class Reader:
    def __init__(self, input_file):
        self.input_file = input_file
        self.bingo = self.read()
    
    def read(self):
        choices = [int(choice) for choice in self.input_file.readline().strip().split(',')]
        boards = []
        board = []
        self.input_file.readline()
        for line in self.input_file.readlines():
            if line == '\n':
                boards.append(board)
                board = []
            else:
                board.append([int(boardElement) for boardElement in line.strip().split()])
        boards.append(board)
        return Bingo(choices, boards)
        
reader = Reader(input_file)
print(reader.bingo.getResult())
