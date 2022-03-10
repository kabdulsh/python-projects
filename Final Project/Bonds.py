#prompt user for starting balance of each type.
#years_until_retirement = desired_retirement_age - age

import matplotlib.pyplot as plt

class Bonds:

    def __init__(self):
        self.bond_balance = 0
        self.return_on_bonds = []
        self.bond_balance_after_each_year = []

        with open("bonds.txt") as rates_of_return:
            for rate in rates_of_return:
                self.return_on_bonds.append(float(rate))

    def get_starting_balance(self):
        self.bond_balance = int(input("Initial amount of money in bonds:\n"))

    def apply_return_on_investment(self, year):
        self.bond_balance = self.bond_balance + (self.bond_balance * self.return_on_bonds[year])

    def write_balance_to_file(self, balance):
        bond_balance_file = open("bond_balance.txt", "a")
        bond_balance_file.write("{}\n" .format(balance))
        bond_balance_file.close()

        self.bond_balance_after_each_year.append(balance)

    def plot(self, age, desired_retirement_age):

        years = range(age, desired_retirement_age)
        plt.plot(years, self.bond_balance_after_each_year)
        plt.show()