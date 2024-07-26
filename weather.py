import requests
from twilio.rest import Client
from datetime import datetime, timedelta
import time

# Twilio configuration
account_sid = 'your_twilio_account_sid'
auth_token = 'your_twilio_auth_token'
twilio_phone_number = 'your_twilio_phone_number'
your_phone_number = 'your_phone_number'

# Weather API configuration
api_key = 'your_weather_api_key'
latitude = 33.0198
longitude = -96.6989

def get_weather_forecast():
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={latitude}&lon={longitude}&exclude=current,minutely,hourly,alerts&appid={api_key}&units=imperial"
    response = requests.get(url)
    data = response.json()
    daily_forecast = data['daily'][0]  # Today's forecast
    weather_conditions = daily_forecast['weather'][0]['main']
    return weather_conditions

def send_sms(message):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message,
        from_=twilio_phone_number,
        to=your_phone_number
    )
    print(f"Message sent: {message.sid}")

def check_weather_and_send_sms():
    weather_conditions = get_weather_forecast()
    if 'rain' in weather_conditions.lower():
        message = "Good morning! It looks like it's going to rain today in Plano, Texas. Don't forget your umbrella!"
    else:
        message = "Good morning! There's no rain expected today in Plano, Texas. Have a great day!"
    send_sms(message)

if __name__ == "__main__":
    while True:
        now = datetime.now()
        target_time = now.replace(hour=7, minute=0, second=0, microsecond=0)
        if now > target_time:
            target_time += timedelta(days=1)
        sleep_duration = (target_time - now).total_seconds()
        time.sleep(sleep_duration)
        check_weather_and_send_sms()
