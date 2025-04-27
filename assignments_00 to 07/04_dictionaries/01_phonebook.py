def read_phone_nums():

    phonebook = {}

    while True:
        name = input("Enter name: ")
        if name == "":
            break
        number = input("Enter number: ")
        phonebook[name] = number

    return phonebook

def print_phonebook(phonebook):

    for name in phonebook:
        print(str(name) + " -> " + str(phonebook[name]))

def lookup_num(phonebook):

    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name not in phonebook:
            print(name + " is not in the phonebook")
        else:
            print(phonebook[name])

def main():
    phonebook = read_phone_nums()
    print_phonebook(phonebook)
    lookup_num(phonebook)

if __name__ == '__main__':
    main()