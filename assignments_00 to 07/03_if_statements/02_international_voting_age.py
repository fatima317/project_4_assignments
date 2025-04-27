PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48

BLUE = "\033[94m"
RESET = "\033[0m"

def main():
    
    print("How old are you? ", end="")
    print(BLUE, end="")
    voting_age = int(input())
    print(RESET, end="")

    if voting_age >= PETURKSBOUIPO_AGE:
        print("You can vote in Peturksbouipo where the voting age is " + str(PETURKSBOUIPO_AGE) + ".")
    else:
        print("You cannot vote in Peturksbouipo where the voting age is " + str(PETURKSBOUIPO_AGE) + ".")

    if voting_age >= STANLAU_AGE:
        print("You can vote in Stanlau where the voting age is " + str(STANLAU_AGE) + ".")
    else:
        print("You cannot vote in Stanlau where the voting age is " + str(STANLAU_AGE) + ".")

    if voting_age >= MAYENGUA_AGE:
        print("You can vote in Stanlau where the voting age is " + str(MAYENGUA_AGE) + ".")
    else:
        print("You cannot vote in Stanlau where the voting age is " + str(MAYENGUA_AGE) + ".")


if __name__ == '__main__':
    main()