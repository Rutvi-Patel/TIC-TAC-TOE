# ----------------------------------------------------------------------------------------
#   Player object contains different kind of players
#                
#   (c) 2020 Arjang Fahim
#
#   Date: 7/26/2020
#   email: fahim.arjang@csulb.edu
#   version: 1.0.0
# ----------------------------------------------------------------------------------------


import math
import random
import numpy as np


class Player():
    def __init__(self, board):
        self.board = board


class RandomComputerPlayer(Player):
    def __init__(self, board):
        super().__init__(board)

    def next_move(self):
        available_space = self.board.available_space()

        square = random.choice(available_space)
        self.board.board_data[square] = self.board.c_letter


class HumanPlayer(Player):
    def __init__(self, board):
        super().__init__(board)

    def next_move(self):
        print("Please enter your move ", end=" ")
        square = input()
        while self.board.board_data[int(square)-1] != 0:
            print("Please enter empty position ", end=" ")
            square = input()

        self.board.board_data[int(square) - 1] = self.board.h_letter


class SmartPlayer(Player):
    def __init__(self, board):
        super().__init__(board)

        # self.scores = []
        pass

    def next_move(self):
        # available_space = self.board.available_space()
        # self.available_moves()

        best = self.minimax(self.board.c_letter,len(self.board.available_space()), self.board.board_data)
        square = best[1]
        # print(square)
        self.board.board_data[square] = self.board.c_letter

    def is_winner(self, letter):
        if (
                (self.board.board_data[0] == letter and self.board.board_data[1] == letter and self.board.board_data[2] == letter) or
                (self.board.board_data[3] == letter and self.board.board_data[4] == letter and self.board.board_data[5] == letter) or
                (self.board.board_data[6] == letter and self.board.board_data[7] == letter and self.board.board_data[8] == letter) or
                (self.board.board_data[0] == letter and self.board.board_data[3] == letter and self.board.board_data[6] == letter) or
                (self.board.board_data[1] == letter and self.board.board_data[4] == letter and self.board.board_data[7] == letter) or
                (self.board.board_data[2] == letter and self.board.board_data[5] == letter and self.board.board_data[8] == letter) or
                (self.board.board_data[0] == letter and self.board.board_data[4] == letter and self.board.board_data[8] == letter) or
                (self.board.board_data[2] == letter and self.board.board_data[4] == letter and self.board.board_data[6] == letter)
        ):
            return True
        else:
            return False

    def available_moves(self):
        self.available_m =  self.board.available_space()
        return self.board.available_space()


    def evaluate(self):
        if self.is_winner(self.board.c_letter):
            score = +1
        elif self.is_winner(self.board.h_letter):
            score = -1
        else:
            score = 0

        return score


    def minimax(self, letter,depth, board):

        best = []
        next_letter = ""
        if letter == self.board.c_letter:
            next_letter = self.board.h_letter
            best = [- np.inf, -1]
        elif letter == self.board.h_letter:
            next_letter = self.board.c_letter
            best = [np.inf, -1]


        if (self.is_winner(next_letter) or (depth == 0)):
            score = (self.evaluate()) * (depth+1)
            # print(score)
            return [score, -1]


        for move in self.board.available_space():
            board[move] = letter
            my_score = self.minimax(next_letter, (depth-1), board)
            board[move] = 0
            my_score[1] = move

            if letter == self.board.c_letter:
                if my_score[0] > best[0]:
                    best = my_score
            else:
                if my_score[0] < best[0]:
                    best = my_score

        return best



