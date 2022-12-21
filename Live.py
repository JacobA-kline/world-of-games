from CurrencyRouletteGame import CurrencyRouletteGame
from GuessGame import GuessGame
from MemoryGame import MemoryGame
from Score import add_score


class Live:
    def __init__(self):
        self.username = ""
        self.game_difficulty = int
        self.game_type = int

    def welcome(self):
        self.username = input("Hi, What is your name?\n").title()
        greeting = f"Hello {self.username}! and welcome to the World of Games!\nHere you can find many cool games to " \
                   f"play."
        print(greeting)

    def load_game(self):
        testing_game_type = True
        testing_game_difficulty = True
        while testing_game_type:
            try:
                self.game_type = int(input(
                    "Please choose a game to play:\n1. Guess Game - guess a number and see if you chose like the "
                    "computer.\n "
                    "2. Memory Game - a sequence of numbers will appear for 1 second "
                    "and you "
                    "have to guess it back.\n 3. "
                    "Currency Roulette - try and guess the value of a random amount of USD in ILS.\nPlease type the "
                    "game "
                    "number "
                    "1 - 3:\n"))
                if self.game_type not in range(1, 4):
                    print("Oops, you chose a number out of the scope. type a number between please try again.")
                    continue
            except ValueError:
                print("Oops, invalid game type. Please type a valid number between 1 and 3.\n")
                continue
            self.game_difficulty = int
            while testing_game_difficulty:
                try:
                    self.game_difficulty = int(input("Please choose game difficulty from 1 - 5:\n"))
                    if self.game_difficulty not in range(1, 6):
                        print("Oops, you chose a game difficulty out of the scope please try again.")
                        continue
                except ValueError:
                    print("Oops, invalid game difficulty. Please type a valid number between 1 and 5.")
                    continue
                testing_game_type = False
                testing_game_difficulty = False

        if self.game_type == 1:
            guessgame = GuessGame()
            guessgame.welcome()
            winning = guessgame.play(difficulty=self.game_difficulty)
            self.is_winning(im_winning=winning)
            self.play_again()
        elif self.game_type == 2:
            memorygame = MemoryGame()
            winning = memorygame.play(difficulty=self.game_difficulty)
            self.is_winning(im_winning=winning)
            self.play_again()
        else:
            currencyroulettegame = CurrencyRouletteGame()
            winning = currencyroulettegame.play(difficulty=self.game_difficulty)
            self.is_winning(im_winning=winning)
            self.play_again()

    def play_again(self):
        user_answer = input("Would you like to play again? (y/n): \n".lower())
        user_play_again = True
        while user_play_again:
            if user_answer == "y":
                self.load_game()
            elif user_answer == "n":
                print("Good bye!")
                quit()
            else:
                print("Invalid answer, please try again.")
                continue

    def is_winning(self, im_winning):
        if im_winning:
            add_score(name=self.username, difficulty=self.game_difficulty)
        else:
            self.game_difficulty = 0
            add_score(name=self.username, difficulty=self.game_difficulty)