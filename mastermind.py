import random


class Game:
    """Represents a game of Mastermind."""

    def __init__(self, guesses=8, code=None):
        """Creates a new Game with the specified number of guesses available for the player."""

        self._game_state = "UNFINISHED"                 # Possible game states: UNFINISHED, WON, LOST

        # Colors available for the game
        # R = Red, Y = Yellow, G = Green, B = Blue, W = White, K = Black
        self._colors = ['R', 'Y', 'G', 'B', 'W', 'K']

        if code is None:
            self.code = [random.choice(self._colors),   # Create the random code for this game
                         random.choice(self._colors),
                         random.choice(self._colors),
                         random.choice(self._colors)]
        else:
            self.code = code

        self.guesses = guesses                          # Number of guesses currently available

    def get_code(self):
        """Returns a string representing the current code"""
        return self.code[0] + self.code[1] + self.code[2] + self.code[3]

    def get_game_state(self):
        """Returns the current game state ('UNFINISHED', 'WON', or 'LOST')"""
        return self._game_state

    def check(self, guess):
        """Checks to see whether a guess is correct, or partially correct.
        Prints out feedback for the player, then updates the game state and the number of guesses.

        Args:
            guess:  A four-letter string representing a Mastermind guess (e.g., "RYGB", "GGBB", "KRBW")
        """

        correct = 0
        partial = 0

        leftover_guess = []
        leftover_code = []

        # Calculate how many pegs have been guessed correctly
        for position, char in enumerate(guess):
            if self.code[position] == char:    # Peg is completely correct
                correct += 1
            else:
                leftover_guess.append(char)
                leftover_code.append(self.code[position])

        for char in leftover_guess:         # Go over the leftovers to find partially correct guesses
            if char in leftover_code:
                partial += 1
                leftover_code.remove(char)

        if correct == 4:                    # Check for win state
            self._game_state = "WON"
            print('YOU WON!\n')
        elif self.guesses == 1:             # Check for loss state
            self._game_state = "LOST"
            print('You ran out of guesses! The code was: ' + self.get_code() + '\n')

        # Neither win nor loss, output results and decrement the guess counter
        else:
            self.guesses -= 1
            if correct == 0 and partial == 0:
                print("No pegs were guessed correctly.")
            else:
                results = 'X' * correct + 'O' * partial
                print()
                print('Your results: ' + results)
                if self.guesses == 1:
                    print('You have ' + str(self.guesses) + " guess left.\n")
                else:
                    print('You have ' + str(self.guesses) + " guesses left.\n")

    def is_valid_guess(self, guess):
        """Checks to see if the guess is valid (correct length, with only valid letters)"""
        if len(guess) != 4:
            return False
        for char in guess:
            if char not in self._colors:
                return False
        return True


def print_game_intro():
    """Prints the game intro text with instructions."""

    print("""
Welcome to Mastermind, a game where you try to guess the secret code!
Each code has four colored pegs, in order. The colors are:
R = Red, Y = Yellow, G = Green, B = Blue, W = White, K = Black.
(Duplicate colors are allowed.)

Once you have made your guess, you'll get an 'X' for each peg that is the
right color and in the right position, and an 'O' for each peg that is the
right color, but in the wrong position. Good luck!
    """)


def main():
    """Runs the Mastermind Game"""

    playing = True
    print_game_intro()

    while playing:

        # Initialize Game
        game = Game()
        # print(game.get_code())    # For testing only

        # Main Guessing Loop
        print("A new code has been generated. Try to guess the code!")
        while game.get_game_state() == 'UNFINISHED':
            guess = input("Type four letters to enter your guess (Example: RYGB):").upper()
            while not game.is_valid_guess(guess):
                print("Your guess must be four letters from the following list: R, Y, G, B, W, K.")
                guess = input("Try guessing again (Example guesses: RYGB, BBYY, YRWK): ")
            game.check(guess)

        play_again = input("Play again? Y/N: ").upper()
        while play_again != 'Y' and play_again != 'N':
            play_again = input("Play again? Y/N: ").upper()

        if play_again == 'N':
            playing = False

    print()


if __name__ == '__main__':
    main()
