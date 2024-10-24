import math

# Tamaño del tablero
BOARD_SIZE = 4
MAX_DEPTH = 4  # Limitar la profundidad del algoritmo Minimax

# Representación de los jugadores
HUMAN = 'O'  # Aquí 'HUMAN' representa a la computadora cuando usa 'O'
COMPUTER = 'X'
EMPTY = ' '

# Inicializar el tablero
def create_board():
    return [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Imprimir el tablero
def print_board(board):
    for row in board:
        print("| " + " | ".join(row) + " |")
    print()

# Comprobar si hay un ganador
def check_winner(board, player):
    # Verificar filas y columnas
    for i in range(BOARD_SIZE):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(BOARD_SIZE)]):
            return True

    # Verificar diagonales
    if all([board[i][i] == player for i in range(BOARD_SIZE)]) or all([board[i][BOARD_SIZE - 1 - i] == player for i in range(BOARD_SIZE)]):
        return True

    return False

# Comprobar si el tablero está lleno (empate)
def is_full(board):
    return all([cell != EMPTY for row in board for cell in row])

# Minimax con poda alfa-beta
def minimax(board, depth, alpha, beta, maximizing_player, current_player):
    if check_winner(board, COMPUTER):
        return 10 - depth
    if check_winner(board, HUMAN):
        return depth - 10
    if is_full(board) or depth == MAX_DEPTH:
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board[i][j] == EMPTY:
                    board[i][j] = current_player
                    eval = minimax(board, depth + 1, alpha, beta, False, HUMAN if current_player == COMPUTER else COMPUTER)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board[i][j] == EMPTY:
                    board[i][j] = current_player
                    eval = minimax(board, depth + 1, alpha, beta, True, HUMAN if current_player == COMPUTER else COMPUTER)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Computadora hace una jugada
def computer_move(board, current_player):
    print(f"La computadora ({current_player}) está pensando...")
    best_score = -math.inf if current_player == COMPUTER else math.inf
    best_move = None
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == EMPTY:
                board[i][j] = current_player
                score = minimax(board, 0, -math.inf, math.inf, current_player == COMPUTER, HUMAN if current_player == COMPUTER else COMPUTER)
                board[i][j] = EMPTY
                print(f"Evaluando movimiento para {current_player} en ({i+1}, {j+1}): Puntuación {score}")
                
                if current_player == COMPUTER:
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
                else:
                    if score < best_score:
                        best_score = score
                        best_move = (i, j)

    if best_move:
        board[best_move[0]][best_move[1]] = current_player
        print(f"La computadora ({current_player}) juega en la posición: {best_move[0] + 1}, {best_move[1] + 1}")
    else:
        print(f"No se encontró un movimiento para la computadora ({current_player}).")

# Jugada del humano
def human_move(board, player):
    while True:
        move = input(f"Turno del jugador {player}. Ingresa tu movimiento (fila y columna 1-4 separados por espacio): ")
        try:
            row, col = map(int, move.split())
            row -= 1
            col -= 1
            if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE and board[row][col] == EMPTY:
                board[row][col] = player
                break
            else:
                print("Movimiento inválido. Intenta de nuevo.")
        except ValueError:
            print("Entrada inválida. Asegúrate de ingresar dos números separados por un espacio.")

# Lógica del juego principal
def play_game(mode):
    board = create_board()
    current_player = HUMAN

    while True:
        print_board(board)
        if check_winner(board, HUMAN):
            print("¡Gana el jugador O (Humano o Computadora)!")
            break
        if check_winner(board, COMPUTER):
            print("¡Gana el jugador X (Computadora)!")
            break
        if is_full(board):
            print("¡Empate!")
            break

        if mode == 1:  # Humano vs Humano
            human_move(board, current_player)
            current_player = COMPUTER if current_player == HUMAN else HUMAN
        elif mode == 2:  # Humano vs Computadora
            if current_player == HUMAN:
                human_move(board, HUMAN)
                current_player = COMPUTER
            else:
                computer_move(board, COMPUTER)
                current_player = HUMAN
        elif mode == 3:  # Computadora vs Computadora
            computer_move(board, current_player)
            current_player = COMPUTER if current_player == HUMAN else HUMAN

# Seleccionar el modo de juego
def main():
    print("Selecciona el modo de juego:")
    print("1. Humano vs Humano")
    print("2. Humano vs Computadora")
    print("3. Computadora vs Computadora")

    mode = int(input("Ingresa el número del modo de juego: "))
    play_game(mode)

if __name__ == "__main__":
    main()
