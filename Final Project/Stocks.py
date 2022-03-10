#prompt user for starting balance of each type.
#years_until_retirement = desired_retirement_age - age

import matplotlib.pyplot as plt

class Stocks:

    def __init__(self):
        self.stocks_balance = 0
        self.return_on_stocks = []
        self.stocks_balance_after_each_year = []

        with open("stocks.txt") as rates_of_return:
            for rate in rates_of_return:
                self.return_on_stocks.append(float(rate))

    def get_starting_balance(self):
        self.stocks_balance = int(input("Initial amount of money in stocks:\n"))

    def apply_return_on_investment(self, year):
        self.stocks_balance = self.stocks_balance + (self.stocks_balance * self.return_on_stocks[year])

    def write_balance_to_file(self, balance):
        stocks_balance_file = open("stocks_balance.txt", "a")
        stocks_balance_file.write("{}\n" .format(balance))
        stocks_balance_file.close()

        self.stocks_balance_after_each_year.append(balance)

    def plot(self, age, desired_retirement_age):
        years = range(age, desired_retirement_age)
        plt.plot(years, self.stocks_balance_after_each_year)
        plt.show()