def solveNQueensBnB(n: int):
    res = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    
    col = set()
    posDiag = set()   # r + c
    negDiag = set()   # r - c

    def backtrack(r):
        if r == n:
            res.append([''.join(row) for row in board])
            return False   # Change to True for only one solution

        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue  # Pruning - Branch and Bound

            # Place queen
            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = 'Q'

            if backtrack(r + 1):
                return True

            # Backtrack
            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = '.'

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
    boards = solveNQueensBnB(4)
    printSolutions(boards)