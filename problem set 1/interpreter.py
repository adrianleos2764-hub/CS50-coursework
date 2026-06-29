# program lets user to do math based on user input
math = input("enter equation: ")
x, y, z = math.split(" ") #splits the input into three parts based off expected format of equation
x = int(x)
z = int(z)
if y == "+":
    print(float(x + z))
elif y == "-":
    print(float(x - z))
elif y == "*":
    print(float(x * z))
elif y == "/":
    print(float(x / z))
elif y == "%":
    print(float(x % z))
elif y == "**":
    print(float(x ** z))
else: #in case of unexpected wrongly formatted input, the program will print this message
    print("Sorry, I dont understand this format or formula.")
