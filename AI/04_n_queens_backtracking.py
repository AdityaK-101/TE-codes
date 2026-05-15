def solveNQueens(n: int):
    res = []
    board = [['.' for _ in range(n)] for _ in range(n)]

    def isSafe(row, col):
        # Check same column (above)
        for i in range(row):
            if board[i][col] == 'Q':
                return False
            
        # Check upper right diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        # Check upper left diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        return True

    def backtrack(row):
        if row == n:
            res.append([''.join(r) for r in board])
            return False  # Change to True if you want only one solution

        for col in range(n):
            if isSafe(row, col):
                board[row][col] = 'Q'
                if backtrack(row + 1):
                    return True
                board[row][col] = '.'  # backtrack
        return False

    backtrack(0)
    return res


def printSolutions(boards):
    if not boards:
        print("No solution found.")
        return
    for idx, board in enumerate(boards):
        print(f"Solution {idx + 1}:")
        for row in board:
            print(' '.join(row))
        print()


# Test
if __name__ == "__main__":
    boards = solveNQueens(4)
    printSolutions(boards)