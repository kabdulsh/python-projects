#prompt user for starting balance of each type.
#years_until_retirement = desired_retirement_age - age

import matplotlib.pyplot as plt

class Mattress:

    def __init__(self):
        self.mattress_balance = 0
        self.mattress_balance_after_each_year = []

    def get_starting_balance(self):
        self.mattress_balance = int(input("Initial amount of money under mattress:\n"))

    def write_balance_to_file(self, balance):
        mattress_balance_file = open("mattress_balance.txt", "a")
        mattress_balance_file.write("{}\n" .format(balance))
        mattress_balance_file.close()

        self.mattress_balance_after_each_year.append(balance)

    def plot(self, age, desired_retirement_age ):

        years = range(age, desired_retirement_age)
        plt.plot(years, self.mattress_balance_after_each_year)
        plt.show()