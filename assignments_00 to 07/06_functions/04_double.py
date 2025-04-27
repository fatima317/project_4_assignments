BOLD_ITALIC = "\033[1;3m"
RESET = "\033[0m"

def double(num):
    return num * 2

def main():
    print("Enter a number: ", end="")
    print(BOLD_ITALIC, end="")
    num = int(input())
    print(RESET, end="")
    
    result = double(num)
    print(f"Double that is {result}")

if __name__ == '__main__':
    main()
