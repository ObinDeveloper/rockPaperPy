import random


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class AllRockPlayer(Player):
    def move(self):
        return 'rock'


class RandomPlayer(Player):
    def move(self):
        return random.choice(['rock', 'paper', 'scissors',
                              'lizard', 'spock'])


class ReflectPlayer(Player):
    def __init__(self):
        self.opponent_move = None

    def move(self):
        if self.opponent_move:
            return self.opponent_move
        return random.choice(['rock', 'paper', 'scissors',
                              'lizard', 'spock'])

    def learn(self, my_move, their_move):
        self.opponent_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.moves = ['rock', 'paper', 'scissors',
                      'lizard', 'spock']
        self.current_move = 0

    def move(self):
        move = self.moves[self.current_move]
        self.current_move = (self.current_move + 1) % len(self.moves)
        return move


class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("Enter your move (rock, paper, "
                         "scissors, lizard, spock): ").lower()
            if move in ['rock', 'paper', 'scissors', 'lizard', 'spock']:
                return move
            print("Invalid move! Please try again.")
