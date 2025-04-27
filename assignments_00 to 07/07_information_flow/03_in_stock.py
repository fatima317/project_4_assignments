BOLD_ITALIC = "\033[1;3m"
RESET = "\033[0m"

def main():
    
    print("Enter a fruit: ", end="")
    print(BOLD_ITALIC, end="")
    fruit= input()
    print(RESET, end="")
    stock = num_in_stock(fruit)
	
    if stock == 0:
     print("This fruit is not in stock.")
    else:
     print("This fruit is in stock! Here is how many:")
     print(stock)


def num_in_stock(fruit):
	
	if fruit == 'apple':
		return 50
	if fruit == 'banana':
		return 20
	if fruit == 'orange':
		return 500
	if fruit == 'mang':
		return 250
	else:
		return 0


if __name__ == '__main__':
    main()