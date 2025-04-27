AFFIRMATION: str = "I am capable of doing anything I put my mind to."

# ANSI escape codes
BLUE = "\033[94m"
RESET = "\033[0m"

def main():
    print(f"\nPlease type the following affirmation: {AFFIRMATION}")

    print(BLUE, end="")        
    user_input = input()
    print(RESET, end="")        

    while user_input != AFFIRMATION:
        print("\nThat was not the affirmation.")

        print(f"\nPlease type the following affirmation: {AFFIRMATION}")
        
        print(BLUE, end="")     
        user_input = input()
        print(RESET, end="")    

    print("That's right! :)")

if __name__ == '__main__':
    main()
