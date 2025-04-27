MIN_HEIGHT: int = 50

BOLD_ITALIC = "\033[1;3m"
RESET = "\033[0m"

def main():

    while True:
        print("\nHow tall are you (in cm)? ", end="")
        print(BOLD_ITALIC, end="")
        height_input = input()
        print(RESET, end="")
        
        if height_input == "":
           break
     
        height = int(height_input)

        if height >= MIN_HEIGHT:
           print("You're tall enough to ride!")
        else:
           print("You're not tall enough to ride, but maybe next year!")
    

if __name__ == '__main__':
    main()