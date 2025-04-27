SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my "

BOLD_ITALIC = "\033[1;3m"
RESET = "\033[0m"

def main():
    
    print("Please type an adjective and press enter. ", end="")
    print(BOLD_ITALIC, end="")
    adjective:str = input()
    print(RESET, end="")
    
    print("Please type a noun and press enter. ", end="")
    print(BOLD_ITALIC, end="")
    noun:str = input()
    print(RESET, end="")

    print("Please type a verb and press enter. ", end="")
    print(BOLD_ITALIC, end="")
    verb:str = input()
    print(RESET, end="")

    print(SENTENCE_START + adjective + " " + noun + " " + verb + "!")

if __name__ == "__main__":
    main()