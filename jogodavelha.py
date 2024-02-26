def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def validate_input(prompt, valid_values):
    while True:
        value = input(prompt).upper()
        if value in valid_values:
            return value
        print("Entrada inválida. Por favor, tente novamente.")

def main():
    print("Bem-vindo ao Jogo da Velha!")
    print("Jogador 1, você vai jogar com 'X'. Jogador 2, você vai jogar com 'O'.")
    player_symbols = {'X', 'O'}
    player1_symbol = validate_input("Jogador 1, escolha 'X' ou 'O': ", player_symbols)
    player2_symbol = 'X' if player1_symbol == 'O' else 'O'
    print(f"Jogador 1 jogará com '{player1_symbol}' e Jogador 2 jogará com '{player2_symbol}'.")
    
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = [player1_symbol, player2_symbol]
    current_player = 0

    while True:
        print_board(board)
        print(f"Vez do Jogador {current_player + 1} ({players[current_player]})")
        row = int(input("Escolha a linha (0, 1, 2): "))
        col = int(input("Escolha a coluna (0, 1, 2): "))

        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Coordenadas fora do tabuleiro. Por favor, tente novamente.")
            continue

        if board[row][col] != " ":
            print("Essa posição já está ocupada. Tente novamente.")
            continue

        board[row][col] = players[current_player]
        
        if check_winner(board, players[current_player]):
            print_board(board)
            print(f"Parabéns! Jogador {current_player + 1} ({players[current_player]}) venceu!")
            break

        if all(all(cell != " " for cell in row) for row in board):
            print_board(board)
            print("Empate!")
            break

        current_player = (current_player + 1) % 2

if __name__ == "__main__":
    main()
