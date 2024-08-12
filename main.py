from config import app
from flask import render_template, request, session, redirect, url_for
import sqlite3
from weather_station import weather_station_data


# ******************** LOGIN ROUTE LOGIC ****************
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == 'mepl@123':
            session["username"] = request.form.get("username")
            return redirect(url_for('index'))
        else:
            error = 'Invalid Credentials. Please try again.'

    return render_template('login.html', error=error)


# Logout
@app.route("/logout")
def logout():
    session["username"] = None
    return redirect("/")


# ******************** INDEX PAGE ****************
@app.route('/')
def index():
    if not session.get("username"):
        return redirect("/login")

    with sqlite3.connect("instance/weather-station-database.sqlite") as connection:
        connection.enable_load_extension(True)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM weather_station  WHERE mac_id ORDER BY id DESC")

        data = cursor.fetchall()

    # Render the data in an HTML template
    return render_template('index.html', title='WEATHER STATION DASHBOARD', data=data)


# ******************** WEATHER API CALL ****************
@app.route('/weatherdata', methods=['GET'])
def weather_data_api():
    data = request.args.get("data")
    AS3935 = request.args.get("AS")

    # result = weather_station_data(mac_id, wind_speed, wind_force, wind_direction, humidity, temperature, pressure,
    #                               noise, rain)

    result = weather_station_data(data, AS3935)

    print(result)

    return result


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
