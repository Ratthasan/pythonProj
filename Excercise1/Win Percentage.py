'''Create a function called win_percentage() that takes two parameters named wins and losses.

This function should return out the total percentage of games won by a team based on these two numbers.

Hint
In order to calculate the ratio of wins out of total games we can use wins / (wins + losses) where wins + losses is equal to the total number of games. To convert that value to a percentage, multiply it by 100.'''

def win_percentage(wins,losses):
    total =wins+losses
    return (wins*100/total)


print(win_percentage(5,6))