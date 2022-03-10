from Mattress import *
from BankSavings import *
from Bonds import *
from Stocks import *


class RetirementCalculator:

    def __init__(self):

        self.account1 = Mattress()
        self.account1.get_starting_balance()

        self.account2 = BankSavings()
        self.account2.get_starting_balance()

        self.account3 = Bonds()
        self.account3.get_starting_balance()

        self.account4 = Stocks()
        self.account4.get_starting_balance()

    # for each year until retirement allow the user to invest more money is any/all of their accounts

    def menu(self):

        choice = ""
        choices = ["A", "B", "C", "D", "E"]
        while choice not in choices:
            print("""\na) Mattress\nb) Bank Savings\nc) Bonds\nd) Stocks\ne) NONE\n""")
            choice = input().upper()
        return choice

    def get_total_balance(self):

        self.total = self.account1.mattress_balance + self.account2.bank_balance + self.account3.bond_balance + self.account4.stocks_balance

        return self.total

    def invest_more_money(self, age, desired_retirement_age):

        self.years_until_retirement = desired_retirement_age - age

        file = open("total_balance.txt", "w")
        file.write("MATTRESS | BANK SAVINGS | BONDS | STOCKS | TOTAL\n")
        file.close()

        mattress_balance_file = open("mattress_balance.txt", "w")
        bank_balance_file = open("bank_balance.txt", "w")
        bond_balance_file = open("bond_balance.txt", "w")
        stocks_balance_file = open("stocks_balance.txt", "w")


        for year in range(self.years_until_retirement):

            self.account2.apply_return_on_investment()
            self.account3.apply_return_on_investment(year)
            self.account4.apply_return_on_investment(year)

            answer = input("T minus {} years: Are you willing to add money to any of your accounts?\n" .format(self.years_until_retirement - year)).upper()

            while answer != "NO":
                choice = self.menu().upper()
                if choice == "A":
                    amount = int(input("How much money would you like to add under the mattress?\n"))
                    self.account1.mattress_balance =  self.account1.mattress_balance + amount
                if choice == "B":
                    amount = int(input("How much money would you like to invest into your bank savings?\n"))
                    self.account2.bank_balance = self.account2.bank_balance + amount
                if choice == "C":
                    amount = int(input("How much money would you like to invest into bonds?\n"))
                    self.account3.bond_balance = self.account3.bond_balance + amount
                if choice == "D":
                    amount = int(input("How much money would you like to invest into stocks?\n"))
                    self.account4.stocks_balance = self.account4.stocks_balance + amount
                if choice == "E":
                    break

            # display current balance ( having accounted for return on investment )
            print("MATTRESS - Your current balance is ${:.2f}" .format(self.account1.mattress_balance))
            print("BANK SAVINGS - Your current balance is ${:.2f}".format(self.account2.bank_balance))
            print("BONDS - Your current balance is ${:.2f}".format(self.account3.bond_balance))
            print("STOCKS - Your current balance is ${:.2f}".format(self.account4.stocks_balance))
            print("---------------------------------------------------------------------------------------------------")
            print("TOTAL - Your current balance is ${:.2f}\n" .format(self.get_total_balance()))

            file = open("total_balance.txt", "a")
            file.write("{:.2f} | {:.2f} | {:.2f} | {:.2f} | {:.2f}\n".format(self.account1.mattress_balance, self.account2.bank_balance, self.account3.bond_balance, self.account4.stocks_balance, self.total))
            file.close()

            self.account1.write_balance_to_file(self.account1.mattress_balance)
            self.account2.write_balance_to_file(self.account2.bank_balance)
            self.account3.write_balance_to_file(self.account3.bond_balance)
            self.account4.write_balance_to_file(self.account4.stocks_balance)

    def check_goal(self, desired_retirement_savings, desired_retirement_age):

        print("At {} years of age,\n" .format(desired_retirement_age))
        print("     MATTRESS - Your total balance is ${:.2f}".format(self.account1.mattress_balance))
        print("     BANK SAVINGS - Your total balance is ${:.2f}".format(self.account2.bank_balance))
        print("     BONDS - Your total balance is ${:.2f}".format(self.account3.bond_balance))
        print("     STOCKS - Your total balance is ${:.2f}".format(self.account4.stocks_balance))
        print("---------------------------------------------------------------------------------------------------")
        print("     TOTAL - Your total balance is ${:.2f}\n".format(self.get_total_balance()))

        print("Your total balance adjusted for inflation is ${:.2f}\n" .format(self.total / (1.03** self.years_until_retirement)))

        if self.total >= desired_retirement_savings:
            print("Yay! You hit your target savings.")
        else:
            print("Ouch! You did not hit your target savings.")

# Prompt use for age, desired retirement age, desired retirement savings


age = int(input("Age:\n"))
desired_retirement_age = int(input("Desired retirement age:\n"))
desired_retirement_savings = int(input("Desired retirement savings:\n"))

calculator = RetirementCalculator()
calculator.invest_more_money(age, desired_retirement_age)
calculator.check_goal(desired_retirement_savings, desired_retirement_age)

calculator.account1.plot(age, desired_retirement_age)
calculator.account2.plot(age, desired_retirement_age)
calculator.account3.plot(age, desired_retirement_age)
calculator.account4.plot(age, desired_retirement_age)