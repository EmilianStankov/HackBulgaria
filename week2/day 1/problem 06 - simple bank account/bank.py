balance = 0

def get_balance():
    global balance
    return balance


def deposit_money(amount):
    if amount < 0:
        return False
    else:
        global balance
        balance += amount


def withdraw_money(amount):
    if amount > get_balance() or amount < 0:
        return False
    else:
        global balance
        balance -= amount
