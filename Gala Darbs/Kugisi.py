import random

def create_board(size):
    return [["O"] * size for _ in range(size)]

def print_board(board):
    for row in board:
        print(" ".join(row))

def random_row(board):
    return random.randint(0, len(board) - 1)

def random_col(board):
    return random.randint(0, len(board[0]) - 1)

def place_ships(board, num_ships):
    ships = []
    for _ in range(num_ships):
        ship_row, ship_col = random_row(board), random_col(board)
        while (ship_row, ship_col) in ships:
            ship_row, ship_col = random_row(board), random_col(board)
        ships.append((ship_row, ship_col))
    return ships

def get_player_input():
    while True:
        try:
            row = int(input("Ievadiet rindu: "))
            col = int(input("Ievadiet kolonu: "))
            return row, col
        except ValueError:
            print("Lūdzu ievadiet derīgus skaitļus.")

def play_game(board_size=5, num_ships=3, max_turns=10):
    board = create_board(board_size)
    ships = place_ships(board, num_ships)
    print("Laipni lūdzam spēlē 'Kuģīši'!")

    turns = 0
    while turns < max_turns:
        print(f"\nTurn {turns + 1} of {max_turns}")
        print_board(board)
        guess_row, guess_col = get_player_input()

        if (guess_row, guess_col) in ships:
            print("Trāpījums!")
            board[guess_row][guess_col] = "X"
            ships.remove((guess_row, guess_col))
            if not ships:
                print("Apsveicu! Jūs esat nogremdējis visus kuģus!")
                break
        else:
            if (0 <= guess_row < board_size) and (0 <= guess_col < board_size):
                if board[guess_row][guess_col] == "O":
                    print("Garām!")
                    board[guess_row][guess_col] = "-"
                else:
                    print("Jūs jau esat šeit mēģinājis!")
            else:
                print("Šis šāviens ir ārpus spēles laukuma.")

        turns += 1

    if ships:
        print("\nJūs izsmēlāt visus mēģinājumus. Spēle beigusies.")
        print("Kuģu atrašanās vietas bija:")
        for ship_row, ship_col in ships:
            board[ship_row][ship_col] = "S"
        print_board(board)

if __name__ == "__main__":
    play_game()
