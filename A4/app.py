import json
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, login_manager
import requests
from datetime import datetime, timedelta


# Initialize Flask app
app = Flask(__name__)


# Route for the homepage or dashboard
@app.route("/", methods=["GET", "POST"])
def dashboard():
    return render_template("dashboard.html")


# Route for Recommended Running Routes page
@app.route('/recommended-routes')
def recommended_routes():
    return render_template('recommended-routes.html')

# Route for Marathon Gear page
@app.route('/marathon-gear')
def marathon_gear():
    return render_template('marathon-gear.html')

# Route for Cross Training page
@app.route('/cross-training')
def cross_training():
    return render_template('cross-training.html')


if __name__ == "__main__":
    app.run(debug=True)

