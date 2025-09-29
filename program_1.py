#Kilometer to Mile by Griffin Corniea 9.29.25
def kilometer_conversion(kilometers):
    miles = kilometers * 0.6214


    return miles

### I think i have to put in the input logic
if __name__ == '__main__':
    kilometers = float(input("How many kilometers: "))
    miles = kilometer_conversion(kilometers)
    print("Miles:", miles)