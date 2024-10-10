import random
from game import Game
from players import HumanPlayer, AllRockPlayer
from players import RandomPlayer, ReflectPlayer, CyclePlayer


def tournament(competitors, rounds=5, player_name=None):
    while True:
        results = {competitor.__class__.__name__: 0
                   for competitor in competitors}

        human_player = competitors[0]

        for competitor in competitors[1:]:
            print(f"\n{human_player.__class__.__name__} vs "
                  f"{competitor.__class__.__name__}")
            game = Game(human_player, competitor,
                        player_name=player_name, rounds=rounds)
            game.play_game()

            if game.p1_score > game.p2_score:
                results[human_player.__class__.__name__] += 1
            elif game.p2_score > game.p1_score:
                results[competitor.__class__.__name__] += 1

        sorted_results = sorted(results.items(),
                                key=lambda x: x[1], reverse=True)

        print("\n🏁 Tournament Results 🏁")
        rank = 1
        human_player_rank = None

        for player, wins in sorted_results:
            if rank == 1:
                print(f"{rank}. 🏆 {player}: {wins} wins")
            else:
                print(f"{rank}. {player}: {wins} wins")

            if player == "HumanPlayer":
                human_player_rank = rank

            rank += 1

        if human_player_rank:
            print(f"\n🎉 {player_name}, you ranked #{human_player_rank} "
                  "in the tournament! 🎉")

        winner = sorted_results[0][0]
        if winner == "HumanPlayer":
            print(f"🏆 Congratulations, {player_name}, you are the "
                  "tournament champion! 🏆")
        else:
            print(f"🏆 The tournament champion is {winner}! 🏆")

        play_again = input("\nWould you like to play the tournament "
                           "again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing the tournament! Goodbye!")
            break

    return False


def main():
    while True:
        player_name = input("What's your name? ")

        human_player = HumanPlayer()
        # List of available computer players
        computer_players = [AllRockPlayer(), RandomPlayer(),
                            ReflectPlayer(), CyclePlayer()]

        while True:
            game_type = input("Do you want to play a single game or "
                              "a tournament? (single/tournament): ").lower()
            if game_type in ['single', 'tournament']:
                break
            else:
                print("I don't understand your entry, "
                      "please try again.")

        if game_type == 'single':
            # Randomly select a computer player for single mode
            computer_player = random.choice(computer_players)
            print("You're playing "
                  f"against {computer_player.__class__.__name__}")

            game = Game(human_player, computer_player,
                        player_name=player_name, rounds=3)
            game.play_game()

            play_again = input("\nWould you like to play again? "
                               "(yes/no): ").lower()
            if play_again != 'yes':
                print("Thanks for playing! Goodbye!")
                return

        elif game_type == 'tournament':
            if not tournament([human_player] + computer_players, rounds=5,
                              player_name=player_name):
                return


if __name__ == '__main__':
    main()
