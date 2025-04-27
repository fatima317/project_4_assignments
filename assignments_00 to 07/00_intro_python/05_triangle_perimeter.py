BOLD_ITALIC = "\033[1;3m"
RESET = "\033[0m"

def main():
    print("What is the length of side 1? ", end="")
    print(BOLD_ITALIC, end="")
    side1 = float(input())
    print(RESET, end="")
    
    print("What is the length of side 2? ", end="")
    print(BOLD_ITALIC, end="")
    side2 = float(input())
    print(RESET, end="")
    
    print("What is the length of side 3? ", end="")
    print(BOLD_ITALIC, end="")
    side3 = float(input())
    print(RESET, end="")
    

    perimeter = side1 + side2 + side3
    print(f"\nThe perimeter of the triangle is {perimeter}")

if __name__ == "__main__":
    main()
