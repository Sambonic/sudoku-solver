from sudoku.sudoku_board import SudokuBoard
from sudoku.backtracking_algo import *
from sudoku.genetic_algo import *
import copy 
import time
import psutil
# Initialize sudoku board
size = 9
complexity = 'Very high'
sudoku_board = SudokuBoard(size, complexity)
unsolved_board = copy.deepcopy(sudoku_board.board)
print("Generated Sudoku Puzzle:")
sudoku_board.print_sudoku()

# Solving the Puzzle using Backtracking Algorithm
solver = BacktrackingSolver()
sudoku_board.solved_board = solver.backtracking_algorithm(sudoku_board.board, size)

print("\nSolving Sudoku Puzzle:")

sudoku_board.print_sudoku(sudoku_board.solved_board)

print("\nNumber Of Iterations:", solver.get_iterations())
print(f"\nExecution time: {solver.get_elapsed():.4f} seconds")
print(f"\nExecution memory: {solver.get_memory()} MB")




# Solving using Genetic Algorithm
flattened_board = [item for row in unsolved_board for item in row]
flattened_board = ''.join(map(str, flattened_board))

flattened_target = [item for row in sudoku_board.solved_board for item in row]
flattened_target = ''.join(map(str, flattened_target))

population_size = 900
population = []
for _ in range(population_size):
    population.append(GeneticSolver(flattened_board,flattened_target,None))

print("\nSolving Sudoku Puzzle:")

population[0].genetic_algorithm(population,population_size)

print("\nNumber Of Iterations:", population[0].get_iterations())
print(f"\nExecution time: {population[0].elapsed_time:.4f} seconds")
print(f"\nExecution memory: {population[0].get_memory()} MB")