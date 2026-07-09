# program converts camel case to snake_case
conversion = input("Enter variable name in camel case: ")
#convert to snake case
for letter in conversion:
    if letter.isupper():
        conversion = conversion.replace(letter, "_" + letter.lower())
print(conversion)


