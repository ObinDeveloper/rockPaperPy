from players import HumanPlayer


def beats(one, two):
    return ((one == 'rock' and two in ['scissors', 'lizard']) or
            (one == 'scissors' and two in ['paper', 'lizard']) or
            (one == 'paper' and two in ['rock', 'spock']) or
            (one == 'lizard' and two in ['spock', 'paper']) or
            (one == 'spock' and two in ['scissors', 'rock']))


class Game:
    def __init__(self, p1, p2, player_name=None, rounds=3):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0
        self.rounds = rounds
        self.player_name = player_name

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()

        print(f"Player 1: {move1}  Player 2: {move2}")

        if beats(move1, move2):
            print("Player 1 wins the round!")
            self.p1_score += 1
        elif beats(move2, move1):
            print("Player 2 wins the round!")
            self.p2_score += 1
        else:
            print("It's a tie!")

        print(f"Score: Player 1 - {self.p1_score}, "
              f"Player 2 - {self.p2_score}")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round_num in range(self.rounds):
            print(f"Round {round_num + 1}:")
            self.play_round()
        print("Game over!")
        print(f"Final score: Player 1 - {self.p1_score}, "
              f"Player 2 - {self.p2_score}")
        self.announce_winner()

    def announce_winner(self):
        if self.p1_score > self.p2_score:
            if isinstance(self.p1, HumanPlayer):
                print(f"Yay! {self.player_name}, you are the winner! 😊")
            else:
                print("Player 1 wins the game!")
        elif self.p2_score > self.p1_score:
            if isinstance(self.p2, HumanPlayer):
                print(f"Unfortunately, {self.player_name}, you lost. 😞")
            else:
                print("Player 2 wins the game!")
        else:
            print("It's a tie!")
