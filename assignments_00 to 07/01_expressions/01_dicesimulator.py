import random

NUM_SIDES = 6
def roll_dice():

    die1 = random.randint(1 , NUM_SIDES)
    die2 = random.randint(1 , NUM_SIDES)
    total = die1 + die2
    print(f"\nTotal of two dice is {total}")

def main():

    die1 = 10
    print(f"\ndie1 in main() starts as {die1}")

    for i in range(3):
        roll_dice()
    print(f"\ndie1 in main() is still {die1}")

if __name__ == "__main__":
    main()

