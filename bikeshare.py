import time
import pandas as pd

# Dictionary to map city names to their respective CSV data files
CITY_DATA = { 
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv' 
}

<<<<<<< HEAD
def correct_input(str_inp, runtype):
    """Checks the correctness of the input."""
||||||| parent of e9167d5 (Your descriptive commit message here)
def correct_input(str_inp, runtype):
=======
def correct_input(prompt, input_type):
>>>>>>> e9167d5 (Your descriptive commit message here)
    """Check the correctness of the user input based on the expected type.
    
    Args:
        prompt (str): The prompt message for user input.
        input_type (str): Indicates the type of input expected ('city', 'month', 'day').
    
    Returns:
        str: Validated user input.
    """
    valid_inputs = {
        'city': ['chicago', 'new york city', 'washington'],
        'month': ['january', 'february', 'march', 'april', 'may', 'june', 'all'],
        'day': ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
    }

    while True:
<<<<<<< HEAD
        line_input = input(str_inp)
        try:
            # Check if input matches expected city names
            if line_input in ['chicago', 'new york city', 'washington'] and runtype == 1:
                break
            elif line_input in ['january', 'february', 'march', 'april', 'may', 'june','all'] and runtype == 2:
            # Check if input matches expected month names
            elif line_input in ['january', 'february', 'march', 'april', 'may', 'june', 'all'] and runtype == 2:
                break
            # Check if input matches expected day names
            elif line_input in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'] and runtype == 3:
                break
            else:
                # Provide feedback for invalid city input
                if runtype == 1:
                    print("please enter: chicago, new york city or washington")
                # Provide feedback for invalid month input
                if runtype == 2:
                    print("please enter: january-june or all")
                # Provide feedback for invalid day input
                if runtype == 3:
                    print("please enter: sunday-saturday or all")
        except ValueError:
            print("wrong input!")
    return line_input
||||||| parent of e9167d5 (Your descriptive commit message here)
        line_input = input(str_inp)
        try:
            # Check if input matches expected city names
            if line_input in ['chicago', 'new york city', 'washington'] and runtype == 1:
                break
            # Check if input matches expected month names
            elif line_input in ['january', 'february', 'march', 'april', 'may', 'june', 'all'] and runtype == 2:
                break
            # Check if input matches expected day names
            elif line_input in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'] and runtype == 3:
                break
            else:
                # Provide feedback for invalid city input
                if runtype == 1:
                    print("please enter: chicago, new york city or washington")
                # Provide feedback for invalid month input
                if runtype == 2:
                    print("please enter: january-june or all")
                # Provide feedback for invalid day input
                if runtype == 3:
                    print("please enter: sunday-saturday or all")
        except ValueError:
            print("wrong input!")
    return line_input
=======
        line_input = input(prompt)
        if line_input in valid_inputs[input_type]:
            return line_input
        print(f"Invalid input! Please enter one of the following: {', '.join(valid_inputs[input_type])}")
>>>>>>> e9167d5 (Your descriptive commit message here)

