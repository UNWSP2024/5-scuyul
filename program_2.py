#Math Tester by Griffin Corniea 9.29.25
import random
def main():
    num1 = (random.randint(1, 999))
    num2 = (random.randint(1, 999))

    print(" " + str(num1))
    print("+" + str(num2))
    print("------")

    #wait for key press
    input("Press enter to see answer...")
    print("")
    print("the answer is: " + str(num1 + num2))

if __name__ == "__main__":
    main()