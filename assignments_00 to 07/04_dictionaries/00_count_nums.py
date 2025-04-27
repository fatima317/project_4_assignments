BLUE = "\033[94m"
RESET = "\033[0m"

def get_user_num():

    user_num =[]
    while True:
        print("Enter a number: ", end="")
        print(BLUE, end="")
        user_input = input()
        print(RESET, end="")

        if user_input == "":
            break

        num = int(user_input)
        user_num.append(num)
    return user_num

def count_num(num_lst):

    num_dict = {}
    for num in num_lst:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    return num_dict

def print_count(num_dict):

    for num in num_dict:
        print(str(num) + " appears " + str(num_dict[num]) + " times.", end=" ")

def main():
    
    user_num = get_user_num()
    num_dict = count_num(user_num)
    print_count(num_dict)
    
if __name__ == '__main__':
    main()