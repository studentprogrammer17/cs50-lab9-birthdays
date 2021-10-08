import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

db = SQL("sqlite:///birthdays.db")

MONTH_DAY = {}

dates = ["01","02","03","04","05","06","07","08","09","10","11","12"]

MONTHS = [
        "Январь",
        "Февраль",
        "Март",
        "Апрель",
        "Май",
        "Июнь",
        "Июль",
        "Август",
        "Сентябрь",
        "Октябрь",
        "Ноябрь",
        "Декабрь",
    ]


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        surname = request.form.get("surname")
        year = request.form.get("year")
        month = request.form.get("month")
        day = request.form.get("day")
        point = "."

        date = str(day)+str(point)+str(month_to_dat(month))+str(point)+str(year)
        fullname = str(name)+str(" ")+str(surname)

        db.execute("INSERT INTO registrants (fullname,date) VALUES (?, ?)",fullname,date)

        return redirect("/")

    else:

        birthdays = db.execute("SELECT * FROM registrants")

        return render_template("index.html",birthdays = birthdays,months=MONTHS)

def month_to_dat(month):
    if month == "Январь":
        month = "01"
    elif month == "Февраль":
        month = "02"
    elif month == "Март":
        month = "03"
    elif month == "Апрель":
        month = "04"
    elif month == "Май":
        month = "05"
    elif month == "Июнь":
        month = "06"
    elif month == "Июль":
        month = "07"
    elif month == "Август":
        month = "08"
    elif month == "Сентябрь":
        month = "09"
    elif month == "Октябрь":
        month = "10"
    elif month == "Ноябрь":
        month = "11"
    elif month == "Декабрь":
        month = "12"
    return month


