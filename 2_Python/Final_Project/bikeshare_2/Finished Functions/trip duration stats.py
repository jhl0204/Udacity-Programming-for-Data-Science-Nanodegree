from datetime import timedelta

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # from the load_data function, df is already given as filtered 
    # (meaning that the rows are shortened (less than the total number of rows in a dataframe))
    # thus only need to find the TOTAL SUM of the column 'DURATION'

    # https://stackoverflow.com/questions/41286569/get-total-of-pandas-column
    # display total travel time

    # import timedelta!!! s
    total_travel_time = df['Trip Duration'].sum()

    # use timedelta function to output duration
    # yet for some reason, timedelta() doesn't accept int32,64 as valid dtype
    # thus need to cast it as float 
    
    t2 = total_travel_time.astype('float64', copy=False)
    time_in_duration = timedelta(seconds=t2)
	print("The total travel time in seconds is: {} which converts to {} in duration ".format(total_travel_time, time_in_duration))

    # display mean travel time

    # Refereence: 
    # https://stackoverflow.com/questions/31037298/pandas-get-column-average-mean

	mean_travel_time = df['Trip Duration'].mean()
	print("Mean travel time is: '{}' ".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
