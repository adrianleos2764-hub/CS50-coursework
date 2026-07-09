#  program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not.
def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if  len(s) in range(2, 7) and s[0:2].isalpha and s.isalnum(): #checks for minium and maxium character then fool proofs punctuation and spaces
        pass
    else:
        return False
    character_number = None #prepares documentation for first number
    for index, char in enumerate(s[2:6]): #returns index number and character of our first number
        if char.isdigit() and char == '0': # if character is a number digit and is 0 return false
            return False
        elif char.isdigit():
            character_number = index + 2 #stores index but +2 as enumerate creates new number sequence in our slice
        break
    for str in s[character_number:]:
        if str.isalpha(): #if any letter follows a number return false
            return False
    return True #if all conditions pass without returning false it is valid returning true.
    
        
  
        

        

            

        

    
    
    
    
    


main()