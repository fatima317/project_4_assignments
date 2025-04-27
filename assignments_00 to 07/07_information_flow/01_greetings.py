BOLD_ITALIC = "\033[1;3m"
RESET = "\033[0m"

def greet(name:str):
    return "Greetings " + name + "!"  

def main():
    print("What's your name? ", end="")
    print(BOLD_ITALIC, end="")
    name = input()
    print(RESET, end="")

    print(greet(name))

if __name__ == '__main__':
    main()