import random
def main():
    print("\nGuess My Number")

    secret_number = random.randint(0, 99)
    print("\nI am thinking of a number between 0 and 99...")

    guess_number = int(input("Enter a guess: "))

    while guess_number != secret_number:
        if guess_number < secret_number:
            print("\nYour guess is too low")
        else:
            print("\nYour guess is too high")

        print()
        guess_number = int(input("Enter a new guess: "))

    print("\nCongrats! The number was: " + str(secret_number))
    

if __name__ == '__main__':
    main()