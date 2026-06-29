#program ask user for input based on time of day and responds what to eat based on the input in 24 hour format
def main():
    clock = input("What time is it?: ")
    clock = convert(clock)
    if 7 <= clock <= 8:
        print("You should eat breakfast.")
    elif 12 <= clock <= 13:
        print("You should eat lunch.")
    elif 18 <= clock <= 19:
        print("You should eat dinner.")
    else:
        print("You should not eat right now.")


def convert(time):
    # converts time to float to future check it against time ranges
    hours, minutes = time.split(":") #splits the input into two parts based off expected format of time
    hours = float(hours) * 60 #converts hours to minutes for final calculation conversion
    minutes = float(minutes)
    time = (hours + minutes) / 60 #converts for hours and minutes in a float format
    return time # returns the time in new format for comparison in main function

main()