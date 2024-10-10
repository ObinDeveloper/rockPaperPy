moves = ['rock', 'paper', 'scissors', 'lizard', 'spock']


def beats(one, two):
    return ((one == 'rock' and two in ['scissors', 'lizard']) or
            (one == 'scissors' and two in ['paper', 'lizard']) or
            (one == 'paper' and two in ['rock', 'spock']) or
            (one == 'lizard' and two in ['spock', 'paper']) or
            (one == 'spock' and two in ['scissors', 'rock']))
