import os

from art import logo
print(logo)
continued = True
bids = {}


def find_the_highest_bidder(bids_records):
    highest_bid = 0
    winner = ""
    for bidder in bids_records:
        value = bids_records[bidder]
        if value > highest_bid:
            winner = bidder
            highest_bid = value
    print(f"the winner is: {winner} & the price was {highest_bid}")


while continued:
    name=input("What is your name? ")
    price=int(input("What is your bid?: $"))
    bids[name]=price
    continued=input("Are there any more bidders? Type 'yes' or 'no' ")
    if continued == 'no':
        continued = False
        find_the_highest_bidder(bids)
