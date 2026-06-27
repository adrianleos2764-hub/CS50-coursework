#program canculates for a tip amount based on bill and tip percentage
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    return float(d.replace("$", "")) #returns it in float fomat replacing the $ sign with nothing so it can be converted to float
    


def percent_to_float(p):
    return float(p.replace("%", "")) / 100 #returns it in float format removing the % sign and dividing by 100 to get decimal to canculate in main function
    


main()