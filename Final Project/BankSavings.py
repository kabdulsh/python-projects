#prompt user for starting balance of each type.
#years_until_retirement = desired_retirement_age - age

import matplotlib.pyplot as plt

class BankSavings:

    def __init__(self):
        self.bank_balance = 0
        self.bank_balance_after_each_year = []

    def get_starting_balance(self):
        self.bank_balance = int(input("Initial amount of money in bank savings:\n"))

    def apply_return_on_investment(self):
        self.bank_balance = self.bank_balance + (self.bank_balance * 0.02)

    def write_balance_to_file(self, balance):
        bank_balance_file = open("bank_balance.txt", "a")
        bank_balance_file.write("{}\n" .format(balance))
        bank_balance_file.close()

        self.bank_balance_after_each_year.append(balance)

    def plot(self, age, desired_retirement_age):

        years = range(age, desired_retirement_age)
        plt.plot(years, self.bank_balance_after_each_year)
        plt.show()