MIN_DEPOSIT = 10
MIN_BET = 5
MIN_LINES = 1
MAX_LINES = 3


def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount < MIN_DEPOSIT:
                print(
                    f"Minimum bet is ${MIN_DEPOSIT}. Please enter a valid amount.")
            else:
                print(f"You deposited ${amount}.")
                return amount

        else:
            print("Please enter a valid number.")


def funct_calls():
    amount = deposit()
    lines_choose = lines_betting()
    lines = main_depo()
    total_amount = amount * lines_choose
    print(
        f"You are betting ${amount} on {lines_choose} lines. Total bet: ${total_amount}.")
    if total_amount > amount:
        print(
            f"You do not have enough funds to make this bet.Your balance is ${amount}")


def lines_betting():
    while True:
        lines_choose = input("How many lines would you like to bet on ? ")
        if lines_choose.isdigit():
            lines_choose = int(lines_choose)
            if lines_choose < MIN_LINES or lines_choose > MAX_LINES:
                print(
                    f"Please enter a valid number of lines ({MIN_LINES}-{MAX_LINES}).")
            else:
                print(f"You chose to bet on {lines_choose} lines.")
                return lines_choose
        else:
            print("Please enter a valid number.")


def main_depo():
    while True:
        line_bet = input("How much would you like to bet on each line? $")
        if line_bet.isdigit():
            line_bet = int(line_bet)
            if line_bet < MIN_BET:
                print(
                    f"Minimum bet per line is ${MIN_BET}. Please enter a valid amount.")
            else:
                print(f"You are betting ${line_bet} on each line.")
                return line_bet
        else:
            print("Please enter a valid number.")


funct_calls()
