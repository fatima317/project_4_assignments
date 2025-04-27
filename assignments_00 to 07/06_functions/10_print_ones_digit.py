BLUE = "\033[94m"
RESET = "\033[0m"

def print_ones_digit(num:int):
    ones_digit = num % 10
    print("The ones digit is", ones_digit)

def main():
    
    print("Enter a number: ", end="")
    print(BLUE, end="")
    num = int(input())
    print(RESET, end="")

    print_ones_digit(num)

if __name__ == '__main__':
    main()
