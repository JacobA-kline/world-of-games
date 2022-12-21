import random


class GuessGame:
    def __init__(self):
        self.secret_number = int
        self.user_guess = int
        self.is_winning = bool

    def welcome(self):
        print("Welcome to the Guess Game.")

    def generate_number(self, number):
        self.secret_number = random.randint(1, number)
        return self.secret_number

    def get_guess_from_user(self, difficulty):
        self.user_guess = int(input(f"Please guess a number from 1 - {difficulty}:\n"))
        return self.user_guess

    def compare_results(self, secret, guess):
        if secret == guess:
            print(f"You've guessed correctly! The number is {secret}.")
            self.is_winning = True
        else:
            print(f"You are wrong! The number is {secret}.")
            self.is_winning = False

    def play(self, difficulty):
        self.generate_number(number=difficulty)
        self.get_guess_from_user(difficulty=difficulty)
        self.compare_results(secret=self.secret_number, guess=self.user_guess)
        return self.is_winning
