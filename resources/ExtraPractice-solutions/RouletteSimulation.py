'''
# American Roulette
## ref: https://www.roulettestar.com/guide/probability/

Bet Type                Fraction    Ratio       Percentage
----------------------------------------------------------
Even (e.g. Red/Black)   1/2.11      1.11 to 1   47.4%
Column                  1/3.16      2.16 to 1   31.6%
Dozen                   1/3.16      2.16 to 1   31.6%
Six Line                1/6.33      5.33 to 1   15.8%
Corner                  1/9.50      8.50 to 1   10.5%
Street                  1/12.67     11.67 to 1  7.9%
Split                   1/19.00     18.00 to 1  5.3%
Straight                1/38.00     37.00 to 1  2.6%
'''
import random

def isWin() -> bool:
    '''
    Play a single game.
    :return: True, if WIN; otherwise, False.
    '''
    num = random.uniform(0, 100)
    return num <= 47.4

def play(money) -> float:
    '''
    Simulate a single Game with initial money.
    :param float money: Amount of money that was brought to the game
    :return: Amount of money after the game.
    '''
    if isWin():
        return round(money * 1.11, 2)
    else:
        return 0

def simulate(money, n=100) -> tuple[float, float]:
    '''
    Simulate a night of gambling in Roulette
    :param float money: Amount of money that was brought to the game
    :param int n: Number of Trials you play the game
    :return: Amount of money after the night.
    '''
    total = money
    for i in range(n):
        keeped = total * 0.4 # Everytime you keep half of the money
        total = keeped + play(total-keeped)
    total = round(total, 2)
    return total

def isGain(left, origin) -> bool:
    '''
    :return: True if Gained; otherwise, False.
    '''
    return left >= origin

def casinoSimulate(customers):
    '''
    Simulate a night of operating a Casino
    :param int customers: Number of customers over a night
    :return: Amount of money after the night.
    '''
    totalMoney = 0
    totalGain = 0
    totalEarned = 0
    winedCustomer = 0
    for i in range(1, customers+1):
        money = random.randint(50, 500)
        turns = random.randint(1, 20)
        left = simulate(money, turns)
        totalMoney += money
        totalGain += round(left - money, 2)
        earned = round(money - left, 2)
        totalEarned += earned

        print("="*50)
        print("Customer #"+str(i), "brings $", money, "and played", turns)
        print("Customer #"+str(i), "left $", left)
        print("We earned $", earned)
        if not isGain(left, money):
            print("Customer #"+str(i), "learned a lesson from Roulette")
        else:
            print("Customer #"+str(i), "dominates the Roulette")
            winedCustomer += 1
        print()

    print("="*50)
    totalEarned = round(totalEarned, 2)
    totalGain = round(totalGain, 2)
    avgGain = round(totalGain/customers, 2)
    print("Customers Total:\t$", totalMoney)
    print("Customers Net Gain:\t$", totalGain)
    print("Customers AVG Gain:\t$", avgGain)
    print('-'*50)
    print("Casino Net Gain:\t$", totalEarned)

    print()
    print("Total Customers: ", customers)
    print("ONLY", winedCustomer, "Customers Gained from Roulette")
    print("Probability of Gain:\t", round(winedCustomer/customers*100,2), "%")

casinoSimulate(1000)




