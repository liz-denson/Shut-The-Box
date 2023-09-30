######################################
# Shut the Box programming assignment
# Liz Denson & Connor Loudermilk
# 2023-09-29
######################################

from CSC201UT import MSDie
import random

class ShutTheBox:
    def __init__(self):
        self.tiles = list(range(1, 10))
        self.dice = [MSDie(6), MSDie(6)] # Initialized with two 6-sided dice
        self.players = []

    def roll_dice(self):
        if sum(self.tiles) <= 6:
            return [self.dice[0].roll()] # Roll only one die if sum of tiles is 6 or less
        else:
            return [die.roll() for die in self.dice] # Roll both dice otherwise

    def play_game(self, num_players):
        for player_num in range(1, num_players + 1):
            self.tiles = list(range(1, 10)) # Reset tiles for each player
            player_score = sum(self.tiles)
            while player_score > 0:
                dice_result = self.roll_dice()
                dice_sum = sum(dice_result)
                print(f"Player {player_num} rolled: {dice_result}")
                valid_moves = self.get_valid_moves(dice_sum)
                if not valid_moves:
                    break
                print(f"Valid moves: {valid_moves}")
                chosen_tiles = self.choose_move(valid_moves)
                self.flip_tiles(chosen_tiles)
                player_score = sum(self.tiles)
                print(f"Player {player_num}'s current score: {player_score}")
            self.players.append((player_num, player_score))
        self.display_results()

    def get_valid_moves(self, dice_sum):
        valid_moves = []
        for i in range(1, 2**len(self.tiles)):
            bits = bin(i)[2:].zfill(len(self.tiles))
            cur_combo = []
            tile_sum = 0
            for bit_index in range(len(bits)):
                if bits[bit_index] == '1':
                    tile_sum += bit_index + 1
                    cur_combo.append(bit_index + 1)
            if tile_sum == dice_sum:
                valid_moves.append(cur_combo)
        return valid_moves

    def choose_move(self, valid_moves):
        return random.choice(valid_moves)

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
