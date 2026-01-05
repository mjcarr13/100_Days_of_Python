def blind_auction():
    name = input("What is your name?\n")
    bid = input("How much do you want to bid?\n")
    bids[name] = bid

bids = {}
auction_running = True
import art
print(art.logo)
while auction_running:
    blind_auction()
    restart = input("Are there any more bidders? Type 'yes' or 'no'").lower()
    print("\n" * 100)
    if restart == "no":
        auction_running = False
        winner = max(bids, key=bids.get)
        print(f"The winnner is {winner} with a winning bid of ${bids[winner]}")



