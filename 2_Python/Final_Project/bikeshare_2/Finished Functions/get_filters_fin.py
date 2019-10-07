
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\nHello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    validity = False 

    while True: 
        # won't need try / catch because we're dealing with strings anyways 
        # (and converting the prompt to strings anyway)
        # try:
        #     city = str(input("Type in city name: ").strip().lower())
        # except ValueError:
        #     print("Sorry, I'm looking for a string type")
        
        city = str(input("\nPick a city (chicago, new york city, washington): ").strip().lower())

        if city not in ("chicago", "new york city", "washington"):
            print("\nInvalid Response. Please try again")
            continue
        else:
            print("\nIt looks like you want to see data for: '{}' ".format(city.title()))
            validity_check()
            break

    # criteria = str(input("Would you like to filter the data by month, day, both or not at all? Type 'None' for no time filter").strip().lower())

    # if criteria not in ("month", "day", "both")
    while True:
        month = str(input("\nType in name of month to filter by (i.e. January): ").strip().lower())

        if month not in ("january", "february", "march", "april", "may", "june", "all"):
            print("\nInvalid. Please type in month name (or \"all\" to select every month)")
            continue
        else:
            print("\nIt looks like you want to filter by: '{}' ".format(month.title()))
            validity_check()
            break

    while True:
        day = str(input("\nType in name of day to filter by (i.e. Monday): ").strip().lower())

        if day not in ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday" , "sunday", "all"):
            print("Invalid. Please type in valid day (or \"all\" to select every day)")
            continue
        else:
            print("\nIt looks like you want to filter by: '{}' ".format(day.title()))
            validity_check()
            break

    print('-'*40)
    return city, month, day

def validity_check(): 
    
    while True: 
        validity = str(input("Is your input correct? Type 'y' to continue and 'n' to restart: \n").strip().lower())
        if validity not in ("y", "n"):
            print("\nInvalid Response. Please try again")
            continue
        elif validity == 'y':
            break
        else: 
            get_filters()