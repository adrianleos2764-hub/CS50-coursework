# program prints "money" out based on user greeting 
greeting = input("Greeting: ")
if "hello" in greeting.lower(): # if hello is in the users input prints $0
    print("$0")
elif greeting.lower().startswith("h"): #if it starts with h prints $20
    print("$20")
else: #if message does not have hello in it or does not start with h prints $100
    print("$100")