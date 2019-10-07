# Modified Version of the code in following url reference:
# Reference: https://knowledge.udacity.com/questions/26261


def raw_data(df): 
    
    # initial input! 
    display_raw_input = input("\nWould you like to see individual raw data? Enter 'yes' or 'no'\n").strip().lower()    
    if display_raw_input in ("yes", "y"):
        i = 0
        
        # use while loop for the inputs that you want repeated! 
        # thus should start here, not at the beginning of the code

        while True: 
            # check if i is out of bounds, if upper limit is out of bounds, 
            # then print from lower limit to length of dataframe rows                     
            if (i + 5 > len(df.index) - 1):
                # remember that the slicing is lower bound inclusive and upper bound exclusive!! 
                # thus upper bound should be (len(df.index) --> won't print out that upper bound bc its exclusive)
                print(df.iloc[i:len(df.index), :])
                print("You've reached the end of the rows")
                break

            # if i is not out of bounds, then just print the dataframe normally
            print(df.iloc[i:i+5, :])
            i += 5
            
            # program temporarily halts at the input! 
            # thus while loop does not get executed 100000 times (exaggerated) a second lol 
            show_next_five_input = input("\nWould you like to see the next 5 rows? Enter 'yes' or 'no'\n").strip().lower()
            if show_next_five_input not in ("yes", "y"):
                break



                
                

def raw_data_222(df): 
    i = 0
    while True: 
        display_raw_data = input("\nWould you like to see individual raw data? Enter 'yes' or 'no'\n").strip().lower()

        if display_raw_data not in ("yes", "no", 'y', 'n'):
            print("Invalid response. Please type in 'yes' or 'no'")
            continue
        elif display_raw_data in ("yes", "y"):
            # show data
            # print("show data")
            # exclusive of last element 
            print(df.iloc[0:5,:])
            # ask again as an input (make sure to use variables)
            show_next_five = input("\nWould you like to see the next 5 rows?")
                
            if show_next_five in ("yes", "y"):
                i = i + 5
                # check if i is out of bounds, if upper limit is out of bounds, 
                # then print from lower limit to length of dataframe rows                     
                if (i + 5 >= len(df.index)):
                    print(df.iloc[i:len(df.index) - 1, :])
                    print("You've reached the end of the rows")
                    break

                # otherwise, just print normally 
                print(df.iloc[i: i+5, :])
                # then ask again for 'show next five'
            else: # if not, then break out of the while loop
                break

        else:  
            print("You have chose not to see the individual data")
            break   



