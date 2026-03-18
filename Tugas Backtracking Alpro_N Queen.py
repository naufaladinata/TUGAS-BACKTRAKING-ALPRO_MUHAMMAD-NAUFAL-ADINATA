import time

N = 4  

def print_board(board):
    for row in board:
        print(" ".join(row))
    print("\n" + "-"*10 + "\n")
    time.sleep(0.5)  # delay biar terlihat prosesnya


def is_safe(board, row, col):
    # cek kolom atas
    for i in range(row):
        if board[i][col] == "Q":
            return False

    # cek diagonal kiri atas
    i, j = row-1, col-1
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # cek diagonal kanan atas
    i, j = row-1, col+1
    while i >= 0 and j < N:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True


def solve_n_queen(board, row):
    # jika semua ratu sudah ditempatkan
    if row == N:
        print("Solusi ditemukan:\n")
        print_board(board)
        return True

    # coba tiap kolom
    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = "Q"
            print(f"Menempatkan Q di ({row},{col})")
            print_board(board)

            # rekursi ke baris berikutnya
            if solve_n_queen(board, row + 1):
                return True

            # backtracking
            board[row][col] = "."
            print(f"Backtracking dari ({row},{col})")
            print_board(board)

    return False


# inisialisasi papan
board = [["." for _ in range(N)] for _ in range(N)]

if not solve_n_queen(board, 0):
    print("Tidak ada solusi")