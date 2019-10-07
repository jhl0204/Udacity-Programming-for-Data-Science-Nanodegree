def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    user_type_count = df["User Type"].value_counts()
    print(user_type_count)

    # Display counts of gender
    # tried to use try / except block but udacity thread pointed me towards if statement to generalize! 
    # Reference: https://study-hall.udacity.com/rooms/community:nd104:645596-project-328/community:thread-11448949055-512760?contextType=room
    # https://stackoverflow.com/questions/19482970/get-list-from-pandas-dataframe-column-headers

    # df.columns returns the list of column index in DataFrame
    # if "Gender" isn't included in that list, then execute code, otherwise print statement
    if "Gender" in df.columns: 
        gender_count = df["Gender"].value_counts()

        # to count null values
        # Reference: https://stackoverflow.com/questions/26266362/how-to-count-the-nan-values-in-a-column-in-pandas-dataframe
        nan_values = df["Gender"].isna().sum()

        print("\nCounts by Gender: \n{}\n \n*Note: there were '{}' NaN values for gender column".format(gender_count,nan_values))
    else:
        print("No such column exists in this dataset")

    # Display earliest, most recent, and most common year of birth

	if "Birth Year" in df.columns:

        earliest = df['Birth Year'].min()
        most_recent = df['Birth Year'].max()
        most_common = df['Birth Year'].mode()[0]
        print("\nEarliest birth year: '{}'. \nMost recent birth year: '{}'. \nMost common birth year: '{}'.".format(earliest, most_recent, most_common))

    else:
        print("\nNo column named 'Birth Year' exists in this dataset")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
