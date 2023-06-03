from datetime import datetime
import pytz
"""
Get the current time for multiple time zones.

Returns:
    dict: A dictionary containing the current time for each time zone.
"""

def get_current_time_for_timezones(timezones):
    
    current_time_with_zone ={}
    # Get the current date and time
    current_time = datetime.now()
    for timezone in timezones:
        # Get the time zone
        timezone_pytz = pytz.timezone(timezone) 
        # Convert the current time to the specified time zone
        localized_time = current_time.astimezone(timezone_pytz)
        # Format the localized time in a human-readable format
        formatted_time = localized_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')
        current_time_with_zone[timezone]=formatted_time
        print(current_time_with_zone)
    return current_time_with_zone
