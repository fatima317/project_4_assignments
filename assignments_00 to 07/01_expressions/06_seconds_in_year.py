DAYS_PER_YEAR = 365
HOURS_PER_DAY = 24
MIN_PER_HOUR = 60
SEC_PER_MINUTE = 60

def main():
    # Constants for time calculations
    seconds_in_year = DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MINUTE

    print(f"\nThere are {seconds_in_year} seconds in a year!")

if __name__ == '__main__':
    main()