# Import your Game class
from game import Game
# Create your Dunder Main statement.
if __name__ == '__main__':
    new_game = Game()
    new_game.game_welcome()
    new_game.start()
# Inside Dunder Main:
## Create an instance of your Game class
## Start your game by calling the instance method that starts the game loop
