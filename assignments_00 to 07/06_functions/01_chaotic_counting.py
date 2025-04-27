import random
DONE_LIKELIHOOD = 0.3

def chaotic_counting():
    for i in range(1, 11):
        if done():
            return
        print(i, end=" ")

def done():
    if random.random() < DONE_LIKELIHOOD:
        return True
    return False


def main():
    print("\nI'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("\nI'm done.")
    
if __name__ == '__main__':
    main()