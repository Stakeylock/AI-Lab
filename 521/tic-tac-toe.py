def check_winner(b):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a, c, d in wins:
        if b[a] == b[c] == b[d] != " ":
            return b[a]
    return "Draw" if " " not in b else None


def minimax(b, max_turn):
    result = check_winner(b)
    if result == "X": return 1
    if result == "O": return -1
    if result == "Draw": return 0

    best = -float("inf") if max_turn else float("inf")
    player = "X" if max_turn else "O"

    for i in range(9):
        if b[i] == " ":
            b[i] = player
            score = minimax(b, not max_turn)
            b[i] = " "
            best = max(best, score) if max_turn else min(best, score)

    return best


def best_move(b):
    best, move = -float("inf"), None
    for i in range(9):
        if b[i] == " ":
            b[i] = "X"
            score = minimax(b, False)
            b[i] = " "
            if score > best:
                best, move = score, i
    return move


def print_board(b):
    for i in range(0, 9, 3):
        print(b[i], "|", b[i+1], "|", b[i+2])
    print()


def main():
    b = [" "] * 9
    
    while True:
        print_board(b)
        move = int(input("Enter your move (1-9): "))
        if b[move-1] != " ":
            print("Invalid move!")
            continue
        b[move-1] = "O"

        if check_winner(b): break

        b[best_move(b)] = "X"
        if check_winner(b): break

    print_board(b)
    print("AI wins!" if check_winner(b) == "X" else
          "You win!" if check_winner(b) == "O" else "Draw!")


if __name__ == "__main__":
    main()
