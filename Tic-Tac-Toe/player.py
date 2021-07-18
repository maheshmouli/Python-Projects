import math
import random


class Player:
    def __init__(self, letter):
        self.name = letter

    def get_move(self, game):
        pass

class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        sqr = random.choice(game.available_moves())
        return sqr

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_sqr = False
        val = None
        while not valid_sqr:
            square = input(self.letter + '\'s turn. Enter your move(0-9): ')

            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_sqr = True
            except ValueError:
                print("Invalid Input. Try Again")

        return val
