BLUE = "\033[94m"
RESET = "\033[0m"

def print_multiple(message:str, repeats:int):
    for _ in range(repeats):
        print(message, end=" ")

def main():

    print("Please type a message: ", end="")
    print(BLUE, end="")
    message = input()
    print(RESET, end="")

    print("Enter a number of times to repeat your message: ", end="")
    print(BLUE, end="")
    repeats = int(input())
    print(RESET, end="")

    print_multiple(message, repeats)

if __name__ == '__main__':
    main()