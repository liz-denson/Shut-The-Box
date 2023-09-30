######################################
# Shut The Box programming assignment
# Liz Denson & Connor Loudermilk
# 2023-09-29
######################################

from CSC201UT import MSDie
import random

class ShutTheBox:
    def __init__(self):
        self.tiles = list(range(1, 10)) # initialize tiles from 1 to 9
        self.dice = [MSDie(6), MSDie(6)] # create two 6-sided dice
        self.players = [] # list to store players and their scores

    def roll_dice(self):
        """Roll one or two dice based on the sum of tiles."""
        if sum(self.tiles) <= 6:
            return [self.dice[0].roll()] # roll one die if sum of tiles is 6 or less
        else:
            return [die.roll() for die in self.dice] # otherwise, roll both dice

    def play_game(self, num_players):
        """Main game loop for each player."""
        for player_num in range(1, num_players + 1):
            self.tiles = list(range(1, 10)) # reset tiles for each player
            player_score = sum(self.tiles)
            while player_score > 0:
                dice_result = self.roll_dice() # roll dice
                dice_sum = sum(dice_result) # sum of dice rolled
                valid_moves = self.get_valid_moves(dice_sum) # get valid moves for the current roll
                if not valid_moves: # end turn if no valid moves
                    break
                chosen_tiles = self.choose_move(valid_moves) # randomly choose a valid move
                self.flip_tiles(chosen_tiles) # flip chosen tiles
                player_score = sum(self.tiles) # update player score
            self.players.append((player_num, player_score)) # record player's score
        self.display_results() # display the final results

    def get_valid_moves(self, dice_sum):
        """Calculate valid moves based on the sum of dice rolled."""
        valid_moves = []
        for i in range(1, 2**len(self.tiles)):
            bits = bin(i)[2:].zfill(len(self.tiles))
            cur_combo = []
            tile_sum = 0
            for bit_index in range(len(bits)):
                if bits[bit_index] == '1':
                    tile_sum += self.tiles[bit_index] # sum tiles corresponding to '1' bits
                    cur_combo.append(self.tiles[bit_index]) # add those tiles to current combination
            if tile_sum == dice_sum:
                valid_moves.append(cur_combo) # if the sum matches dice_sum, add combo to valid moves
        return valid_moves

    def choose_move(self, valid_moves):
        """Randomly select one move from the list of valid moves."""
        return random.choice(valid_moves)

    def flip_tiles(self, tiles_to_flip):
        """Remove tiles from the list that are flipped."""
        for tile in tiles_to_flip:
            self.tiles.remove(tile)

    def display_results(self):
        """Sort players based on their scores and display the results."""
        self.players.sort(key=lambda player: player[1])
        winner_score = self.players[0][1]
        for player_num, score in self.players:
            print(f"Player {player_num}: {score}")
        winners = [player[0] for player in self.players if player[1] == winner_score]
        if len(winners) == 1:
            print(f"Player {winners[0]} wins!") # announce the winner
        else:
            print(f"Players {', '.join(map(str, winners))} tie!") # announce a tie

def main():
    """Main function to initiate the game."""
    print("Welcome to Shut the Box!")
    while True:
        try:
            num_players = int(input("How many players? ")) # input number of players
            if num_players <= 0:
                print("Please enter a positive number of players.")
                continue
            break
        except ValueError: # non-integer value input
            print("Please enter a valid integer for the number of players.")
    game = ShutTheBox() # game instance
    game.play_game(num_players) # start the game

if __name__ == "__main__":
    main() # call main function