def get_filters():
    """Prompts user for city, month, and day to analyze."""
    """
    Asks the user to specify a city, month, and day to analyze.
    
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
<<<<<<< HEAD
    # Get user input for city, month, and day using the correct_input function
    # Get user input for city (chicago, new york city, washington)
    city = correct_input("Enter a city: ", 1)

    # Get user input for month (all, january, february, ... , june)
    month = correct_input("Enter a month between January and June: ", 2)
    day = correct_input("Enter a day between Monday and Saturday: ", 3)

    # Get user input for day of the week (all, monday, tuesday, ... sunday)
    day = correct_input("Enter a day between monday and saturday: ", 3)
||||||| parent of e9167d5 (Your descriptive commit message here)
    # Get user input for city (chicago, new york city, washington)
    city = correct_input("Enter a city: ", 1)

    # Get user input for month (all, january, february, ... , june)
    month = correct_input("Enter a month between January and June: ", 2)

    # Get user input for day of the week (all, monday, tuesday, ... sunday)
    day = correct_input("Enter a day between monday and saturday: ", 3)
=======
    city = correct_input("Enter a city: ", 'city')
    month = correct_input("Enter a month between January and June: ", 'month')
    day = correct_input("Enter a day between monday and saturday: ", 'day')
>>>>>>> e9167d5 (Your descriptive commit message here)

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """Loads data for the specified city and applies filters."""
    # Load the city's data and convert 'Start Time' to datetime
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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
<<<<<<< HEAD
    
    # Extract month, day of week, hour from Start Time to create new columns

    # Extract month, day of week, and hour from 'Start Time' to create new columns
||||||| parent of e9167d5 (Your descriptive commit message here)

    # Extract month, day of week, and hour from 'Start Time' to create new columns
=======
>>>>>>> e9167d5 (Your descriptive commit message here)
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # Filter by month and day
    if month != 'all':
<<<<<<< HEAD
        # Use the index of the months list to get the corresponding int
        # Get the corresponding int for the month
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        # Filter by month to create the new DataFrame
||||||| parent of e9167d5 (Your descriptive commit message here)
        # Get the corresponding int for the month
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
=======
        month_idx = ['january', 'february', 'march', 'april', 'may', 'june'].index(month) + 1
        df = df[df['month'] == month_idx]
>>>>>>> e9167d5 (Your descriptive commit message here)

    if day != 'all':
<<<<<<< HEAD
        # Filter by day of week to create the new DataFrame
        # Filter by day of week to create a new DataFrame
||||||| parent of e9167d5 (Your descriptive commit message here)
        # Filter by day of week to create a new DataFrame
=======
>>>>>>> e9167d5 (Your descriptive commit message here)
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Calculate and print the most common month, day, and start hour
    # Display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:', popular_month)

    # Display the most common day of the week
    most_common_day = df['day_of_week'].mode()[0]
    print('Most Day Of Week:', most_common_day)

    # Display the most common start hour
    most_common_start_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    """Displays statistics on the most popular stations and trips."""
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Start Station:', popular_start_station)

    # Display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most End Station:', popular_end_station)

    # Display most frequent combination of start station and end station trip
    frequent_combination = df.groupby(['Start Station', 'End Station'])
    popular_frequent_combo_station = frequent_combination.size().sort_values(ascending=False).head(1)
    print('Most frequent combination of Start Station and End Station trip:\n', popular_frequent_combo_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time)

    # Display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df, city):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Show user type counts and, if applicable, gender and birth year stats
    print('User Type Stats:')
    print(df['User Type'].value_counts())
    
    if city != 'washington':
        print('Gender Stats:')
        print(df['Gender'].value_counts())
        
        # Display earliest, most recent, and most common year of birth
        print('Birth Year Stats:')
        most_common_year = df['Birth Year'].mode()[0]
        print('Most Common Year:', most_common_year)
        most_recent_year = df['Birth Year'].max()
        print('Most Recent Year:', most_recent_year)
        earliest_year = df['Birth Year'].min()
        print('Earliest Year:', earliest_year)

        print('Earliest Year:', earliest_year)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def data_info(df):
<<<<<<< HEAD
    """Displays five rows of bikeshare data."""
    """Displays five rows of bikeshare data if the user wishes to see it."""
    
||||||| parent of e9167d5 (Your descriptive commit message here)
    """Displays five rows of bikeshare data if the user wishes to see it."""
    
=======
    """Displays five rows of bikeshare data if the user wishes to see it.""" 
>>>>>>> e9167d5 (Your descriptive commit message here)
    response_locket = ['yes', 'no']
    read_data = ''
    counter = 0
    
    while read_data not in response_locket:
        print('\nDo you wish to view the raw bikeshare data?')
        print('\nRight responses: \nyes or no')
        print('\nValid responses: \nyes or no')
        read_data = input().lower()
        if read_data == 'yes':
           print(df.head())
        elif read_data not in response_locket:
            print('Wrong input!')
            print('Reloading...\n')
            print('Wrong input!')
            print('Reloading...\n')
    
    while read_data == 'yes':
        print('Wish to view more data?')
        counter += 5
        print('Do you wish to view more data?')
        counter += 5
        read_data = input().lower()
        if read_data == 'yes':
              print(df[counter:counter + 5])
        elif read_data != 'yes':
              break

print('_'*40)

print('_' * 40)

def main():
<<<<<<< HEAD
    """Main function to run the bikeshare analysis."""
    """Main function to execute the bikeshare data analysis."""
    
||||||| parent of e9167d5 (Your descriptive commit message here)
    """Main function to execute the bikeshare data analysis."""
    
=======
    """Main function to execute the bikeshare data analysis."""  
>>>>>>> e9167d5 (Your descriptive commit message here)
    while True:
        city, month, day = get_filters()  # Get filters from user
        df = load_data(city, month, day)  # Load and filter data
        # Call functions to display statistics and data
        data_info(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        city, month, day = get_filters()  # Get user filters
        df = load_data(city, month, day)  # Load the filtered data
        data_info(df)  # Display raw data if requested
        time_stats(df)  # Display time statistics
        station_stats(df)  # Display station statistics
        trip_duration_stats(df)  # Display trip duration statistics
        user_stats(df, city)  # Display user statistics

        # Ask user if they want to restart the analysis
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
    main()  # Run the main function
