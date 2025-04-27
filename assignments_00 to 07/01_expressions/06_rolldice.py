import random

NUM_SIDE = 6
def main():
    die1 = random.randint(1, NUM_SIDE)
    die2 = random.randint(1, NUM_SIDE)
    total = die1 + die2

    print(f"\nDice have {NUM_SIDE} sides each.")
    print(f"\nFirst die: {die1}")
    print(f"\nSecond die: {die2}")
    print(f"\nTotal of two dice is: {total}")
    
if __name__ == '__main__':
    main()