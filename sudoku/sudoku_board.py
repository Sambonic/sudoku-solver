from .backtracking_algo import *
import random
import copy

class SudokuBoard:
    def __init__(self, size, complexity):
        self.board = None
        self.solved_board = None
        self.generate_sudoku(size, complexity)

    def flip(self):
        flip_type = random.choice(["horizontal", "vertical","diagonal"])
        if flip_type == "vertical":
            # Reverse the entire board for horizontal flip
            self.solved_board.reverse()  
        elif flip_type == "horizontal":
            # Reverse each row for vertical flip
            for row in self.solved_board:
                row.reverse() 
        elif flip_type == "diagonal":
            size = len(self.solved_board)
            new_board = [[0 for _ in range(size)] for _ in range(size)]  # Create a new board

            for i in range(size):
                for j in range(size):
                    # New row index based on the flipped position
                    new_row = size - 1 - i
                    new_board[new_row][j] = self.solved_board[i][j]

            # Update the solved_board with the flipped values
            self.solved_board = new_board

    def shuffle_sudoku(self,size):
        # Shuffles a solved Sudoku board by swapping groups of rows and columns
        group_num = int(size**(0.5))

        # Randomly swap groups of rows eg. 9x9 puzzle with have 3 rows swapped with another 3 rows
        for _ in range(5):  # Swap a few times
            group1_index = random.randint(0, group_num - 1)
            group2_index = random.randint(0, group_num - 1)
            if group1_index != group2_index:
                start_row1 = group1_index * group_num
                start_row2 = group2_index * group_num
                self.flip()
                for i in range(group_num):
                    self.solved_board[start_row1 + i], self.solved_board[start_row2 + i] = self.solved_board[start_row2 + i], self.solved_board[start_row1 + i]
                    

        # Randomly swap groups of rows eg. 9x9 puzzle with have 3 cols swapped with another 3 cols
        for _ in range(5):
            group1_index = random.randint(0, group_num - 1)
            group2_index = random.randint(0, group_num - 1)
            if group1_index != group2_index:
                start_col1 = group1_index * group_num
                start_col2 = group2_index * group_num
                self.flip()
                for i in range(group_num):
                    self.solved_board[i][start_col1], self.solved_board[i][start_col2] = self.solved_board[i][start_col2], self.solved_board[i][start_col1]
     


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
        self.shuffle_sudoku(size)
        self.board = copy.deepcopy(self.solved_board)

        #Calculate cells to remove based on complexity
        cells_to_remove = int(size**2 * (complexity_values[complexity]))

        #Remove cells while maintaining solvability
        for _ in range(cells_to_remove):
            while True:

                row = random.randint(0, size - 1)
                col = random.randint(0, size - 1 )

                #Remove non-zero cells
                if self.board[row][col] != 0:  
                    self.board[row][col] = 0
                    break

        return self.board

    def print_sudoku(self, board=None):
        for row in self.board:
            print(" ".join(map(str, row)))

