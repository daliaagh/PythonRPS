#!/usr/bin/env python3

import random

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""

class Player:

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

class RandomPlayer(Player):
    def move(self):
        return (random.choice(moves))

    def learn(self, my_move, their_move):
        pass

class HumanPlayer(Player):
    def move(self):
        answer = input("""Choose your move - Rock, Paper or """
        """Scissors? To exit press x\n""")
        while answer not in moves and answer != 'x':
            answer = input("Enter a valid move!")
        return answer

    def learn(self, my_move, their_move):
        pass

class ReflectPlayer(Player):
    pass

    def learn(self, my_move, their_move):
        pass

class CyclePlayer(Player):
    pass

    def learn(self, my_move, their_move):
        pass

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))

class Game:
    def __init__(self, RandomPlayer, HumanPlayer):
        self.RandomPlayer = RandomPlayer
        self.HumanPlayer = HumanPlayer
        self.count_wins = 0
        self.count_losses = 0
        self.count_ties = 0
#        self.score1 = 0
#        self.score2 = 0

#    def score(self):
#        move1 = self.RandomPlayer.move()
#        move2 = self.HumanPlayer.move()
#        if beats(move1, move2):
#            self.count_wins += 1
#            print(self.count_wins)
#        if HumanPlayer.move == RandomPlayer.move:
#            self.count_ties += 1
#            print(self.count_ties)
#        elif beats(move2, move1):
#            self.count_losses += 1
#            print(self.count.losses)
#        else:
#            print("tada")

    def play_round(self):
#        print(self.count_wins)
        move1 = self.RandomPlayer.move()
        move2 = self.HumanPlayer.move()
        print(f"Player 1 Move: {move1}  Player 2 Move: {move2}")

        if beats(move1, move2):
            self.count_wins += 1
            print(f"wins:{self.count_wins}")
#        elif HumanPlayer.move == RandomPlayer.move:
#            self.count_ties += 1
        elif move1 == move2:
            self.count_ties += 1
            print(f"ties:{self.count_ties}")
        elif beats(move2, move1):
            self.count_losses += 1
            print(f"losses:{self.count_losses}")
        else:
            print("tada")

        self.score1 = self.count_wins
        self.score2 = self.count_wins
        print(f"Player 1 Score: {self.score1}    Player 2 Score: {self.score2}\n")

        self.RandomPlayer.learn(move1, move2)
        self.HumanPlayer.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(10):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")
        print(f"Player One Wins: {self.score1}    Player Two Wins: {self.score2}\n")

if __name__ == '__main__':
    game = Game(RandomPlayer(), HumanPlayer())
    game.play_game()
