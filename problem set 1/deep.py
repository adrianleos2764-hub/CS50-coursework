# program ask question of life outputs yes to correct answer otherwise outputting no
question = input("What is the answer to life, the universe, and everything? ")
if question == "42" or question == "forty-two" or question == "forty two":
    print("Yes") #if question results in one of these print yes
else: # if the answer is anything else print no!
    print("No")