import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    while True: 
        # won't need try / catch because we're dealing with strings anyways 
        # (and converting the prompt to strings anyway)
        # try:
        #     city = str(input("Type in city name: ").strip().lower())
        # except ValueError:
        #     print("Sorry, I'm looking for a string type")
        
        city = str(input("Pick a city (chicago, new york city, washington): ").strip().lower())

        if city not in ("chicago", "new york city", "washington"):
            print("Invalid. Please try again")
            continue
        else:
            break

    while True:
        month = str(input("Type in name of month to filter by (i.e. January): ").strip().lower())

        if month not in ("january", "february", "march", "april", "may", "june", "all"):
            print("Invalid. Please type in month name (or \"all\" to select every month)")
            continue
        else:
            break

    while True:
        day = str(input("Type in name of day to filter by (i.e. Monday): ").strip().lower())

        if day not in ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday" , "sunday", "all"):
            print("Invalid. Please type in valid day (or \"all\" to select every day)")
            continue
        else:
            break


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime type
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['Month'] = df['Start Time'].dt.month
    df['Day_of_Week'] = df['Start Time'].dt.weekday_name
    df['Hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    # thus if user inputted actual month
    if month != 'all':
       # use the index of the months list to get the corresponding int --> must be in chronological order!! 
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        
        # month outputted as integer
        month = months.index(month) + 1

        # month column is in type(integer)
        df = df[df['Month'] == month]


    # filter by day of week if applicable
    # thus if user inputted actual day
    if day != 'all':
        # list of days must be in chronological order!! 
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        # day = days.index(day) + 1
        
        # filter by day of week to create the new dataframe
        # make sure to add .title()! bc within dataframe, the first letter of weekday is capitalized 
        df = df[df['Day_of_Week'] == day.title()]
        

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # look_up dictionary 
    look_up = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May',
        '6': 'June', '7': 'July', '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December'}

    # display the most common month
    popular_month = df['Month'].mode()[0]
    month_in_string = look_up[str(popular_month)]
    print("The most common month was: ", month_in_string)

    # display the most common day of week
    popular_day = df['Day_of_Week'].mode()[0]
    print("The most common day of the week was: {}".format(popular_day))

    # display the most common start hour
    popular_hour = df['Hour'].mode()[0]
    print('The most common start hour was:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
