#functions go here

# checks unput is a number more than zero
from wsgiref import headers


def num_check(question):
    valid = False
    while not valid:

        error = "Please enter a number that is more than zero"

        try:

            response = float(input(question))

            if response > 0:
                return response
            
            else:
                print(error)
                print ()

        except ValueError:
            print(error)

# Main Routine goes here

# Introduction ?/ Heading print statements
print()
print("**** Area Perimeter Calculator*****")
print()

keep_going = ""
while keep_going == "":

    width = num_check("Width: ")
    height = num_check("Height: ")

    # Calculate area (width x height)
    area = width * height

    # Calculate perimeter (width + height) x 2
    perimeter = 2 * (width + height)

    # Output area and perimeter tp 2dp
    print("Perimeter: {:.2f} units".format(perimeter))
    print("Area: {:.2f} square units".format(area))
    print()
    keep_going = input("Press <enter> to keep going or any key to quit")

print ()
print("Thanks for using the area / perimeter calculator")





