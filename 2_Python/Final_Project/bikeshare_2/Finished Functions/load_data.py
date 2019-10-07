import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
              
df = pd.read_csv(CITY_DATA['chicago'])
print(df.head(7))

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
       (str) city - name of the city to analyze
       (str) month - name of the month to filter by, or "all" to apply no month filter
       (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
       df - pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month / day of week / Hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['Hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
       # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        # indexing from 0 
        month = months.index(month) + 1
        
        # month returns a number after getting input from the function argument
        # this is because (dt.month) returns a number
        
        # In the following statement: (df['month'] == month), df['month'] is assigned a number (bc month is number from above)
        
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = days.index(day) + 1
        
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]
    
    return df
    
df = load_data('chicago', 'march', 'friday')

print(df.head(3))
