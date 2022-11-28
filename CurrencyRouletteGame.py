import random
from forex_python.converter import CurrencyRates


# Current Currency rates are set to INR. ISR is currently not available in forex_python
class CurrencyRouletteGame:
    def __init__(self):
        self.from_currency_kind = 'INR'
        self.to_currency_kind = 'USD'
        self.random_num = int
        self.conversion = int
        self.user_guess = int
        self.interval1 = int
        self.interval2 = int
        self.is_winning = bool

    def get_money_interval(self, difficulty):
        c = CurrencyRates()
        self.random_num = random.randint(difficulty * 10, difficulty * 15)
        self.conversion = c.convert(self.to_currency_kind, self.from_currency_kind, self.random_num)
        self.conversion = round(self.conversion)
        self.interval1 = (self.conversion - (5 - difficulty))
        self.interval2 = (self.conversion + (5 - difficulty))

    def get_guess_from_user(self, first_interval, second_interval):
        checking_user_input = True
        while checking_user_input:
            try:
                user_guess = int(input(
                    f"Please guess how much is {self.random_num} {self.to_currency_kind} in {self.from_currency_kind}.\n"))
            except ValueError:
                print("please enter numbers only.")
                continue
            else:
                if first_interval <= user_guess <= second_interval:
                    print("Correct")
                    self.is_winning = True
                else:
                    print("You have guessed wrong")
                    self.is_winning = False
            finally:
                checking_user_input = False

    def play(self, difficulty):
        self.get_money_interval(difficulty=difficulty)
        self.get_guess_from_user(first_interval=self.interval1, second_interval=self.interval2)
        return self.is_winning
