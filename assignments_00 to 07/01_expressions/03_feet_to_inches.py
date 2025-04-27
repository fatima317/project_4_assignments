INCHES_PER_FOOT = 12
# This program converts feet to inches.

def main():
   
   feet = float(input("Enter number of feet: "))
   inches = feet * INCHES_PER_FOOT

   print(f"\n{feet} feet is {inches} inches.")


if __name__ == '__main__':
    main()