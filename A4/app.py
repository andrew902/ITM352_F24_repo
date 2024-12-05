import json
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import requests
from datetime import datetime, timedelta


# Initialize Flask app
app = Flask(__name__)

API_KEY = "b74e844c4803cdb071a54d67b274fe2c"
BASE_URL = "https://api.openweathermap.org/data/3.0/onecall"

@app.route("/", methods=["GET", "POST"])
def dashboard():
    # Default coordinates for Honolulu 
    lat, lon = 21.3099, 157.8581
    
    # Get weather data
    response = requests.get(
        BASE_URL,
        params={
            "lat": lat,
            "lon": lon,
            "exclude": "minutely,hourly,alerts",
            "units": "imperial",
            "appid": API_KEY,
        },
    )
    weather_data = response.json()

    # Extract 7-day forecast
    forecast = weather_data["daily"][:7]

    return render_template("dashboard.html",forecast=forecast)

@app.template_filter("dateformat")
def dateformat(index):
    from datetime import datetime, timedelta
    target_date = datetime.now() + timedelta(days=index)
    return target_date.strftime("%a, %b %d")



if __name__ == "__main__":
    app.run(debug=True)

