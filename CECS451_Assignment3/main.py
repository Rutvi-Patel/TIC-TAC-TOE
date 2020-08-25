# import CECS451_Assignment3.Interface.Interface as inface


from CECS451_Assignment3.Board.Board import TerminalBoard
from pathlib import Path

def main():
    board_data = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    # board_data = ['X','O','X','X',0,'O',0,0,'O']
    board = TerminalBoard(board_data)

    board.play()

if __name__ == '__main__':
    main()