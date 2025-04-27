import math
BOLD_ITALIC = "\033[1;3m"
RESET = "\033[0m"
def main():
    
    print("\nEnter the length of AB: ", end="")
    print(BOLD_ITALIC, end="")
    AB = float(input())
    print(RESET, end="")
    
    print("\nEnter the length of AC: ", end="")
    print(BOLD_ITALIC, end="")
    AC = float(input())
    print(RESET, end="")
    

    BC = math.sqrt(AB**2 + AC**2)

    print(f"\nThe length of BC (the hypotenuse) is: {BC}")


if __name__ == '__main__':
    main()