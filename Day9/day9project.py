import os
os.system("cls")

def workOutWinner(bidders):
    highestBid = 0
    highestBidder = ""

    for key in bidders:
        if bidders[key] > highestBid:
            highestBid = bidders[key]
            highestBidder = key

    print(f"{highestBidder} is the highest bidder with a bid of ${highestBid}")


def collectBids():

    moreBidders = True
    bidders = {}
    while moreBidders:
        name = input("What is the name of the bidder? \n")
        bid = int(input("How much do you want to bid? \n$"))
        bidders[name] = bid
        carryOn = input("Are there anymore bidders? (yes) (no)\n").lower()
        if carryOn == "yes":
            os.system("cls")
        else:
            moreBidders = False
            workOutWinner(bidders)

