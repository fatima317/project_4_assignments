BLUE = "\033[94m"
RESET = "\033[0m"

def print_divisors(num:int):
    for i in range(num):
        divisor = i + 1
        if num % divisor == 0:
            print(divisor, end=" ")

def main():

    print("Enter a number: ", end="")
    print(BLUE, end="")
    num = int(input())
    print(RESET, end="")

    print_divisors(num)


if __name__ == '__main__':
    main()