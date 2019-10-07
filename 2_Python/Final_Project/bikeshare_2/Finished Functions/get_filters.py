def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    # is there a way to integrate this in one while loop? or must it be done this way?
    # like, is there a more efficient method of doing it?


    while True: 
        # won't need try / catch because we're dealing with strings anyways 
        # (and converting the prompt to strings anyway)
        # try:
        #     city = str(input("Type in city name: ").strip().lower())
        # except ValueError:
        #     print("Sorry, I'm looking for a string type")
        
        city = str(input("Type in city name: ").strip().lower())

        if city not in ("chicago", "new york city", "washington"):
            print("Invalid. Please try again")
            continue
        else:
            break

    while True:
        month = str(input("Type in name of month to filter by: ").strip().lower())

        if month not in ("january", "february", "march", "april", "may", "june", "all"):
            print("Invalid. Please type in month name (or \"all\" to select every month)")
            continue
        else:
            break

    while True:
        day = str(input("Type in name of day to filter by: ").strip().lower())

        if day not in ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday" , "sunday", "all"):
            print("Invalid. Please type in valid day (or \"all\" to select every day)")
            continue
        else:
            break
    

    print('-'*40)
    return city, month, day


def main():
    while True:
        get_filters()
        


if __name__ == "__main__":
	main()


