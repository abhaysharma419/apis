from flask import Flask,request

from services import get_current_time_for_timezones


app = Flask(__name__)

@app.route('/time', methods=['GET'])
def get_current_time():
    """
    Endpoint to get the current time for multiple time zones.
    
    Returns:
        dict: A dictionary containing the current time for each time zone.
    """
    tz = request.args.getlist('tz')
    if len(tz)==0:
        # Default TimeZones in case no timezone is provided in the GET method
        tz = ['America/New_York', 'Europe/London', 'Asia/Tokyo','Asia/Kolkata']

    current_tz_time_dict=get_current_time_for_timezones(tz)
    return  current_tz_time_dict

if __name__ == '__main__':
    app.run(debug=True)