######################################
# Shut the Box programming assignment
# Liz Denson & Connor Loudermilk
# 2023-09-29
######################################

from CSC201Ut import MSDie

def __add__(self, other):
    return self._value + other._value
MSDie.__add__ = __add__

d1 = MSDie(6)
d2 = MSDie(6)
print(d1, d2)
print (d1 + d2)

# { 1, 2, 3, 4, 5, 6, 7, 8, 9 }
# { {1, 6}, {}} ... etc ---> look at a power set function
# (run through all possible combinations and see which combinations equal the sum of the die)
# then decide based on all of the combos/permutations (count in binary from 0 to the number for the tiles to lay down)

##Connor Loudermilk
##CSC210
##Dr. Gourd
## Shut the Box
##9/22/2023
#########################
from CSC201UT import MSDie
import random


class ShutTheBox:
    def __init__(self):
        self.tiles = list(range(1, 10))
        self.dice = [1, 2]
        self.players = []

    def roll_dice(self): ##Use MSDIE CODE HERE
        return [random.randint(1, 6) for _ in range(len(self.dice))]

    def play_game(self, num_players):
        for player_num in range(1, num_players + 1):
            player_score = sum(self.tiles)
            while player_score > 0:
                dice_result = self.roll_dice()
                print(f"Player {player_num} rolled: {dice_result}")
                valid_moves = self.get_valid_moves(dice_result)
                if not valid_moves:
                    break
                print(f"Valid moves: {valid_moves}")
                chosen_tiles = self.choose_move(valid_moves)
                self.flip_tiles(chosen_tiles)
                player_score = sum(self.tiles)
                print(f"Player {player_num}'s current score: {player_score}")
            self.players.append((player_num, player_score))
        self.display_results()

    def get_valid_moves(self, dice_result):
        valid_moves = []
        for i in range(1, 10):
            for subset in self.subsets(self.tiles, i):
                if sum(subset) == sum(dice_result):
                    valid_moves.append(subset)
        return valid_moves

    

    def choose_move(self, valid_moves):
       

    def flip_tiles(self, tiles_to_flip):
        for tile in tiles_to_flip:
            self.tiles.remove(tile)

    def display_results(self):
        self.players.sort(key=lambda player: player[1])
        winner_score = self.players[0][1]
        print("\nResults:")
        for player_num, score in self.players:
            print(f"Player {player_num}: {score}")
        winners = [player[0] for player in self.players if player[1] == winner_score]
        if len(winners) == 1:
            print(f"Player {winners[0]} wins!")
        else:
            print(f"Players {', '.join(map(str, winners))} tie!")

def main():
    print("Welcome to Shut the Box!")
    num_players = int(input("How many players? "))
    game = ShutTheBox()
    game.play_game(num_players)

if __name__ == "__main__":
    main()

