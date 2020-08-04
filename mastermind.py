import random


class Game:
    """Represents a game of Mastermind"""

    def __init__(self, guesses=8):
        """Creates a new Game with the specified number of guesses available for the player."""
        self.guesses = guesses
        self.code = Code()

    def get_code(self):
        """Returns a string representing the current code"""
        return self.code.get_code()

    def make_guess(self, guess):
        """Takes a guess and returns a code representing how many pegs are correct.

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


class Code:
    """Represents a Mastermind code to be guessed"""

    def __init__(self):
        pegs = ['R', 'Y', 'G', 'B', 'W', 'K']
        self.code = [random.choice(pegs),
                     random.choice(pegs),
                     random.choice(pegs),
                     random.choice(pegs)]

    def get_code(self):
        """Returns a string representing the current code"""
        return self.code[0] + ' ' + self.code[1] + ' ' + self.code[2] + ' ' + self.code[3]


def main():
    """Runs the Mastermind Game

    """
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
    guess = input("Type four letters to enter your guess (Example: RYGB):").upper()

    game1 = Game()
    print(game1.get_code())

    print()
    print(guess)


if __name__ == '__main__':
    main()
