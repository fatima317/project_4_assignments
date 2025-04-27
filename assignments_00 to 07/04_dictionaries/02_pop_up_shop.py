BOLD_ITALIC = "\033[1;3m"
RESET = "\033[0m"
def main():
    
    fruits_cost = {'apple': 10.0,'durian': 25.0,'jackfruit': 15.0,'kiwi': 12.5,'rambutan': 7.0,'mango': 10.0}

    total_cost = 0.0
    for fruit in fruits_cost:
        price = fruits_cost[fruit]
        print(f"How many ({fruit}) do you want?: ", end="")
        print(BOLD_ITALIC, end="")
        quantity = int(input())
        print(RESET, end="")
        
        total_cost += price * quantity

    print(f"\nYour total is ${total_cost}")

if __name__ == '__main__':
    main()