def print_board(board):
   """print_board Prints the Tic Tac Toe board. 

   Args:
       board (_list_): Has the Tic Tac Toe board information.
   """
    print(''' --- --- --- ''')
    print(f'''| {board[0]} | {board[1]} | {board[2]} |''')
    print(''' --- --- --- ''')
    print(f'''| {board[3]} | {board[4]} | {board[5]} |''')
    print(''' --- --- --- ''')
    print(f'''| {board[6]} | {board[7]} | {board[8]} |''')
    print(''' --- --- --- ''')


def main():
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    print_board(board)


main()
