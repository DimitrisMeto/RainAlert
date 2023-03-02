from twilio.rest import Client
import requests
api_key = "API KEY"
ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"
account_sid = "TWILIO SID"
auth_token = "TWILIO TOKEN"

parameters = {
    "lat": 43.858297,
    "lon": 15.501773,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=ENDPOINT, params=parameters)
response.raise_for_status()
data = response.json()
weather_data = data["hourly"]
twelve_hour_data = weather_data[:12]

rain = False

for hour in twelve_hour_data:
    if int(hour["weather"][0]["id"]) < 700:
        rain = True
if rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="+18508090310",
        to="+MY PHONE"
    )
    print(message.status)



