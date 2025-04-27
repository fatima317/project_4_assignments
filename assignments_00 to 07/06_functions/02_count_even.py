def count_even(lst):
    
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    return count

def lst_of_int():

    lst = []
    user_input = input("Enter an integer or press enter to stop: ")
    while user_input != "":
        lst.append(int(user_input))
        user_input = input("Enter an integer or press enter to stop: ")

    return lst

def main():

    lst = lst_of_int()
    even_count = count_even(lst)
    print(f"There are {even_count} even numbers in the list.")
    
if __name__ == '__main__':
    main()