# program ask for mass and prints equivalent energy based off eintsteins equation E=mc^2 (approximation of  300000000 joules)
def main():
    M =int(input("Enter mass in kilograms: "))
    E = M * 300000000 ** 2
    print (str(E))


main()