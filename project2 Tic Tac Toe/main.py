from BoardGame import BoardGame
from Player import Player

board_game = BoardGame()
player_x = Player('X')
player_o = Player('O')

print(board_game)
board_game.modify_board(int(input(player_x.give_instructions())), player_x.piece)
print(board_game)
while board_game.declare_winner(player_x.piece) == '':
    board_game.modify_board(int(input(player_o.give_instructions())), player_o.piece)
    print(board_game)
    winner = board_game.declare_winner(player_o.piece)
    if winner != '':
        break
    board_game.modify_board(int(input(player_x.give_instructions())), player_x.piece)
    print(board_game)
    winner = board_game.declare_winner(player_x.piece)

if winner == 'tie':
    print("TIE!")
else:
    print(f"The winner is: {winner}")
