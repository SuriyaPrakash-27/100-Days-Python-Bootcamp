import gavel_art
import os

print(gavel_art.logo)

print('Welcome to the Secret Auction Program')

bids = {}
def auction(entry_name,entry_bid):

    bids[entry_name] = entry_bid

other_bidder = 'yes'

while other_bidder == 'yes':
    name = input('What is your name?\n')
    bid_value = int(input('What\'s your bid?\n'))
    auction(name, bid_value)
    other_bidder = input("Are there any other bidders? Type 'yes' or 'no'\n")
    os.system("cls")

winner_name = ''
winner_value = 0

for key in bids:
    if bids[key] > winner_value:
        winner_value = bids[key]
        winner_name = key

print(f'The winner is {winner_name} with a bid of ${winner_value}')


