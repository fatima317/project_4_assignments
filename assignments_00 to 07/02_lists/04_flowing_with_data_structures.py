BOLD_ITALIC = "\033[1;3m"
RESET = "\033[0m"

def add_three_copies(my_list, data):
    for _ in range(3):
        my_list.append(data)

def main():

    print("\nEnter a message to copy: ", end="")
    print(BOLD_ITALIC, end="")
    message = input("")
    print(RESET, end="")
    
    my_list = []
    print("\nList before: []")

    add_three_copies(my_list, message)


    formatted_list = "["
    formatted_list += ", ".join([f"'{msg}'" for msg in my_list])
    formatted_list += "]"

    print(f"\nList after: {formatted_list}")

if __name__ == '__main__':
    main()
