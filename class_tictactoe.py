# -*- coding: utf-8 -*-
"""Class tictactoe.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RKEi5Q8EvaZBjbLFRhI7sFVqZ4RYHQFT
"""

import random
import os


class Board():
    def __init__(self):
        self.board = [str(x) for x in range(1, 10)]
        self.nums = [str(x) for x in range(1, 10)]

    def display_board(self):
        print(f'''\t    +--------------------------------+
        |          |          |          |
        |     {self.board[0]}    |     {self.board[1]}    |     {self.board[2]}    | 
        |          |          |          |
        ==================================
        |          |          |          |
        |     {self.board[3]}    |     {self.board[4]}    |     {self.board[5]}    | 
        |          |          |          |
        ==================================
        |          |          |          |
        |     {self.board[6]}    |     {self.board[7]}    |     {self.board[8]}    | 
        |          |          |          |
        +--------------------------------+''')

    def is_valid_move(self, move):
        self.move = move
        if move.isdigit() and len(move) == 1:
            if self.move in self.nums:
                return True
            return False
        return False

    def free_moves(self):
        if len(self.nums) > 0:
            return True
        else:
            return False

    def change_board(self, move, position):
        if self.is_valid_move(move) and self.free_moves():
            self.board[int(move) - 1] = position
            self.nums.remove(move)
            return self.board
        return None

    def wincheck(self, player):
        winlist = [[0, 1, 2],
                   [3, 4, 5],
                   [6, 7, 8],
                   [0, 3, 6],
                   [1, 4, 7],
                   [2, 5, 8],
                   [0, 4, 8],
                   [2, 4, 6]]
        for a, b, c in winlist:
            if self.board[a] == self.board[b] == self.board[c] == player.position:
                return True
        return False


class Player():
    def __init__(self, position):
        self.position = position

    def __str__(self):
        return f"Player {self.position}"


class Game():
    def __init__(self):
        self.player1 = Player('\033[35mX\033[0m')
        self.player2 = Player('\033[2;34;5mO\033[0m')
        self.board = Board()

    def print_board(self):
        self.board.display_board()

    def change_turn(self, player):
        if player is self.player1:
            return self.player2
        else:
            return self.player1

    def won_game(self, player):
        return self.board.wincheck(player)

    def update_board(self, move, position):
        if self.board.change_board(move, position) is not None:
            return self.board.change_board(move, position)
        else:
            move = input("\033[2;31;1mWrong move, try again :\033[0m")
            return self.board.change_board(move, position)


def start():
    print(""" \033[1;35;2m
                          *****************************************
                          **    Welcome To Tic Tac Toe Game !    **
                          *****************************************\033[0m""")
    game = Game()
    player = game.player1
    num = [str(x) for x in range(1,10)]
    while len(num) > 0:
        game.print_board()
        move = input(f'{player} put your move = ')
        game.update_board(move, player.position)
        num.remove(move)
        game.print_board()
        if game.won_game(player):
            print('\033[2;34;1m', player, '\033[2;34;1mis the Winner!\033[0m')
            if player.position == '\033[35mX\033[0m':
                return '\033[35mX\033[0m'
            elif player.position == '\033[2;34;5mO\033[0m':
                return '\033[2;34;5mO\033[0m'
        elif not game.won_game(player) and len(num) == 0:
            print("\033[2;31;1mI\'ts Tie !\033[0m")
            return 'Tie'
        else:
            player = game.change_turn(player)

# function to choose randomly who start to play first.
def whofirst():
    players = ("Heads", "Tails")
    x = random.choice(players)
    print(x, 'play first')

# ask the users for music while playing
def play_music():
    print('\033[2;36;1mWill you want to hear some music while playing ?\nY/N = \033[0m')
    answer = input().lower()
    if answer == 'y' :
        file = 'C:\\Users\\rinay\\Desktop\\playlist\\Coldplay.mp3'
        print('\033[2;36;1mPlaying sound while you playing\033[0m')
        os.startfile(file)

play_music()
whofirst()
if __name__ == '__main__':
    wining_dict = {'X': 0, 'O': 0, 'Tie': 0}
    restart = 'y'
    while restart == 'y':
        gameon = start()
        if gameon == '\033[35mX\033[0m':
            wining_dict['X'] = wining_dict['X'] + 1
        elif gameon == '\033[2;34;5mO\033[0m':
            wining_dict['O'] = wining_dict['O'] + 1
        else:
            wining_dict['Tie'] = wining_dict['Tie'] + 1
        restart = input("Do want to play Again? (Y/N) :").lower()
    else:
        print("\033[2;31;1mGame Over !\033[0m")
        print('\033[2;31;1mFinal winnings board ->\033[0m', wining_dict)