import sqlite3
from time import strftime, localtime


def weather_station_data(data, AS3935):
    mac_id = "84:FC:E6:7B:E0:E8"

    try:
        # Parse the hex data
        wind_speed = int(data[0:4], 16)
        wind_speed = round((wind_speed / 100), 2)

        wind_force = int(data[4:8], 16)
        wind_force = round(wind_force, 2)

        wind_direction = int(data[8:12], 16)
        wind_direction = round(wind_direction, 2)

        wind_direction_2 = int(data[12:16], 16)

        humidity = int(data[16:20], 16)
        humidity = round((humidity / 10), 2)

        temperature = int(data[20:24], 16)
        temperature = round((temperature / 10), 2)

        noise = int(data[24:28], 16)
        noise = round((noise / 10), 2)

        pm_25 = int(data[28:32], 16)
        pm_10 = int(data[32:36], 16)

        pressure = int(data[36:40], 16)
        pressure = round((pressure / 10), 2)

        high_lux = int(data[40:44], 16)
        low_lux = int(data[44:48], 16)
        light_lux = int(data[48:52], 16)
        rain = int(data[52:56], 16)
        rain = round((rain / 10), 2)

        date_time = strftime("%Y-%m-%d %H:%M:%S", localtime())

        with sqlite3.connect("instance/weather-station-database.sqlite") as connection:
            connection.enable_load_extension(True)
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO weather_station (as3935, mac_id, wind_speed, wind_force, wind_direction, humidity, "
                "temperature, pressure, noise, rain, date_time) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (AS3935, mac_id, wind_speed, wind_force, wind_direction, humidity, temperature, pressure, noise, rain,
                 date_time))

            connection.commit()

    except Exception as e:
        # Handle the error here, you can print the error message or log it
        # print(f"Error saving data to the database: {e}")
        return e  # Indicate failure to the caller

    return "Success"
