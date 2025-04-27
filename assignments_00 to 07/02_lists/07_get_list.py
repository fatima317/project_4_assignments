BLUE = "\033[94m"
RESET = "\033[0m"

def main():
    
    lst =[]
    print("Enter a value: ", end="")
    print(BLUE, end="")
    val = input()
    print(RESET, end="")
    while val != "":
        lst.append(val)
        print("Enter a value: ", end="")
        print(BLUE, end="")
        val = input()
        print(RESET, end="")

    print("Here's the list:", f"[{', '.join(lst)}]")


if __name__ == '__main__':
    main()