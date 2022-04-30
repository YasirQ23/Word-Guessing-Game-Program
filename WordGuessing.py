import random

# Create a class for the game
# Pick a word from a pre-made random words list


class Game():
    def __init__(self):
        self.board = ['_', '_', '_', '_', '_']
        self.turns_left = 7
        self.guessed_letters = []
        self.word = random.choice(
            ['roate', 'store', 'stare', 'pious', 'ouija', 'aisle', 'ocean', 'about', 'cones', 'audio'])

# Show board
    def show_board(self):
        for letter in self.board:
            print(letter, end=" ")

# Give welcome msg and show blanked out word
    def start_game(self):
        print(f'Hello, Welcome to Yasir\'s word guessing game.')
        Game.show_board(self)
        print(f'\nThat is the word you\'ll be guessing today.')

# Take in an input to start off the game
    def guesstaker(self):
        self.guess = input(
            f'Please enter the letter you would like to guess.\n')[0].lower()
        while self.guess.isnumeric():
            print(f'Invalid input, Please try again')
            self.guess = input(
                f'\nPlease enter the letter you would like to guess.\n')[0].lower()
        if self.guess.upper() in self.guessed_letters:
            print(
                f'You\'ve already used the letter "{self.guess.upper()}" please try another letter.')
            self.guess = input(
                f'Please enter the letter you would like to guess.\n')[0].lower()
        elif self.guess in self.word:
            Game.correct_choice(self)
        elif self.guess not in self.word:
            Game.wrong_choice(self)

# If the letter input by the user is correct 1)give msg "you got it right that letter is in the word" 2)show board with letter in place
# 3)show letters used 4)show turns remaining
    def correct_choice(self):
        print(f'Correct! "{self.guess.upper()}" is in the word.')
        index = self.word.index(self.guess)
        self.board[index] = self.guess
        Game.show_board(self)
        self.guessed_letters.append(self.guess.upper())
        print(
            f'\nThese are the letters you have already used:\n{self.guessed_letters}')
        print(f'You have "{self.turns_left}" attempts remaining')

# If the letter input by the user is incorrect 1) give msg "sorry that letteris not in the word" 2) show board uncahnged
# 3) show letters used 4)take away a turn 5)show turns remaining
    def wrong_choice(self):
        print(
            f'Sorry, Unfortunatley "{self.guess.upper()}" is not in the word.')
        self.guessed_letters.append(self.guess.upper())
        print(
            f'These are the letters you have already used:\n{self.guessed_letters}')
        self.turns_left -= 1
        print(f'You have "{self.turns_left}" attempts remaining')
        Game.show_board(self)

# repeat this process until the last turn either completes the word or leaves player with 0 turns left
# If game won respond with good job yata yata and display full board and turns remaining and letters used
# or if game lost respond with whatever major loser duhh show fulll board and letters used (can also just show what same as win but with a loser statement)


my_game = Game()


def run():
    my_game.start_game()
    while my_game.turns_left > 0 and '_' in my_game.board:
        my_game.guesstaker()
    if my_game.turns_left == 0:
        print(
            f'\nWow looks like your out of turns there bud, Better luck next time.\nThe word was "{my_game.word.title()}"')
    else:
        print(
            f'I knew you could do it, Congrats you won and with "{my_game.turns_left}" lives left!!!\nThe word was "{my_game.word.title()}"')


run()
