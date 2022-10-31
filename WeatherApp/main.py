from flask import Flask, render_template, request
import data
import datetime
import os

app = Flask(__name__)
API_key = '9292ad5c92460e49877ed8fb49108ea7'

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        forecast()
    else:
        color = os.environ['BG_COLOR']
        return render_template("./index.html",  color=color)


@app.route('/forecast', methods=["GET", "POST"])
def forecast():
    try:
        input_error_flag = 0
        user_input = request.form.get("location").capitalize()
        my_data = data.get_lat_lon(user_input, API_key)
        next_week = [(datetime.date.today() + datetime.timedelta(days=i)).strftime("%d.%m.%Y") for i in range(0, 7)]
        days_name = [(datetime.date.today() + datetime.timedelta(days=i)).strftime("%A") for i in range(0, 7)]
        date_today = str(datetime.date.today())
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        data.appendHistory(user_input, date_today, current_time)
        return render_template("./forecast.html", data=my_data, date=next_week, user_input=user_input,days_name=days_name)
    except Exception:
        input_error_flag = 1
        return render_template("./index.html", error_flag=input_error_flag)



if __name__ == "__main__":
    app.run()
