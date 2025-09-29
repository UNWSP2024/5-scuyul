#Math Tester by Griffin Corniea 9.29.25
import random
def main():
    num1 = (random.randint(1, 999))
    num2 = (random.randint(1, 999))

    print(" " + str(num1))
    print("+" + str(num2))
    print("------")

    #wait for key press
    answer = input("Answer: ")
    print("")

    if answer == str((num1 + num2)):
        print("Correct, Great Job!")
    else:
        print("Incorrect the correct answer was: " + str((num1 + num2)))

if __name__ == "__main__":
    main()