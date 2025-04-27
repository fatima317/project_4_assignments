BOLD_ITALIC = "\033[1;3m"
RESET = "\033[0m"

def main():
    
    print("\nPlease enter an integer to be divided: ", end="")
    print(BOLD_ITALIC, end="")
    number1 = int(input())
    print(RESET, end="")
    
    print("\nPlease enter an integer to divide by: ", end="")
    print(BOLD_ITALIC, end="")
    number2 = int(input())
    print(RESET, end="")
    

    division = number1 // number2 
    remainder = number1 % number2

    print(f"\nThe result of this division is {division} with a remainder of {remainder}")


if __name__ == '__main__':
    main()