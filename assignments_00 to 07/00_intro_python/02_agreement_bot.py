BOLD_ITALIC = "\033[1;3m"
RESET = "\033[0m"

def main():

    print ("What's your favorite animal? ", end="")
    print(BOLD_ITALIC, end="")
    animal = (input())
    print(RESET, end="")
   
    print(f"\nMy favorite animal is also {animal}!")

if __name__ == "__main__":
    main()
