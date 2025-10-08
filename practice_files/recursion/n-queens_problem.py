# The N-Queens problem is a classic chess puzzle that asks how to place N queens
# on an NxN chessboard so that no two queens threaten each other.
# This is an advanced recursion problem that combines backtracking with recursive thinking.


# Explanation:
# This advanced exercise combines recursion with backtracking.
# The solve() function recursively tries to place queens column by column.
# If a placement is invalid, it backtracks and tries a different position.
# The is_safe() function checks if a queen can be placed on board[row][col] without conflicting with other queens.

def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check this row on left side
        for i in range(col):
            if board[row][i] == 1:
                return False
        
        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        
        # Check lower diagonal on left side
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        
        return True

    def solve(board, col):
        if col >= n:
            return True
        
        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 1
                if solve(board, col + 1):
                    return True
                board[i][col] = 0
        
        return False

    board = [[0 for _ in range(n)] for _ in range(n)]
    
    if solve(board, 0):
        return board
    else:
        return None

# Test the function
solution = solve_n_queens(8)
if solution:
    for row in solution:
        print(row)
else:
    print("No solution exists")
