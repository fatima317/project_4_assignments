MAX_LENGTH:int = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()
        print(f"Removed: {removed_item}")

def get_lst():

    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():

    lst = get_lst()
    print("Original list:", lst)

    shorten(lst)
    print("Shortened list:", lst)
    
if __name__ == '__main__':
    main()