from sudoku.sudoku_board import SudokuBoard
from sudoku.backtracking_algo import *
from sudoku.genetic_algo import *

import copy 

# Initialize sudoku board
size = 9
complexity = 'Medium'
sudoku_board = SudokuBoard(size, complexity)
unsolved_board = copy.deepcopy(sudoku_board.board)
print("Generated Sudoku Puzzle:")
sudoku_board.print_sudoku()

# Solving the Puzzle using Backtracking Algorithm
solver = BacktrackingSolver()
sudoku_board.solved_board = solver.backtracking_algorithm(sudoku_board.board, size)
sudoku_board.iterations = solver.get_iterations()
print("\nSolving Sudoku Puzzle:")
sudoku_board.print_sudoku(sudoku_board.solved_board)
print("\nNumber Of Iterations:", sudoku_board.iterations)



# Solving using Genetic Algorithm
flattened_board = [item for row in unsolved_board for item in row]
flattened_board = ''.join(map(str, flattened_board))
print(flattened_board)
flattened_target = [item for row in sudoku_board.solved_board for item in row]
flattened_target = ''.join(map(str, flattened_target))
print(flattened_target)

population_size = 900
population = []

# create initial population
for _ in range(population_size):
    population.append(GeneticSolver(flattened_board,flattened_target,None))

population[0].genetic_algorithm(population,population_size)