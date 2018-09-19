import time
import pandas as pd
CITY_DATA = {
                'chicago': 'chicago.csv',
                'new york city': 'new_york_city.csv',
                'washington': 'washington.csv'
            }
months = ['january', 'february', 'march', 'april', 'may', 'june']
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday',
        'saturday']


def get_filters():
    """Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no \
        month filter
        (str) day - name of the day of week to filter by, or "all" to \
        apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs
    city = ''
    month = ''
    day = ''
    while city not in CITY_DATA:
        city = input('Please enter which city,valid inputs are \
chicago, new york city , washington:').lower()

    # get user input for month (all, january, february, ... , june)
    filter = None
    while filter not in ('both', 'month', 'day', ''):
        filter = input('Would you like to filter the data by month,day,both \
or no filter at all? valid inputs are month, day , both or Just press Enter for no filter :').lower()
    if not filter:
        month = 'all'
        day = 'all'
    elif filter == 'both':
        while month not in months:
            month = input('which month, valid months are january, \
february, march, april, may, june:').lower()
        while day not in days:
            day = input('Which day - Monday, Tuesday, Wednesday, Thursday,\
Friday, Saturday, or Sunday?: ').lower()
    elif filter == 'month':
        while month not in months:
            month = input('which month, valid months are january, \
february, march, april, may, june:').lower()
        day = 'all'
    elif filter == 'day':
        while day not in days:
            day = input('Which day - Monday, Tuesday, Wednesday, Thursday,\
Friday, Saturday, or Sunday?: ').lower()
        month = 'all'
    print('-'*40)
    print('Exploring data for city={}, month={} and day={} ,'.
          format(city, month, day))
    return city, month, day


def load_data(city, month, day):
    """Loads data for the specified city and filters by month and day if \
    applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to \
        apply no month filter
        (str) day - name of the day of week to filter by, or "all" \
        to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    try:
        file = CITY_DATA[city.lower()]

        # load data file into a dataframe
        df = pd.read_csv(file)

        # extract month and day of week from Start Time to create new columns
        df['Start Time'] = pd.to_datetime(df['Start Time'])
        df['month'] = df['Start Time'].dt.month
        df['day_of_week'] = df['Start Time'].dt.weekday_name
        # filter by month if applicable
        if month != 'all':
            # use the index of the months list to get the corresponding int
            # months = ['january', 'february', 'march', 'april', 'may', 'june']
            month = months.index(month)+1
            # print(month)

            # filter by month to create the new dataframe
            df = df.loc[df['month'] == month]
        if day != 'all':
            # filter by day of week to create the new dataframe
            df = df.loc[df['day_of_week'] == day.title()]

        return df
    except Exception as e:
        print('Exception occured: {}'.format(e))
        return None


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    try:
        # display the most common month
        popular_month = df['month'].mode()[0]
        print('Most common Month is {}'.format(popular_month))

        # display the most common day of week
        popular_day = df['day_of_week'].mode()[0]
        print('Most common day of the week is {}'.format(popular_day))

        # display the most common start hour
        popular_start_hour = df['Start Time'].dt.hour.mode()[0]
        print('Most common start hour is {}'.format(popular_start_hour))

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    except Exception as e:
        print('Exception occured {}'.format(e))
        return None


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    try:
        # display most commonly used start station
        popular_start_station = df['Start Station'].mode()[0]
        print('commonly used start station {}'.format(popular_start_station))

        # display most commonly used end station
        popular_end_station = df['End Station'].mode()[0]
        print('commonly used end station is {}'.format(popular_end_station))

        # display most frequent combination of start and end stations trip
        station_combo = df.groupby(['Start Station', 'End Station']).size()
        station_combo_df = station_combo.to_frame(name='count').\
            sort_values('count', ascending=False).reset_index()
        # print(station_combo_df)
        print('frequent start and end stations are {} and {}'.
              format(station_combo_df.loc[0][0], station_combo_df.loc[0][1]))
        # print(df[['Start Station', 'End Station']].mode())
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    except Exception as e:
        print('Exception occured {}'.format(e))
        return None


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    try:
        # display total travel time
        total_travel_time = str(df['Trip Duration'].sum())
        count = str(df['Trip Duration'].count())
        print('Total Travel Time={},count={}'.format(total_travel_time, count))

        # display mean travel time
        avg_travel_time = str(df['Trip Duration'].mean())
        print('Average Travel Time={},count={}'.format(avg_travel_time, count))
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    except Exception as e:
        print('exception occured {}'.format(e))
        return None


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    try:
        # Display counts of user types
        print('Displaying counts of user types')
        for val, cnt in df['User Type'].value_counts().iteritems():
            print('{}={}'.format(val, cnt))

        # Display counts of gender
        print('Displaying the counts of each gender')
        for val, cnt in df['Gender'].value_counts().iteritems():
            print('{}={}'.format(val, cnt))

        # Display earliest, most recent, and most common year of birth
        print('earliest birth year is {}'.format(df['Birth Year'].min()))
        print('recent birth year is {}'.format(df['Birth Year'].max()))
        print('common birth year is {}'.format(df['Birth Year'].mode()[0]))

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)
    except Exception as e:
        print('exception occured {}'.format(e))


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        raw_data = input('\nWould you like to see data? Enter yes or no.\n')
        n = 5
        while raw_data.lower() != 'no':
            print(df[n:n+5])
            raw_data = input('\nWould you like to see more data? Enter \
            yes or no.\n')
            n = n + 5

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
