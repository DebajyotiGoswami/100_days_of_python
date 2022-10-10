from os import system
from blind_auction_logo import logo
#HINT: You can call clear() to clear the output in the console.

def highest_bidder(bid):
    max_bid = -9999
    max_bidder = ""
    for key , value in bid.items():
        if value >= max_bid:
            max_bidder = key
            max_bid = value
    print(f"{max_bidder} is the highest bidder with bid amount {max_bid}")
bid = {}

bidding_finished = False
while not bidding_finished:
    _ = system("cls")
    print(logo)
    name = input("What is your name ? ")
    price = int(input("What is your bid amount ? $"))
    bid[name] = price

    continue_choice = input("Is there any other bidder ? 'yes' / 'no' ? ")
    if continue_choice == 'no':
        bidding_finished = True
        highest_bidder(bid)
    elif continue_choice == 'yes':
        _ = system("cls")
    else:
        continue_choice = input("Is there any other bidder ? 'yes' / 'no' ? ")
