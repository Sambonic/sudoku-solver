from backtracking_algo import *
import random
import copy

class SudokuBoard:
    def __init__(self, size, complexity):
        self.iterations = 0
        self.board = None
        self.solved_board = None
        self.generate_sudoku(size, complexity)

    def generate_sudoku(self, size, complexity):

        complexity_values = {
            "Low": 0.2,
            "Medium": 0.5,
            "High": 0.7,
            "Very high": 0.9,
        }

        #Create the empty self.board
        self.board = [[0 for _ in range(size)] for _ in range(size)]

        #Solve the Sudoku completely
        solver = BacktrackingSolver()
        self.solved_board  = solver.backtracking_algorithm(copy.deepcopy(self.board), size)
        self.board = copy.deepcopy(self.solved_board)

        #Calculate cells to remove based on complexity
        cells_to_remove = int(size**2 * (complexity_values[complexity]))

        #Remove cells while maintaining solvability

        for _ in range(cells_to_remove):
            while True:

                row = random.randint(0, size - 1)
                col = random.randint(0, size - 1 )

                #Remove non-zero cells
                if self.board [row][col] != 0:  
                    self.board [row][col] = 0
                    break

        return self.board

    def print_sudoku(self, board=None):
        for row in self.board:
            print(" ".join(map(str, row)))

