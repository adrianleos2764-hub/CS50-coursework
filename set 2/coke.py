#program takes user input in coins for 50 cents for a coke bottle also prints out change due
def main():
    due = 50 #a starting point used to also manipulate later
    print("Amount due: " + str(due)) # Displays amount owed to get a coke.
    money = input("Insert coin: ")
    if int(money) in (5,10,25): #if money is equal to these numbers subtract it from due 
         due = due - int(money)
         print("Sucess!") # prints sucess in sense of users payment worked.
    else:
         print("Please insert valid coin!(5,10,25)")
    while due > 1: #loop repeating a payment loop until no more is due
          print("Amount due: " + str(due)) # Displays amount owed to get a coke.
          money = input("Insert coin: ")
          if int(money) in (5,10,25):
               due = due - int(money) 
               
          else:
               print("Please insert valid coin(5,10,25)")
    if due ==  0: #measures for complete payment 
        print("Enjoy your coke!")
    elif due < 0: #if overpaid owe change to user and give the coke
        print("Change Owed: " + str(abs(due)) + "\n"  "Enjoy your coke!")
main()
          
         





   

    

