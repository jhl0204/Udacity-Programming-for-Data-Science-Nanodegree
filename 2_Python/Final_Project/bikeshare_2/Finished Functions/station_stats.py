
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station

    start_station = df['Start Station'].mode()[0]
	print("Most commonly used start station was: {}".format(start_station))

    # display most commonly used end station

    end_station = df['End Station'].mode()[0]
	print("Most commonly used end station was: {}".format(end_station))
	
    # display most frequent combination of start station and end station trip

    # outputs dtype: int64 --> if I try to slice into it ex) pair[0], I get one number! 
    # thus must use the form below (table form)
    pair = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False)
    
    # outputs a table (with different dtypes per column) --> I think the reset_index makes the datatype into a table
    pair_2 = df.groupby(['Start Station', 'End Station']).size().reset_index(name="counts")
    pair_final = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False).reset_index(name="counts")
    
    frequent_start_pair = pair_final['Start Station'][0]
    frequent_end_pair = pair_final['End Station'][0]

    print("The start station for most frequent combination is {} and the end station is {}".format(frequent_start_pair, frequent_end_pair))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)