print('''Tax Year: 2017
Filing Status: Married filing jointly''')

print('')

income = ''

while income != '-1':
    income = float(input('Enter Taxable Income (or -1 to quit): '))

    print('')

    tax10 = 0
    tax15 = 0
    tax25 = 0
    tax28 = 0
    tax33 = 0
    tax35 = 0
    tax39 = 0

    if income < 0:
        break
    if income >= 0:
        if income < 18650:
            tax10 = income * 0.1
            print('Taxes owed at 10%%: $%.0f' % tax10)
        else:
            tax10 = 18650 * 0.1
            print('Taxes owed at 10%%: $%.0f' % tax10)
    if income >= 18650:
        if income < 75900:
            tax15 = ((income - 18650) * 0.15)
            print('Taxes owed at 15%%: $%.0f' % tax15)
        else:
            tax15 = (75900 - 18650) * 0.15
            print('Taxes owed at 15%%: $%.0f' % tax15)
    if income >= 75900:
        if income < 153100:
            tax25 = ((income - 75900) * 0.25)
            print('Taxes owed at 25%%: $%.0f' % tax25)
        else:
            tax25 = ((153100 - 75900) * 0.25)
            print('Taxes owed at 25%%: $%.0f' % tax25)
    if income >= 153100:
        if income < 233350:
            tax28 = ((income - 153100) * 0.28)
            print('Taxes owed at 28%%: $%.0f' % tax28)
        else:
            tax28 = ((233350 - 153100) * 0.28)
            print('Taxes owed at 28%%: $%.0f' % tax28)
    if income >= 233350:
        if income < 416700:
            tax33 = ((income - 233350) * 0.33)
            print('Taxes owed at 33%%: $%.0f' % tax33)
        else:
            tax33 = ((416700 - 233350) * 0.33)
            print('Taxes owed at 33%%: $%.0f' % tax33)
    if income >= 416700:
        if income < 470700:
            tax35 = ((income - 416700) * 0.35)
            print('Taxes owed at 35%%: $%.0f' % tax35)
        else:
            tax35 = ((470700 - 416700) * 0.35)
            print('Taxes owed at 35%%: $%.0f' % tax35)
    if income >= 470700:
        tax39 = ((income - 470700) * 0.396)
        print('Taxes owed at 39.6%%: $%.0f' % tax39)

    total_tax = tax10 + tax15 + tax25 + tax28 + tax33 + tax35 + tax39

    print('')

    print('Total taxes owed: $%.2f' % total_tax)

    print('')

    tax_percent_of_income = (total_tax / income) * 100
    print('Taxes as a percentage of Gross Income: %.2f%%\n' % tax_percent_of_income)