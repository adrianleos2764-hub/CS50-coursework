# takes desired user input and "slows it down" by adding 3 dots inbetween each word
response = input("whats the source? ") #ask the user for a source to slow down
print(response.replace(" ", "...")) # prints the response with 3 dots inbetween each word