#program prompts user for text then outputs it with vowels taken out!
short_version = input("Insert your desired word: ")
if short_version != str:
   print("Please insert a word!")
vowels = ["A", "a", "I", "i", "O", "o", "U", "u", "E", "e"]
for char in short_version:
    if char in vowels:
     short_version = short_version.replace(char, "")
print(short_version)
  
        


        

