import pandas as pd
import os

df= pd.read_csv("/Users/jhl/Documents/Udacity/Python/bikeshare-2/chicago.csv")
#  datetime conversion
df['Start Time'] = pd.to_datetime(df['Start Time'])
# month 
df['month'] = df['Start Time'].dt.month
df['day_of_week'] = df['Start Time'].dt.weekday_name
df['Hour'] = df['Start Time'].dt.hour

# popular_month returns int 
popular_month = df['month'].mode()[0]
popular_day = df['day_of_week'].mode()[0]
popular_hour = df['Hour'].mode()[0]

# look_up dictionary 
look_up = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May',
        '6': 'June', '7': 'July', '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December'}

# matches string in the look_up dictionary 
a = look_up[str(popular_month)]

print(a)
print(popular_day)
print('Popular Hour:', popular_hour)

print('-'*40)

# df = df[df['day_of_week'] == day]

df_2 = df['End Station'].mode()[0]
print(df_2)



# pair = df.groupby(['Start Station', 'End Station']).size().reset_index(name="counts")
# min_count = pair['counts'].min()
# max_count = pair['counts'].max()


print(min_count)
print(max_count)

# outputs
pair = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False)
    
    # outputs a table (with different dtypes per column) 
pair_2 = df.groupby(['Start Station', 'End Station']).size().reset_index(name="counts")
pair_final = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False).reset_index(name="counts")
    
# print(pair.dtypes)
pair.head()
# pair_2.head()
# pair_final.head()

# pair_2['Start Station'][0]
