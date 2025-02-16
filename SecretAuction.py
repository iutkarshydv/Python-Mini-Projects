logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
import os
bidders={}
def add_bidder(name,amount):
    bidders[name]=amount

status="yes"
print(logo)
print("Welcome to Secret Auction")
while not status=="no":

    bidder_name=input("Enter Your Name: ")
    bidder_amount=input("Enter your bid amount: ")
    add_bidder(bidder_name,bidder_amount)
    status=input("Is there any other person in room? ").lower()
    os.system('CLS')
    print(logo)


highest=0
for bidder in bidders:
    bid_amount = int(bidders[bidder])
    if bid_amount > highest:
        highest=bid_amount
        winner = bidder

print(f"{winner} is the highest bidder with ${highest} bidding amount.")

