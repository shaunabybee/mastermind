import random


class Game:
    """Represents a game of Mastermind."""


    def __init__(self, guesses=8):
        """Creates a new Game with the specified number of guesses available for the player."""
        self._pegs = ['R', 'Y', 'G', 'B', 'W', 'K']  # Available colors for the Mastermind pegs
        self.guesses = guesses                       # Number of guesses currently available
        self.code = [random.choice(self._pegs),      # Array that represents the code (four colored pegs in order)
                     random.choice(self._pegs),
                     random.choice(self._pegs),
                     random.choice(self._pegs)]

    def get_code(self):
        """Returns a string representing the current code"""
        return self.code[0] + self.code[1] + self.code[2] + self.code[3]

    def make_guess(self, guess):
        """Takes a guess and returns a code representing how many pegs are correct.
        Also decrements self.guesses.

        Args:
            guess:  A four-letter string representing a Mastermind guess, example: "RYGB"
                    Colored pegs are represented as follows:
                        R: Red
                        Y: Yellow
                        G: Green
                        B: Blue
                        W: White
                        K: Black
        Returns:
            A zero- to four-character string representing how many pegs in the guess are correct.
                X = Correct: Peg is the right color, in the right position
                O = Partially Correct: Peg is the right color, but in the wrong position
            Examples:
                XXXX: Guess is entirely correct (all pegs are the right color, in the right position)
                XXO: Guess includes two pegs that are the right color, in the right position,
                     and also includes one peg that is the right color, in the wrong position.
                O: Guess includes one peg that is the right color, in the wrong position.
                Empty string: Guess is entirely wrong (no pegs are the right color)
        """

        matched = [False, False, False, False]
        correct = 0
        partial = 0

        for position, char in enumerate(guess):
            print(position, char)
            if char in self.code:   # TODO YOU ARE HERE
                print(char)

        self.guesses -= 1


def print_game_intro():
    """Prints the game intro text with instructions."""

    print("Welcome to Mastermind! A new code has been generated for you to guess.")
    print("Each code has four colored pegs, in order. The colors are:")
    print("R = Red, Y = Yellow, G = Green, B = Blue, W = White, K = Black.")
    print("Duplicate colors are allowed (a code could have four blue pegs, for example).")
    print()
    print("Once you have made a guess, you'll get a code telling you whether you guessed any pegs correctly.")
    print("You'll get an 'X' for each peg that is the correct color in the correct position, and an 'O' for")
    print("each peg that is correct color, but in the wrong position.")
    print("For example, the code \"XXO\" means that two pegs are positioned correctly, and one peg is the right")
    print("color, but in the wrong position. Good luck!")
    print()


def main():
    """Runs the Mastermind Game"""

    print_game_intro()

    game1 = Game()
    guess = input("Type four letters to enter your guess (Example: RYGB):").upper()
    game1.make_guess(guess)

    print(game1.get_code())

    print()



if __name__ == '__main__':
    main()
