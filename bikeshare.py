import time
import pandas as pd

# Dictionary to map city names to their respective CSV data files
CITY_DATA = { 
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv' 
}

def correct_input(prompt, valid_inputs):
    """Check the correctness of the user input based on the expected valid inputs.
    
    Args:
        prompt (str): The prompt message for user input.
        valid_inputs (list): List of valid input options.
    
    Returns:
        str: Validated user input.
    """
    while True:
        line_input = input(prompt).lower()
        if line_input in valid_inputs:
            return line_input
        else:
            print(f"Please enter one of the following: {', '.join(valid_inputs)}")

def get_filters():
    """Asks the user to specify a city, month, and day to analyze.
    
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    city = correct_input("Enter a city (chicago, new york city, washington): ", ['chicago', 'new york city', 'washington'])
    month = correct_input("Enter a month (january, february, march, april, may, june, or all): ", 
                          ['january', 'february', 'march', 'april', 'may', 'june', 'all'])
    day = correct_input("Enter a day (sunday, monday, tuesday, wednesday, thursday, friday, saturday, or all): ", 
                        ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'])

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """Loads data for the specified city and filters by month and day if applicable.
    
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Load data file into a DataFrame
    df = pd.read_csv(CITY_DATA[city])

    # Convert the 'Start Time' column to datetime and extract month, day of week, and hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    # Filter the DataFrame based on month and day
    if month != 'all':
        month_idx = ['january', 'february', 'march', 'april', 'may', 'june'].index(month) + 1
        df = df[df['month'] == month_idx]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

# ... (other functions remain unchanged) ...

def main():
    """Main function to execute the bikeshare data analysis."""
    
    while True:
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
    main()  # Run the main function
