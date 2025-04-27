BOLD_ITALIC = "\033[1;3m"
RESET = "\033[0m"
def main():
    
    print("Type a number to see its square: ", end="")
    print(BOLD_ITALIC, end="")
    number = float(input())
    print(RESET, end="")
    
    square = number ** 2

    print(f"{number} squared is {square}.")

if __name__ == '__main__':
    main()