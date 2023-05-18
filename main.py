def main():

    try:

      miles_entered = float(input("Please enter the number of miles driven: "))

      miles_to_kilometers(miles_entered)

    except:

      print("Invalid entry, please enter a valid number and try again.")

      print()

      main()

def miles_to_kilometers(miles_entered):

  kilometers = miles_entered * 1.60934

  print(f"This converts {miles_entered} miles to {kilometers} kilometers.")

main()

print()

print(input("Please press ENTER to exit the program:"))