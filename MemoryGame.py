import random
from threading import Timer
from os import system, name


# Would this clear the prompt??
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


class MemoryGame:
    def __init__(self):
        self.number_list = []
        self.user_list = []
        self.is_winning = bool

    def generate_sequence(self, difficulty):
        self.number_list = [random.randrange(1, 101) for _ in range(difficulty)]
        print(f"Try and remember these : {(' '.join(map(str, self.number_list)))}")
        t = Timer(difficulty, clear)
        t.start()

    def get_list_from_user(self, difficulty):
        testing_list_len = True
        while testing_list_len:
            self.user_list = input(
                "Try enter the list by memory. Please use just numbers and spaces. example: (22 1 6 2):\n").split()
            try:
                self.user_list = [int(i) for i in self.user_list]
            except ValueError:
                print("Sorry, please enter valid numbers only.")
                continue
            else:
                if len(self.user_list) > difficulty:
                    print("Sorry, you have guessed too many numbers. Try again.")
                    continue
                elif len(self.user_list) < difficulty:
                    print("Sorry, you haven't guessed enough numbers. Try again.")
                    continue
                else:
                    testing_list_len = False

    def is_list_equal(self, number_list, user_list):
        if user_list == number_list:
            print("Good job, you've guessed correctly!")
            self.is_winning = True
        else:
            print("Sorry you are wrong.")
            self.is_winning = False

    def play(self, difficulty):
        self.generate_sequence(difficulty=difficulty)
        self.get_list_from_user(difficulty=difficulty)
        self.is_list_equal(number_list=self.number_list, user_list=self.user_list)
        return self.is_winning
