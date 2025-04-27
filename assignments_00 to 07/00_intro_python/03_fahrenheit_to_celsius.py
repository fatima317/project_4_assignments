BOLD_ITALIC = "\033[1;3m"
RESET = "\033[0m"

def main():
    print("This program converts Fahrenheit to Celsius.")

    print("Enter the temperature in Fahrenheit: ", end="")
    print(BOLD_ITALIC, end="")
    fahrenheit = float(input())
    print(RESET, end="")

    celsius = (fahrenheit - 32) * 5.0 / 9.0 # Convert to Celsius

    print(f"\nTemperature : {fahrenheit}F = {celsius}C.")



if __name__ == '__main__':
    main()