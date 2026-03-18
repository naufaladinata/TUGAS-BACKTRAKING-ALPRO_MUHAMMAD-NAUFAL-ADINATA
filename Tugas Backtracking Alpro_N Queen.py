import time

N = 4  

def print_board(board):
    for row in board:
        print(" ".join(row))
    print("\n" + "-"*10 + "\n")
    time.sleep(0.5)  


def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == "Q":
            return False


    i, j = row-1, col-1
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    i, j = row-1, col+1
    while i >= 0 and j < N:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True


def solve_n_queen(board, row):
    if row == N:
        print("Solusi ditemukan:\n")
        print_board(board)
        return True
        
    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = "Q"
            print(f"Menempatkan Q di ({row},{col})")
            print_board(board)

            if solve_n_queen(board, row + 1):
                return True

            board[row][col] = "."
            print(f"Backtracking dari ({row},{col})")
            print_board(board)

    return False


board = [["." for _ in range(N)] for _ in range(N)]

if not solve_n_queen(board, 0):
    print("Tidak ada solusi")
