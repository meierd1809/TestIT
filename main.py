def main():

    try:

      miles = float(input("Please enter the number of miles driven: "))

      miles_to_kilometers(miles)

    except:

      print("Invalid entry, please enter a valid number and try again.")

      print()

      main()

def miles_to_kilometers(miles):

  kilometers = miles * 1.60934

  print(f"This converts {miles} miles to {kilometers} kilometers.")

main()

print()

print(input("Please press ENTER to exit the program:"))