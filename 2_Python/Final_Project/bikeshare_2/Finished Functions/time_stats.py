
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Use df.mode() to compute most often data --> outputs it as a tabular data with row 0
    # and then access it with indexing (ie [0])

    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.mode.html

    # look_up dictionary 
    look_up = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May',
        '6': 'June', '7': 'July', '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December'}

    # display the most common month
    popular_month = df['month'].mode()[0]
    month_in_string = look_up[str(popular_month)]
    print("The most common month is: ", month_in_string)

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("The most common day of the week is: {}".format(popular_day))

    # display the most common start hour
    popular_hour = df['Hour'].mode()[0]
    print('The most common start hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



    