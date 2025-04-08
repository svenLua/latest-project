# Hello F R I E N D S!
# Today we are using dictionaries
# {} key: value pairs
# this is the simplest way I could think of
# you can make it easy by looping over each bidder too, but that seems unnecessary and uses the 
# max method which we havent gone through yet.

#Get the key with the highest value
#highest_score = max(bid_list, key=bid_list.get)

#Print the key-value pair with the highest value
#print(highest_score, bid_list[highest_score])

import os

bid_list = {}
top_bid = 0
top_name = "none"

while True:
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n"))
    bid_list[name] = bid
    if bid > top_bid:
        top_bid = bid
        top_name = name
    os.system('cls')
    quit = input("Are there more bidders? If yes, type 'y', otherwise type 'q'")
    if quit == 'q':
        print(f"The highest bidder is: {top_name} with a bid of ${top_bid}")
        break
    else:
        continue