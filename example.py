from sudoku.sudoku_board import SudokuBoard
from sudoku.backtracking_algo import *
from sudoku.genetic_algo import *
import copy 
import time

# Initialize sudoku board
size = 9
complexity = 'Medium'
sudoku_board = SudokuBoard(size, complexity)
unsolved_board = copy.deepcopy(sudoku_board.board)
print("Generated Sudoku Puzzle:")
sudoku_board.print_sudoku()

# Solving the Puzzle using Backtracking Algorithm
solver = BacktrackingSolver()

backtracking_start = time.time()
sudoku_board.solved_board = solver.backtracking_algorithm(sudoku_board.board, size)
backtracking_end = time.time()
elapsed_time = backtracking_end - backtracking_start

sudoku_board.iterations = solver.get_iterations()
print("\nSolving Sudoku Puzzle:")
sudoku_board.print_sudoku(sudoku_board.solved_board)
print("\nNumber Of Iterations:", sudoku_board.iterations)
print(f"\nExecution time: {elapsed_time:.4f} seconds")




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
genetic_start = time.time()
population[0].genetic_algorithm(population,population_size)
genetic_end = time.time()
elapsed_time = genetic_end - genetic_start

print("\nNumber Of Iterations:", population[0].get_iterations())
print(f"\nExecution time: {elapsed_time:.4f} seconds")