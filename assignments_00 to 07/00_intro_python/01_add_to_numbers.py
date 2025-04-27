def main():

    print("This program asks the user for two integers and prints their sum..")
    # Get two numbers from the user
    num1 = input("Enter the first number: ")
    num1 = int(num1)  # Convert the input to an integer
    num2 = input("Enter the second number: ")
    num2 = int(num2)  # Convert the input to an integer

    # Add the two numbers
    result = num1 + num2

    # Print the result
    print(f"The total is {result}.")

if __name__ == "__main__":
    main()