import random

class Powerball:

    ticket_cost = 2

    def __init__(self):

        self.white_balls = random.sample(range(1, 70), 5)
        self.red_ball = random.randint(1, 26)

    def get_winnings(self, winning_ticket):

        number_white_matches = 0

        for any_white_ball in self.white_balls:
            if any_white_ball in winning_ticket.white_balls:
                number_white_matches = number_white_matches + 1

        red_match = self.red_ball == winning_ticket.red_ball

        # Why doesn't the following code work properly instead of the 20th line?

        # red_match = 0

        # for the_red_ball in self.red_ball:
            # if the_red_ball in winning_ticket.red_ball:
                # red_match = red_match + 1

        amount_won = 0

        if red_match == 1:
            amount_won = 4
        elif number_white_matches == 1 and red_match == 1:
            amount_won = 4
        elif number_white_matches == 2 and red_match == 1:
            amount_won = 7
        elif number_white_matches == 3:
            amount_won = 7
        elif number_white_matches == 3 and red_match == 1:
            amount_won = 100
        elif number_white_matches == 4:
            amount_won = 100
        elif number_white_matches == 4 and red_match == 1:
            amount_won = 50000
        elif number_white_matches == 5:
            amount_won = 1000000
        elif number_white_matches == 5 and red_match == 1:
            amount_won = 40000000

        return amount_won

total_money_spent = 0
total_amount_won = 0
desired_amount_tickets = -1

while desired_amount_tickets != 0:
    desired_amount_tickets = int(input("How many tickets would you like to buy?\n"))
    if desired_amount_tickets == 0:
        break
    winning_ticket = Powerball()
    total_money_spent = total_money_spent + (desired_amount_tickets * Powerball.ticket_cost)
    for ticket in range(desired_amount_tickets):
        actual_ticket_bought = Powerball()
        total_amount_won = total_amount_won + (actual_ticket_bought.get_winnings(winning_ticket))
    print("The total amount of money spent on Powerball is ${}." .format(total_money_spent))
    print("The total amount of money won from Powerball is ${}." .format(total_amount_won))
    print("The net amount of money gained from Powerball is ${}!\n" .format(total_amount_won - total_money_spent))

    total_money_spent = 0
    total_amount_won = 0