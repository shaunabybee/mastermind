import random


class Game:
    """Represents a game of Mastermind."""

    def __init__(self, guesses=8):
        """Creates a new Game with the specified number of guesses available for the player."""

        self._game_state = "UNFINISHED"                 # Possible game states: UNFINISHED, WON, LOST

        self._colors = ['R', 'Y', 'G', 'B', 'W', 'K']   # Colors available for the game

        self.code = [random.choice(self._colors),       # Create the random code for this game
                     random.choice(self._colors),
                     random.choice(self._colors),
                     random.choice(self._colors)]

        self.guesses = guesses                          # Number of guesses currently available

    def get_code(self):
        """Returns a string representing the current code"""
        return self.code[0] + self.code[1] + self.code[2] + self.code[3]

    def get_game_state(self):
        """Returns the current game state ('UNFINISHED', 'WON', or 'LOST')"""
        return self._game_state

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
        Prints:
            A zero- to four-character string representing how many pegs in the guess are correct.
                X = Correct: Peg is the right color, in the right position
                O = Partially Correct: Peg is the right color, but in the wrong position
            Examples:
                XXXX: Guess is entirely correct (all pegs are the right color, in the right position)
                XXO: Guess includes two pegs that are the right color, in the right position,
                     and also includes one peg that is the right color, in the wrong position.
                O: Guess includes one peg that is the right color, in the wrong position.
                'No pegs were guessed correctly': Guess is entirely wrong (no pegs are the right color)
        """

        # Store the positions of each peg in the code
        # As pegs are guessed, positions will be removed from this index (so they are not used twice)
        positions = {
            'R': [],
            'Y': [],
            'G': [],
            'B': [],
            'W': [],
            'K': []
        }

        for i in range(len(self.code)):
            positions[self.code[i]].append(i)

        correct = 0
        partial = 0

        # Calculate how many pegs have been guessed correctly
        for position, char in enumerate(guess):
            if position in positions[char]:    # Peg is completely correct
                correct += 1
                positions[char].remove(position)
            elif len(positions[char]) > 0:     # Peg is correct color, but in the wrong place
                partial += 1

        if correct == 0 and partial == 0:
            print("No pegs were guessed correctly.")
        else:
            results = 'X' * correct + 'O' * partial
            print(results)

        self.guesses -= 1


def print_game_intro():
    """Prints the game intro text with instructions."""

    print("""
Welcome to Mastermind! A new code has been generated for you to guess.
The code has four colored pegs, in order. The colors are:
R = Red, Y = Yellow, G = Green, B = Blue, W = White, K = Black.
Duplicate colors are allowed.

Once you have made your guess, you'll get an 'X' for each peg that is the
right color and in the right position, and an 'O' for each peg that is the
right color, but in the wrong position. 

For example, 'XXO' means that you guessed two pegs right, and one peg is
the right color, but in the wrong place. Good luck!
    """)


def main():
    """Runs the Mastermind Game"""

    # START NEW GAME
    print_game_intro()
    game1 = Game()
    print(game1.get_code())

    # MAIN GAME LOOP
    while game1.get_game_state() == 'UNFINISHED':
        print()
        guess = input("Type four letters to enter your guess (Example: RYGB):").upper()
        game1.make_guess(guess)
        print(str(game1.guesses) + " guesses left.")


    print()


if __name__ == '__main__':
    main()
