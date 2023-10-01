######################################
# Shut The Box
# Liz Denson & Connor Loudermilk
# 2023-09-29
######################################

"""Import Libraries"""
from CSC201UT import MSDie
import random

#######
# CLASS
#######

class ShutTheBox:
    def __init__(self):
        self.tiles = list(range(1, 10)) # initialize tiles from 1 to 9
        self.dice = [MSDie(6), MSDie(6)] # create two 6-sided dice
        self.players = [] # list to store players and their scores

    def roll_dice(self):
        """Roll one or two dice based on the sum of tiles."""
        if sum(self.tiles) <= 6: # if sum of tiles is 6 or less
            return [self.dice[0].roll()] # roll only one die
        else: # otherwise
            return [die.roll() for die in self.dice] # roll both dice

    def play_game(self, num_players):
        """Main game loop for each player."""
        for player_num in range(1, num_players + 1):  # loop through each player
            self.tiles = list(range(1, 10)) # reset tiles
            player_score = sum(self.tiles)  # initialize player_score with tile sum
            while player_score > 0:  # while player_score is greater than zero
                dice_result = self.roll_dice()  # roll dice and store roll
                dice_sum = sum(dice_result)  # store roll sum
                valid_moves = self.get_valid_moves(dice_sum)  # get valid tiles based on dice sum
                if not valid_moves:  # if no valid tiles
                    break  # end player's turn
                chosen_tiles = self.choose_move(valid_moves)  # choose & store valid tiles to flip
                self.flip_tiles(chosen_tiles)  # flip chosen tiles
                player_score = sum(self.tiles)  # update player's score
            self.players.append((player_num, player_score))  # append player number & store to the players list
        self.display_results()  # display results

    def get_valid_moves(self, dice_sum):
        """Calculate valid moves based on the sum of dice rolled."""
        valid_moves = []  # initialize empty list to store valid moves
        for i in range(1, 2**len(self.tiles)):  # iterate over range from 1 to 2 to the power of number of tiles
            bits = bin(i)[2:].zfill(len(self.tiles))  # convert to binary, remove prefix, & zero fill to tile length
            cur_combo = []  # empty list for cur combo of tiles
            tile_sum = 0  # initialize sum of tiles to 0
            for bit_index in range(len(bits)):  # iterate over each bit in binary
                if bits[bit_index] == '1':  # if bit at bit_index is 1
                    tile_sum += self.tiles[bit_index]  # add tile to tile_sum
                    cur_combo.append(self.tiles[bit_index])  # add the tile to cur combo
            if tile_sum == dice_sum:  # if tile sum = dice sum
                valid_moves.append(cur_combo)  # add cur combo to list of valid tiles
        return valid_moves  # return list of valid tiles


    def choose_move(self, valid_moves):
        """Randomly select one move from the list of valid moves."""
        return random.choice(valid_moves)

    def flip_tiles(self, tiles_to_flip):
        """Remove tiles from the list that are flipped."""
        for tile in tiles_to_flip:
            self.tiles.remove(tile)

    def display_results(self):
        """Sort players based on their scores and display the results."""
        for player_num, score in self.players:
            print(f"Player {player_num}: {score}") # print each player's score
        winner_score = min(self.players, key=lambda player: player[1])[1] # find player with min score
        winners = [player[0] for player in self.players if player[1] == winner_score] # list players with min score
        if len(winners) == 1: # if only one winner
            print(f"\033[1m\033[92mPlayer {winners[0]} wins!\033[0m") # announce winner
        else: # otherwise
            print(f"\033[1m\033[92mPlayers {', '.join(map(str, winners))} tie!\033[0m") # announce tie

######
# MAIN
######

def main():
    """Main function to initiate the game."""
    print("\033[1mWelcome to Shut the Box!\033[0m") # print bold game message
    while True:
        try:
            num_players = int(input("\033[94mHow many players?\033[0m ")) # input number of players in blue
            if num_players <= 0: 
                print("\033[91mPlease enter a positive number of players.\033[0m") # red error if not positive (ex: 0)
                continue # request user input again
            break # exit loop
        except ValueError: # ValueError when input isn't valid integer
            print("\033[91mPlease enter a valid integer for the number of players.\033[0m") # red error if invalid
    game = ShutTheBox() # instantiate a new game
    game.play_game(num_players) # call the play_game method
    
if __name__ == "__main__":
    main() # call main function

#########
# SOURCES
#########

# ANSI escape codes used to format text the terminal
    # Lines (73, 75, 83, 86, 88, & 92)
    # URL: https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797#file-ansi-md
    
# Try Except error handling
    # Lines (89 - 96)
    # URL: https://www.w3schools.com/python/python_try_except.asp
