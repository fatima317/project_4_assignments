MAX_VALUE = 10000

def main():
    
    curr_value = 0
    next_value = 1
    while curr_value <= MAX_VALUE:
        print(curr_value, end=" ")
        value_after_next = curr_value + next_value
        curr_value = next_value
        next_value = value_after_next

if __name__ == '__main__':
    main()