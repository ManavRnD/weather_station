from config import db, app


class weatherStation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mac_id = db.Column(db.String(64), index=True)
    as3935 = db.Column(db.String(64), index=True)
    wind_speed = db.Column(db.String(64), index=True)
    wind_force = db.Column(db.String(64), index=True)
    wind_direction = db.Column(db.String(64), index=True)
    humidity = db.Column(db.String(64), index=True)
    temperature = db.Column(db.String(64), index=True)
    pressure = db.Column(db.String(64), index=True)
    noise = db.Column(db.String(64), index=True)
    rain = db.Column(db.String(64), index=True)
    date_time = db.Column(db.String(64), index=True)


with app.app_context():
    db.create_all()

# ******************** LMAS DAILY PING DB ******************
